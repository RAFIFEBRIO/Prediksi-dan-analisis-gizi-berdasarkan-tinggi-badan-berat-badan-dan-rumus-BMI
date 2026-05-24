import streamlit as st
import pandas as pd

st.markdown("""
<div style='background:white; border-radius:16px; padding:1.8rem 2rem;
            border:1px solid #e2e8f0; margin-bottom:1.5rem;
            box-shadow:0 1px 4px rgba(0,0,0,0.05); border-left:4px solid #2563eb;'>
    <h1 style='margin:0; color:#0f172a !important; font-size:1.8rem; font-weight:800;'>About</h1>
    <p style='margin:0.2rem 0 0 0; color:#64748b; font-size:0.9rem;'>
        Informasi lengkap mengenai proyek, dataset, dan metode
    </p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Metode", "Dataset", "Proyek"])

with tab1:
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("""
        <div style='background:white; border-radius:16px; padding:1.5rem;
                    border:1px solid #e2e8f0; box-shadow:0 1px 4px rgba(0,0,0,0.05);
                    border-top:3px solid #2563eb; height:100%;'>
            <h3 style='color:#0f172a !important; margin-top:0; font-size:1rem;'>Random Forest (Classification)</h3>
            <p style='color:#475569; font-size:0.88rem; line-height:1.8;'>
                Algoritma ensemble learning yang membangun banyak decision tree
                dan menggabungkan hasilnya melalui majority voting.
            </p>
            <p style='color:#0f172a; font-weight:600; font-size:0.85rem; margin-bottom:0.4rem;'>Cara Kerja:</p>
            <ol style='color:#475569; font-size:0.85rem; line-height:1.9; margin:0 0 1rem 0; padding-left:1.2rem;'>
                <li>Bootstrap Sampling dari data training</li>
                <li>Setiap tree membuat prediksi independen</li>
                <li>Hasil akhir = majority vote</li>
            </ol>
            <p style='color:#0f172a; font-weight:600; font-size:0.85rem; margin-bottom:0.4rem;'>Kelebihan:</p>
            <ul style='color:#475569; font-size:0.85rem; line-height:1.9; margin:0 0 1rem 0; padding-left:1.2rem;'>
                <li>Akurasi tinggi, robust terhadap overfitting</li>
                <li>Memberikan feature importance</li>
                <li>Tidak sensitif terhadap outlier</li>
            </ul>
            <div style='background:#f8fafc; border-radius:8px; padding:0.8rem;
                        border:1px solid #e2e8f0; font-size:0.82rem; color:#475569;'>
                <b>Parameter:</b> n_estimators=100, random_state=42, test_size=0.2
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='background:white; border-radius:16px; padding:1.5rem;
                    border:1px solid #e2e8f0; box-shadow:0 1px 4px rgba(0,0,0,0.05);
                    border-top:3px solid #2563eb; height:100%;'>
            <h3 style='color:#0f172a !important; margin-top:0; font-size:1rem;'>KMeans Clustering</h3>
            <p style='color:#475569; font-size:0.88rem; line-height:1.8;'>
                Algoritma unsupervised learning yang membagi data menjadi k kelompok
                berdasarkan kedekatan jarak ke centroid.
            </p>
            <p style='color:#0f172a; font-weight:600; font-size:0.85rem; margin-bottom:0.4rem;'>Cara Kerja:</p>
            <ol style='color:#475569; font-size:0.85rem; line-height:1.9; margin:0 0 1rem 0; padding-left:1.2rem;'>
                <li>Inisialisasi k centroid (k-means++)</li>
                <li>Assign data ke centroid terdekat</li>
                <li>Update centroid ke rata-rata cluster</li>
                <li>Ulangi hingga konvergen</li>
            </ol>
            <p style='color:#0f172a; font-weight:600; font-size:0.85rem; margin-bottom:0.4rem;'>Evaluasi:</p>
            <ul style='color:#475569; font-size:0.85rem; line-height:1.9; margin:0 0 1rem 0; padding-left:1.2rem;'>
                <li>Elbow Method (WCSS/Inertia)</li>
                <li>Silhouette Score</li>
            </ul>
            <div style='background:#f8fafc; border-radius:8px; padding:0.8rem;
                        border:1px solid #e2e8f0; font-size:0.82rem; color:#475569;'>
                <b>Parameter:</b> n_clusters=3, n_init=10, random_state=42
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='background:#f8fafc; border-radius:16px; padding:1.5rem;
                border:1px solid #e2e8f0; border-left:4px solid #2563eb;'>
        <h3 style='color:#0f172a !important; margin-top:0; font-size:1rem;'>SHAP — Explainable AI</h3>
        <p style='color:#475569; font-size:0.88rem; line-height:1.8; margin:0;'>
            <b style='color:#0f172a;'>SHAP (SHapley Additive exPlanations)</b> adalah metode untuk menjelaskan
            output model machine learning berdasarkan teori permainan (game theory). SHAP mengukur
            kontribusi marginal setiap fitur terhadap prediksi model sehingga model "black-box"
            menjadi lebih transparan dan dapat diinterpretasi.
        </p>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div style='background:white; border-radius:16px; padding:1.5rem;
                border:1px solid #e2e8f0; box-shadow:0 1px 4px rgba(0,0,0,0.05); margin-bottom:1rem;'>
        <h3 style='color:#0f172a !important; margin-top:0; font-size:1rem;'>Informasi Dataset</h3>
    </div>
    """, unsafe_allow_html=True)

    info = pd.DataFrame({
        "Properti": ["Nama","Sumber","Jumlah Record","Jumlah Atribut","Missing Values","Format"],
        "Nilai": ["Age Weight Height BMI Analysis","Kaggle","741","5","Tidak ada","CSV"]
    })
    st.dataframe(info, use_container_width=True, hide_index=True)

    st.markdown("### Atribut Dataset")
    attrs = pd.DataFrame({
        "Atribut": ["Age","Height","Weight","Bmi","BmiClass"],
        "Tipe": ["Integer","Float","Float","Float","String"],
        "Deskripsi": ["Umur individu (15–61 tahun)","Tinggi badan (meter, 1.46–2.07)",
                      "Berat badan (kg, 25.9–270)","BMI = Weight / Height²","Kategori BMI (6 kelas)"],
        "Peran": ["Input","Input","Input","Input + Target","Referensi"]
    })
    st.dataframe(attrs, use_container_width=True, hide_index=True)

    st.markdown("### Label Kelas")
    labels = pd.DataFrame({
        "Kategori": ["Kurus","Normal","Overweight","Obesitas"],
        "Rentang BMI": ["< 18.5","18.5 – 24.9","25.0 – 29.9","≥ 30.0"],
        "Risiko Kesehatan": ["Tinggi","Rendah","Sedang","Tinggi"]
    })
    st.dataframe(labels, use_container_width=True, hide_index=True)

with tab3:
    col1, col2 = st.columns(2, gap="large")
    with col1:
        proj = pd.DataFrame({
            "Properti": ["Mata Kuliah","Jenis Tugas","Metodologi","Framework Web","Tahun"],
            "Nilai": ["Data Mining","UAS","CRISP-DM","Streamlit","2026"]
        })
        st.markdown("#### Info Proyek")
        st.dataframe(proj, use_container_width=True, hide_index=True)

    with col2:
        libs = pd.DataFrame({
            "Library": ["pandas","numpy","scikit-learn","matplotlib","seaborn","streamlit","shap","joblib"],
            "Kegunaan": ["Manipulasi data","Operasi array","Machine learning",
                         "Visualisasi","Statistik visual","Web app","Explainable AI","Simpan model"]
        })
        st.markdown("#### Library")
        st.dataframe(libs, use_container_width=True, hide_index=True)

    st.markdown("#### Struktur Folder")
    st.code("""
UAS_DataMining_Obesity/
├── dataset/
│   └── datasetbmi.csv
├── notebook/
│   └── Analysis.ipynb
├── model/
│   ├── classifier.pkl
│   ├── kmeans.pkl
│   ├── scaler.pkl
│   └── cluster_labels.json
├── app/
│   ├── app.py
│   ├── assets/
│   └── view/
│       ├── home.py
│       ├── dataset_overview.py
│       ├── prediction.py
│       ├── visualization.py
│       └── about.py
├── requirements.txt
└── README.md
    """)
