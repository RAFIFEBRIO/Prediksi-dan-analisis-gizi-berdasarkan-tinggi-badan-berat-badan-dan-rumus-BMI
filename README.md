 UAS Data Mining - BMI Analysis & Klasifikasi Obesitas

Deskripsi
Proyek Data Mining untuk menganalisis dan mengklasifikasikan status BMI menggunakan:
- Classification: Random Forest Classifier
- Clustering: KMeans (k=3)

 Anggota Kelompok
- Muhammad Rafi Febrio - 24051214196
- Najwa Fatimah Azzahra - 24051214158

 Dataset
- Sumber: Kaggle - Age Weight Height BMI Analysis
- 741 record, 5 atribut
- Link: https://www.kaggle.com/datasets/rukenmissonnier/age-weight-height-bmi-analysis

 Cara Menjalankan
1. Install dependencies
   pip install -r requirements.txt

2. Jalankan aplikasi web
   cd UAS_DataMining_Obesity/app
   python -m streamlit run app.py

 Struktur Folder
- dataset/ → dataset CSV
- notebook/ → analysis.ipynb
- model/ → model pkl dan json
- app/ → aplikasi Streamlit
- requirements.txt