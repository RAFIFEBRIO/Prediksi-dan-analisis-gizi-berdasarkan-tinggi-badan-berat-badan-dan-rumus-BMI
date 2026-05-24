import streamlit as st

def section_header(title, subtitle=""):
    st.markdown(f"""
    <div style='background:white; border-radius:16px; padding:1.8rem 2rem;
                border:1px solid #e2e8f0; margin-bottom:1.5rem;
                box-shadow:0 1px 4px rgba(0,0,0,0.05); border-left:4px solid #2563eb;'>
        <h1 style='margin:0; color:#0f172a !important; font-size:1.8rem; font-weight:800;'>{title}</h1>
        {f"<p style='margin:0.2rem 0 0 0; color:#64748b; font-size:0.9rem;'>{subtitle}</p>" if subtitle else ""}
    </div>
    """, unsafe_allow_html=True)

section_header("BMI Analysis & Klasifikasi Obesitas",
               "Data Mining Project — Classification & Clustering")

# Badges (tanpa ikon)
st.markdown("""
<div style='display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:1.5rem;'>
    <span style='background:#eff6ff; color:#2563eb; padding:0.3rem 0.85rem; border-radius:20px;
                 font-size:0.8rem; font-weight:600; border:1px solid #bfdbfe;'>Random Forest</span>
    <span style='background:#eff6ff; color:#2563eb; padding:0.3rem 0.85rem; border-radius:20px;
                 font-size:0.8rem; font-weight:600; border:1px solid #bfdbfe;'>KMeans Clustering</span>
    <span style='background:#eff6ff; color:#2563eb; padding:0.3rem 0.85rem; border-radius:20px;
                 font-size:0.8rem; font-weight:600; border:1px solid #bfdbfe;'>SHAP Explainable AI</span>
    <span style='background:#eff6ff; color:#2563eb; padding:0.3rem 0.85rem; border-radius:20px;
                 font-size:0.8rem; font-weight:600; border:1px solid #bfdbfe;'>CRISP-DM</span>
</div>
""", unsafe_allow_html=True)

# Metrik
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Data", "741", "record")
c2.metric("Fitur", "5", "atribut")
c3.metric("Metode", "2", "algoritma")
c4.metric("Kategori BMI", "4", "kelas")

st.markdown("---")

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    <div style='background:white; border-radius:16px; padding:1.8rem;
                border:1px solid #e2e8f0; box-shadow:0 1px 4px rgba(0,0,0,0.05);'>
        <h3 style='color:#0f172a !important; margin-top:0; font-size:1.05rem;'>Deskripsi Proyek</h3>
        <p style='color:#475569; line-height:1.8; font-size:0.92rem;'>
            Proyek ini mengembangkan sistem berbasis Data Mining
            untuk menganalisis dan mengklasifikasikan status BMI seseorang berdasarkan
            data  meliputi umur, tinggi badan, berat badan, dan nilai BMI.
        </p>
        <p style='color:#475569; font-weight:600; font-size:0.92rem; margin-bottom:0.5rem;'>Masalah yang diselesaikan:</p>
        <ul style='color:#475569; line-height:1.9; font-size:0.92rem; margin:0; padding-left:1.2rem;'>
            <li>Klasifikasi kategori BMI: Kurus, Normal, Overweight, Obesitas</li>
            <li>Pengelompokan populasi menggunakan clustering</li>
            <li>Skrining awal risiko kesehatan berbasis BMI secara otomatis</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='background:#0f172a; border-radius:16px; padding:1.8rem;'>
        <div style='font-size:0.72rem; color:#475569; letter-spacing:0.08em;
                    text-transform:uppercase; margin-bottom:1rem;'>INFO PROYEK</div>
        <div style='border-top:1px solid #1e293b; padding-top:1rem;'>
            <div style='font-size:0.72rem; color:#475569; letter-spacing:0.06em;
                        text-transform:uppercase; margin-bottom:0.4rem;'>METODE</div>
            <div style='color:#e2e8f0; font-size:0.88rem; line-height:1.8; margin-bottom:1rem;'>
                Random Forest Classifier<br>KMeans Clustering
            </div>
            <div style='font-size:0.72rem; color:#475569; letter-spacing:0.06em;
                        text-transform:uppercase; margin-bottom:0.4rem;'>DATASET</div>
            <div style='color:#e2e8f0; font-size:0.88rem; line-height:1.8; margin-bottom:1rem;'>
                741 record · 5 atribut<br>Sumber: Kaggle
            </div>
            <div style='font-size:0.72rem; color:#475569; letter-spacing:0.06em;
                        text-transform:uppercase; margin-bottom:0.4rem;'>FRAMEWORK</div>
            <div style='color:#e2e8f0; font-size:0.88rem;'>CRISP-DM</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("### Identitas Anggota Kelompok")

members = [
    {"nama": "Muhammad Rafi Febrio", "nim": "24051214196"},
    {"nama": "Najwa Fatimah Azzahra", "nim": "24051214158"},
]
cols = st.columns(2)
for col, m in zip(cols, members):
    with col:
        st.markdown(f"""
        <div style='background:white; border-radius:16px; padding:1.5rem;
                    border:1px solid #e2e8f0; text-align:center;
                    box-shadow:0 1px 4px rgba(0,0,0,0.05);'>
            <div style='width:56px; height:56px; background:#2563eb; border-radius:50%;
                        display:flex; align-items:center; justify-content:center;
                        margin:0 auto 0.8rem auto;'>
                <span style='color:white; font-size:1.2rem; font-weight:700;'>{m['nama'][0]}</span>
            </div>
            <div style='font-size:1rem; font-weight:700; color:#0f172a; margin-bottom:0.5rem;'>{m['nama']}</div>
            <span style='background:#f1f5f9; color:#475569; padding:0.3rem 0.9rem;
                         border-radius:20px; font-size:0.8rem; font-weight:500;
                         border:1px solid #e2e8f0;'>{m['nim']}</span>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("### Alur Proyek (CRISP-DM)")
steps = [
    ("1", "Business Understanding", "Identifikasi masalah & tujuan klasifikasi BMI"),
    ("2", "Data Understanding", "Eksplorasi dataset 741 record dari Kaggle"),
    ("3", "Data Preparation", "Cleaning, encoding, scaling fitur"),
    ("4", "Modeling", "Random Forest + KMeans Clustering"),
    ("5", "Evaluation", "Accuracy, F1-Score, Silhouette Score"),
    ("6", "Deployment", "Aplikasi web Streamlit"),
]
cols = st.columns(3)
for i, (num, title, desc) in enumerate(steps):
    with cols[i % 3]:
        st.markdown(f"""
        <div style='background:white; border-radius:14px; padding:1.2rem;
                    margin-bottom:1rem; border:1px solid #e2e8f0;
                    box-shadow:0 1px 4px rgba(0,0,0,0.05); border-top:3px solid #2563eb;'>
            <div style='width:28px; height:28px; background:#2563eb; border-radius:50%;
                        display:flex; align-items:center; justify-content:center;
                        margin-bottom:0.5rem;'>
                <span style='color:white; font-size:0.8rem; font-weight:700;'>{num}</span>
            </div>
            <div style='font-size:0.88rem; font-weight:600; color:#0f172a; margin-bottom:0.3rem;'>{title}</div>
            <div style='font-size:0.78rem; color:#64748b;'>{desc}</div>
        </div>
        """, unsafe_allow_html=True)
