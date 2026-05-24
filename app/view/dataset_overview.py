import streamlit as st
import pandas as pd
import os

APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(APP_DIR, "..", "dataset", "datasetbmi.csv")
df = pd.read_csv(file_path)

st.markdown("""
<div style='background:white; border-radius:16px; padding:1.8rem 2rem;
            border:1px solid #e2e8f0; margin-bottom:1.5rem;
            box-shadow:0 1px 4px rgba(0,0,0,0.05); border-left:4px solid #2563eb;'>
    <h1 style='margin:0; color:#0f172a !important; font-size:1.8rem; font-weight:800;'>Dataset Overview</h1>
    <p style='margin:0.2rem 0 0 0; color:#64748b; font-size:0.9rem;'>Eksplorasi dan analisis dataset BMI</p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Jumlah Data", f"{df.shape[0]:,}")
c2.metric("Jumlah Kolom", df.shape[1])
c3.metric("Missing Values", int(df.isnull().sum().sum()))
c4.metric("Sumber", "Kaggle")

st.markdown("---")

st.markdown("""
<div style='background:white; border-radius:16px; padding:1.5rem;
            border:1px solid #e2e8f0; box-shadow:0 1px 4px rgba(0,0,0,0.05); margin-bottom:1rem;'>
    <h3 style='color:#0f172a !important; margin-top:0; font-size:1rem;'>Informasi Dataset</h3>
    <p style='color:#475569; font-size:0.9rem; margin:0;'>
        <b>Sumber:</b>
        <a href='https://www.kaggle.com/datasets/rukenmissonnier/age-weight-height-bmi-analysis'
           target='_blank' style='color:#2563eb; text-decoration:none; font-weight:500;'>
            Kaggle — Age Weight Height BMI Analysis
        </a>
    </p>
    <p style='color:#475569; font-size:0.9rem; margin:0.5rem 0 0 0;'>
        Dataset berisi data antropometri dari 741 individu mencakup umur, tinggi badan,
        berat badan, nilai BMI, dan kategori BMI.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("### Deskripsi Kolom")
col_info = pd.DataFrame({
    "Kolom": ["Age", "Height", "Weight", "Bmi", "BmiClass"],
    "Tipe": ["int64", "float64", "float64", "float64", "object"],
    "Keterangan": ["Umur individu (tahun)", "Tinggi badan (meter)",
                   "Berat badan (kg)", "BMI = Weight / Height²",
                   "Kategori BMI original (6 kelas)"],
    "Rentang": ["15 – 61", "1.46 – 2.07", "25.9 – 270", "12.15 – 66.30", "6 kategori"]
})
st.dataframe(col_info, use_container_width=True, hide_index=True)

st.markdown("---")
st.markdown("### Preview Dataset")
n_rows = st.slider("Tampilkan berapa baris?", 5, 50, 10)
st.dataframe(df.head(n_rows), use_container_width=True)

st.markdown("---")
col1, col2 = st.columns([1.5, 1])
with col1:
    st.markdown("### Statistik Deskriptif")
    st.dataframe(df.describe().round(3), use_container_width=True)
with col2:
    st.markdown("### Distribusi BmiClass")
    bmi_counts = df['BmiClass'].value_counts().reset_index()
    bmi_counts.columns = ['BmiClass', 'Jumlah']
    bmi_counts['%'] = (bmi_counts['Jumlah']/len(df)*100).round(1).astype(str)+'%'
    st.dataframe(bmi_counts, use_container_width=True, hide_index=True)
    st.bar_chart(df['BmiClass'].value_counts())

st.markdown("---")
st.markdown("### Pengecekan Missing Values")
mv = df.isnull().sum().reset_index()
mv.columns = ['Kolom', 'Missing']
mv['Status'] = mv['Missing'].apply(lambda x: 'Lengkap' if x == 0 else f'{x} missing')
st.dataframe(mv, use_container_width=True, hide_index=True)
