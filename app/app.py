import streamlit as st
import os
import sys

st.set_page_config(
    page_title="BMI Analysis App",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
@import url('https://fonts.googleapis.com/icon?family=Material+Icons');

/* ── FIX: keyboard_double_arrow_right muncul sebagai teks ── */
.material-icons,
[data-testid="stSidebarCollapseButton"] span,
[data-testid="collapsedControl"] span {
    font-family: 'Material Icons' !important;
}
[data-testid="stSidebarCollapseButton"],
[data-testid="collapsedControl"] {
    display: none !important;
}

* { font-family: 'Inter', sans-serif !important; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #0f172a !important;
    border-right: 1px solid #1e293b;
}
[data-testid="stSidebar"] * { color: #cbd5e1 !important; }
[data-testid="stSidebar"] .stButton > button {
    border-radius: 10px !important;
    font-weight: 500 !important;
    font-size: 0.88rem !important;
    border: 1px solid transparent !important;
    transition: all 0.2s ease !important;
    text-align: left !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
    background: #1e293b !important;
    border-color: #334155 !important;
    transform: translateX(3px) !important;
}
[data-testid="stSidebar"] .stButton > button[kind="primary"] {
    background: #ef4444 !important;
    border-color: #ef4444 !important;
    color: white !important;
}

/* ── Background ── */
.stApp { background: #f1f5f9; }
.main .block-container { padding: 2rem 3rem; max-width: 1200px; }

/* ── Metric cards ── */
[data-testid="metric-container"] {
    background: white !important;
    border-radius: 14px !important;
    padding: 1.2rem 1.5rem !important;
    border: 1px solid #e2e8f0 !important;
    border-top: 3px solid #2563eb !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
}
[data-testid="stMetricLabel"] p { color: #64748b !important; font-size: 0.8rem !important; font-weight: 500 !important; text-transform: uppercase; letter-spacing: 0.05em; }
[data-testid="stMetricValue"] { color: #0f172a !important; font-weight: 700 !important; font-size: 1.6rem !important; }
[data-testid="stMetricDelta"] { color: #2563eb !important; font-size: 0.78rem !important; }

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: #e2e8f0;
    border-radius: 12px;
    padding: 4px;
    gap: 4px;
    border: none;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 9px !important;
    padding: 0.45rem 1.2rem !important;
    font-weight: 500 !important;
    font-size: 0.88rem !important;
    color: #64748b !important;
    border: none !important;
}
.stTabs [aria-selected="true"] {
    background: white !important;
    color: #0f172a !important;
    font-weight: 600 !important;
    box-shadow: 0 1px 4px rgba(0,0,0,0.12) !important;
}

/* ── Dataframe / Table fix ── */
[data-testid="stDataFrame"] { border-radius: 12px !important; border: 1px solid #e2e8f0 !important; overflow: hidden; }
[data-testid="stDataFrame"] * { color: #0f172a !important; }
.dvn-scroller, .dvn-scroller * { color: #0f172a !important; }
[data-testid="stDataFrame"] th { color: #0f172a !important; font-weight: 600 !important; background: #f8fafc !important; }
[data-testid="stDataFrame"] td { color: #0f172a !important; }
.stDataFrame canvas { color: #0f172a !important; }

/* ── Primary button ── */
.stButton > button[kind="primary"] {
    background: #2563eb !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    letter-spacing: 0.01em !important;
    box-shadow: 0 4px 12px rgba(37,99,235,0.3) !important;
    transition: all 0.2s ease !important;
    padding: 0.6rem 1.5rem !important;
}
.stButton > button[kind="primary"]:hover {
    background: #1d4ed8 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 18px rgba(37,99,235,0.4) !important;
}

/* ── Alerts ── */
[data-testid="stAlert"] { border-radius: 12px !important; font-size: 0.9rem !important; }

/* ── Divider ── */
hr { border: none !important; border-top: 1px solid #e2e8f0 !important; margin: 1.5rem 0 !important; }

/* ── Number input ── */
[data-testid="stNumberInput"] input { border-radius: 8px !important; }

/* ── Slider ── */
[data-testid="stSlider"] { padding: 0.5rem 0; }

/* ── FIX: Label input field ── */
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] label,
label { color: #0f172a !important; }

/* ── FIX: Teks di dalam dataframe/tabel ── */
[data-testid="stDataFrame"] *,
[data-testid="stDataFrameGlideDataEditor"] *,
.dvn-scroller * { color: #0f172a !important; }

/* ══════════════════════════════════════════════════════
   FIX UTAMA: Semua heading & teks di area main (konten)
   harus hitam — override dari sidebar star selector
   ══════════════════════════════════════════════════════ */
.main h1, .main h2, .main h3, .main h4, .main h5, .main h6 {
    color: #0f172a !important;
}
.main p, .main li, .main span, .main div {
    color: #0f172a;
}
/* Markdown headings (### #### dst) yang dirender Streamlit */
.main [data-testid="stMarkdownContainer"] h1,
.main [data-testid="stMarkdownContainer"] h2,
.main [data-testid="stMarkdownContainer"] h3,
.main [data-testid="stMarkdownContainer"] h4,
.main [data-testid="stMarkdownContainer"] h5,
.main [data-testid="stMarkdownContainer"] h6 {
    color: #0f172a !important;
}
.main [data-testid="stMarkdownContainer"] p,
.main [data-testid="stMarkdownContainer"] li,
.main [data-testid="stMarkdownContainer"] strong,
.main [data-testid="stMarkdownContainer"] b {
    color: #0f172a !important;
}
/* stMarkdown class (cara lain Streamlit render markdown) */
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3,
.stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
    color: #0f172a !important;
}
.stMarkdown p, .stMarkdown li, .stMarkdown strong, .stMarkdown b {
    color: #0f172a !important;
}
/* Heading Streamlit native (st.header, st.subheader, st.title) */
[data-testid="stHeading"],
[data-testid="stHeadingWithActionElements"] {
    color: #0f172a !important;
}
[data-testid="stHeading"] *,
[data-testid="stHeadingWithActionElements"] * {
    color: #0f172a !important;
}
/* Teks umum di luar sidebar */
section.main * {
    color: #0f172a;
}
/* Tapi jangan timpa warna sidebar */
[data-testid="stSidebar"] * { color: #cbd5e1 !important; }
/* Dan jangan timpa teks yang sudah punya warna spesifik via inline style */
</style>
""", unsafe_allow_html=True)

APP_DIR = os.path.dirname(os.path.abspath(__file__))
VIEW_DIR = os.path.join(APP_DIR, "view")
if VIEW_DIR not in sys.path: sys.path.insert(0, VIEW_DIR)
if APP_DIR not in sys.path: sys.path.insert(0, APP_DIR)

# Sidebar
st.sidebar.markdown("""
<div style='padding: 1.8rem 1rem 1.2rem 1rem; text-align:center;'>
    <div style='width:56px; height:56px; background:#1e3a8a; border-radius:16px;
                display:flex; align-items:center; justify-content:center;
                margin:0 auto 0.8rem auto;'>
        <span style='color:white; font-size:1.4rem; font-weight:800;'>BMI</span>
    </div>
    <div style='font-size:1.05rem; font-weight:700; color:#f1f5f9;'>BMI Analysis</div>
    <div style='font-size:0.72rem; color:#475569; margin-top:0.2rem; letter-spacing:0.05em;
                text-transform:uppercase;'>Data Mining Project</div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<div style='border-top:1px solid #1e293b; margin:0 1rem;'></div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)

pages = {
    "Home": "home",
    "Dataset Overview": "dataset_overview",
    "Prediction": "prediction",
    "Visualization": "visualization",
    "About": "about"
}

if "page" not in st.session_state:
    st.session_state.page = "home"

for label, key in pages.items():
    if st.sidebar.button(label, use_container_width=True,
                         type="primary" if st.session_state.page == key else "secondary"):
        st.session_state.page = key

st.sidebar.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='border-top:1px solid #1e293b; margin:0 1rem;'></div>", unsafe_allow_html=True)
st.sidebar.markdown("""
<div style='text-align:center; padding:0.8rem 0; color:#334155; font-size:0.72rem; letter-spacing:0.04em;'>
    Data Mining - UAS
</div>
""", unsafe_allow_html=True)

page = st.session_state.page
page_file = os.path.join(VIEW_DIR, f"{page}.py")
with open(page_file, encoding="utf-8") as f:
    code = f.read()
exec(compile(code, page_file, "exec"), {"__file__": page_file, "__name__": "__main__"})