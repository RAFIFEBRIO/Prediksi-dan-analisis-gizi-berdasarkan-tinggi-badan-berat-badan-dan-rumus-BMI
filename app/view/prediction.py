import streamlit as st
import numpy as np
import pandas as pd
import joblib, json, os

APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(APP_DIR, "..", "model")

@st.cache_resource
def load_models():
    clf            = joblib.load(os.path.join(MODEL_DIR, "classifier.pkl"))
    kmeans         = joblib.load(os.path.join(MODEL_DIR, "kmeans.pkl"))
    scaler         = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
    scaler_cluster = joblib.load(os.path.join(MODEL_DIR, "scaler_cluster.pkl"))
    with open(os.path.join(MODEL_DIR, "cluster_labels.json"), encoding="utf-8") as f:
        cmap = json.load(f)
    return clf, kmeans, scaler, scaler_cluster, cmap

clf, kmeans, scaler, scaler_cluster, cluster_map = load_models()
cluster_map = {int(k): v for k, v in cluster_map.items()}

st.markdown("""
<div style='background:white; border-radius:16px; padding:1.8rem 2rem;
            border:1px solid #e2e8f0; margin-bottom:1.5rem;
            box-shadow:0 1px 4px rgba(0,0,0,0.05); border-left:4px solid #2563eb;'>
    <h1 style='margin:0; color:#0f172a !important; font-size:1.8rem; font-weight:800;'>Prediksi Kategori BMI</h1>
    <p style='margin:0.2rem 0 0 0; color:#64748b; font-size:0.9rem;'>
        Masukkan data untuk mendapatkan prediksi kategori BMI dan kelompok cluster
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("""
    <div style='background:white; border-radius:16px; padding:1.5rem;
                border:1px solid #e2e8f0; box-shadow:0 1px 4px rgba(0,0,0,0.05);
                margin-bottom:1rem;'>
        <h3 style='color:#0f172a !important; margin-top:0; font-size:1rem;'>Form Input</h3>
    </div>
    """, unsafe_allow_html=True)

    age    = st.number_input("Umur (tahun)", min_value=1, max_value=100, value=25, step=1)
    height = st.number_input("Tinggi Badan (cm)", min_value=50.0, max_value=250.0, value=170.0, step=0.1)
    weight = st.number_input("Berat Badan (kg)", min_value=10.0, max_value=300.0, value=65.0, step=0.1)

    height_m = height / 100
    bmi = weight / (height_m ** 2)

    if bmi < 18.5:   bmi_color, bmi_label = "#3b82f6", "Kurus (Underweight)"
    elif bmi < 25:   bmi_color, bmi_label = "#22c55e", "Normal"
    elif bmi < 30:   bmi_color, bmi_label = "#f59e0b", "Overweight"
    else:            bmi_color, bmi_label = "#ef4444", "Obesitas"

    st.markdown(f"""
    <div style='background:#f8fafc; border-radius:12px; padding:1rem 1.2rem;
                border:1px solid #e2e8f0; border-left:4px solid {bmi_color}; margin:1rem 0;'>
        <div style='font-size:0.72rem; color:#64748b; letter-spacing:0.06em;
                    text-transform:uppercase; margin-bottom:0.3rem;'>BMI Terhitung</div>
        <div style='font-size:2rem; font-weight:800; color:{bmi_color}; line-height:1;'>{bmi:.2f}</div>
        <div style='font-size:0.85rem; color:#475569; margin-top:0.3rem;'>{bmi_label}</div>
    </div>
    """, unsafe_allow_html=True)

    process = st.button("Proses Prediksi", use_container_width=True, type="primary")

with col2:
    st.markdown("""
    <div style='background:white; border-radius:16px; padding:1.5rem;
                border:1px solid #e2e8f0; box-shadow:0 1px 4px rgba(0,0,0,0.05);
                margin-bottom:1rem;'>
        <h3 style='color:#0f172a !important; margin-top:0; font-size:1rem;'>Hasil Prediksi</h3>
    </div>
    """, unsafe_allow_html=True)

    if process:
        # Classifier: pakai 4 fitur (Age, Height, Weight, Bmi)
        xs = scaler.transform(np.array([[age, height_m, weight, bmi]]))
        prediction  = clf.predict(xs)[0]
        probability = clf.predict_proba(xs)[0]

        # Cluster: pakai Weight + Bmi saja (sesuai training)
        xc = scaler_cluster.transform(np.array([[weight, bmi]]))
        cluster_id  = int(kmeans.predict(xc)[0])
        cluster_lbl = cluster_map.get(cluster_id, f"Cluster {cluster_id}")

        cmap_pred = {"Kurus":"#3b82f6","Normal":"#22c55e","Overweight":"#f59e0b","Obesitas":"#ef4444"}
        color = cmap_pred.get(prediction, "#64748b")

        st.markdown(f"""
        <div style='background:white; border-radius:16px; padding:1.8rem;
                    border:1px solid #e2e8f0; text-align:center;
                    box-shadow:0 1px 4px rgba(0,0,0,0.05); border-top:4px solid {color};
                    margin-bottom:1rem;'>
            <div style='font-size:0.72rem; color:#64748b; letter-spacing:0.1em;
                        text-transform:uppercase; margin-bottom:0.6rem;'>Hasil Klasifikasi</div>
            <div style='font-size:2.2rem; font-weight:800; color:{color};'>{prediction}</div>
            <div style='font-size:0.78rem; color:#94a3b8; margin-top:0.4rem;'>Random Forest Classifier</div>
        </div>
        <div style='background:#f8fafc; border-radius:12px; padding:1rem 1.2rem;
                    border:1px solid #e2e8f0; margin-bottom:1rem;'>
            <div style='font-size:0.72rem; color:#64748b; letter-spacing:0.06em;
                        text-transform:uppercase; margin-bottom:0.3rem;'>Cluster</div>
            <div style='font-size:0.95rem; font-weight:600; color:#0f172a;'>{cluster_lbl}</div>
            <div style='font-size:0.78rem; color:#94a3b8;'>KMeans Clustering (k=3)</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**Probabilitas Prediksi:**")
        for cls, prob in sorted(zip(clf.classes_, probability), key=lambda x: -x[1]):
            st.markdown(f"**{cls}** — {prob*100:.1f}%")
            st.progress(float(prob))

        st.markdown(f"""
        <div style='background:#f8fafc; border-radius:12px; padding:1rem 1.2rem;
                    border:1px solid #e2e8f0; margin-top:1rem;'>
            <div style='font-size:0.72rem; color:#64748b; letter-spacing:0.06em;
                        text-transform:uppercase; margin-bottom:0.4rem;'>Ringkasan Input</div>
            <div style='color:#475569; font-size:0.88rem; line-height:1.8;'>
                Umur: <b>{age} thn</b> &nbsp;·&nbsp; Tinggi: <b>{height} cm</b>
                &nbsp;·&nbsp; Berat: <b>{weight} kg</b> &nbsp;·&nbsp; BMI: <b>{bmi:.2f}</b>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("Isi form di sebelah kiri lalu klik **Proses Prediksi**")
        st.markdown("#### Referensi Kategori BMI")
        st.dataframe(pd.DataFrame({
            "Kategori": ["Kurus","Normal","Overweight","Obesitas"],
            "Rentang BMI": ["< 18.5","18.5 – 24.9","25.0 – 29.9","≥ 30.0"],
            "Risiko": ["Tinggi","Rendah","Sedang","Tinggi"]
        }), use_container_width=True, hide_index=True)
