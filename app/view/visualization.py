import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os, joblib, json

APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS  = os.path.join(APP_DIR, "assets")
df = pd.read_csv(os.path.join(APP_DIR, "..", "dataset", "datasetbmi.csv"))

def bmi_cat(b):
    if b < 18.5: return 'Kurus'
    elif b < 25: return 'Normal'
    elif b < 30: return 'Overweight'
    else: return 'Obesitas'

df['Category'] = df['Bmi'].apply(bmi_cat)
cmap = {"Kurus":"#3b82f6","Normal":"#22c55e","Overweight":"#f59e0b","Obesitas":"#ef4444"}

st.markdown("""
<div style='background:white; border-radius:16px; padding:1.8rem 2rem;
            border:1px solid #e2e8f0; margin-bottom:1.5rem;
            box-shadow:0 1px 4px rgba(0,0,0,0.05); border-left:4px solid #2563eb;'>
    <h1 style='margin:0; color:#0f172a !important; font-size:1.8rem; font-weight:800;'>Visualization</h1>
    <p style='margin:0.2rem 0 0 0; color:#64748b; font-size:0.9rem;'>
        Visualisasi eksplorasi data dan hasil analisis model
    </p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["Distribusi Data","Korelasi & Outlier",
                                   "Hasil Clustering","Evaluasi Model"])

def show_img(name):
    path = os.path.join(ASSETS, name)
    if os.path.exists(path):
        st.image(path, use_container_width=True)
        return True
    return False

with tab1:
    show_img("distribusi_fitur.png")
    show_img("eda_kategori.png")
    st.markdown("#### Distribusi BMI Interaktif")
    fig, ax = plt.subplots(figsize=(10, 4))
    for cat, color in cmap.items():
        ax.hist(df[df['Category']==cat]['Bmi'], alpha=0.65, label=cat, color=color, bins=20)
    ax.set_title("Distribusi BMI per Kategori", fontweight='bold', fontsize=12)
    ax.set_xlabel("BMI"); ax.set_ylabel("Frekuensi"); ax.legend()
    fig.patch.set_facecolor('white')
    st.pyplot(fig); plt.close()

with tab2:
    if not show_img("correlation.png"):
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(df[['Age','Height','Weight','Bmi']].corr(),
                    annot=True, fmt='.3f', cmap='Blues', ax=ax)
        st.pyplot(fig); plt.close()
    show_img("boxplot_outlier.png")

with tab3:
    show_img("elbow_silhouette.png")
    show_img("cluster_scatter.png")
    st.markdown("#### Statistik per Cluster")
    try:
        MD = os.path.join(APP_DIR, "..", "model")
        # Pakai scaler_cluster (Weight+Bmi) — sesuai model baru
        sc_cluster = joblib.load(os.path.join(MD, "scaler_cluster.pkl"))
        km = joblib.load(os.path.join(MD, "kmeans.pkl"))
        with open(os.path.join(MD, "cluster_labels.json"), encoding="utf-8") as f:
            cl = {int(k): v for k, v in json.load(f).items()}
        X_cluster = df[['Weight', 'Bmi']].values
        df['ClusterLabel'] = [cl.get(int(c), str(c)) for c in km.predict(sc_cluster.transform(X_cluster))]
        stats = df.groupby('ClusterLabel')[['Age','Height','Weight','Bmi']].mean().round(2)
        st.dataframe(stats, use_container_width=True)
    except Exception as e:
        st.warning(f"Model tidak dapat dimuat: {e}")

with tab4:
    show_img("confusion_matrix.png")
    show_img("feature_importance.png")
    if show_img("shap_importance.png"):
        st.caption("SHAP menunjukkan kontribusi setiap fitur terhadap keputusan model secara transparan.")
    else:
        st.info("SHAP image tidak tersedia.")
