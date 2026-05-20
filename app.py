import streamlit as st
import base64
from pathlib import Path

# ---------- Logo resolution (robust to working directory) ----------
APP_DIR = Path(__file__).parent.resolve()

def _find_asset(filename: str) -> Path | None:
    """Look for an asset in common locations near app.py."""
    candidates = [
        APP_DIR / "assets" / filename,
        APP_DIR / filename,
        Path.cwd() / "assets" / filename,
        Path.cwd() / filename,
    ]
    for p in candidates:
        if p.is_file():
            return p
    return None

LOGO_PATH = _find_asset("aditya_analytics_logo.png")
ICON_PATH = _find_asset("aditya_icon.png")

def get_base64_image(image_path: Path | None) -> str:
    if not image_path or not image_path.is_file():
        return ""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except (FileNotFoundError, OSError):
        return ""

LOGO_B64 = get_base64_image(LOGO_PATH)
ICON_B64 = get_base64_image(ICON_PATH)
LOGO_SRC = f"data:image/png;base64,{LOGO_B64}" if LOGO_B64 else ""
# Fallback: use full logo if icon-only is missing
ICON_SRC = f"data:image/png;base64,{ICON_B64}" if ICON_B64 else LOGO_SRC

# ---------- Page Config ----------
st.set_page_config(
    page_title="Aditya Analytics Consulting",
    page_icon=str(ICON_PATH) if ICON_PATH else (str(LOGO_PATH) if LOGO_PATH else "📊"),
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Global Styling ----------
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700;9..144,800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

:root{
  /* Brand palette derived from the logo */
  --navy-900:#0a1e4a;
  --navy-800:#102a5e;
  --navy-700:#1e3a8a;
  --navy-600:#2546a3;
  --orange-500:#f97316;
  --orange-400:#fb923c;
  --orange-300:#fdba74;

  /* Surfaces */
  --bg:#f7f8fc;
  --surface:#ffffff;
  --surface-2:#f1f4fb;
  --ink:#0f1f44;
  --ink-soft:#3b4a73;
  --muted:#6b7799;
  --line:rgba(15,31,68,.08);
  --line-strong:rgba(15,31,68,.14);

  --radius-sm:12px;
  --radius:18px;
  --radius-lg:26px;

  --shadow-sm:0 1px 2px rgba(15,31,68,.06), 0 1px 3px rgba(15,31,68,.05);
  --shadow:0 10px 30px rgba(15,31,68,.08), 0 2px 6px rgba(15,31,68,.04);
  --shadow-lg:0 24px 60px rgba(15,31,68,.14), 0 6px 14px rgba(15,31,68,.06);

  --grad-brand: linear-gradient(135deg, var(--navy-700) 0%, var(--navy-900) 60%, #061235 100%);
  --grad-accent: linear-gradient(135deg, var(--orange-500), #ef4f0c);
}

/* Base */
html, body, [data-testid="stAppViewContainer"]{
  background:
    radial-gradient(900px 500px at 8% -5%, rgba(30,58,138,.08), transparent 60%),
    radial-gradient(700px 400px at 95% 0%, rgba(249,115,22,.08), transparent 55%),
    var(--bg) !important;
  color: var(--ink) !important;
  font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif !important;
}

/* Tighten default Streamlit chrome */
[data-testid="stHeader"]{ background: transparent; }
.block-container{ padding-top: 1.2rem; padding-bottom: 4rem; max-width: 1180px; }
#MainMenu, footer{ visibility: hidden; }

/* Typography */
h1, h2, h3, h4 {
  font-family: 'Fraunces', Georgia, serif !important;
  color: var(--ink) !important;
  letter-spacing: -0.02em;
  font-weight: 600 !important;
}
p, li, span, label { color: var(--ink-soft); }
.muted { color: var(--muted) !important; }
.small { font-size: 13px; }
.eyebrow{
  display:inline-flex; align-items:center; gap:8px;
  font-family:'Plus Jakarta Sans', sans-serif;
  font-size:11px; font-weight:700; letter-spacing:.18em; text-transform:uppercase;
  color: var(--orange-500);
}
.eyebrow::before{
  content:""; width:24px; height:2px; background: var(--orange-500); border-radius:2px;
}

/* ============ Sidebar ============ */
[data-testid="stSidebar"]{
  background: var(--grad-brand) !important;
  border-right: 1px solid rgba(255,255,255,.06);
}
[data-testid="stSidebar"] *{ color:#e8eefc !important; }
[data-testid="stSidebar"] .sidebar-logo{
  display:flex; align-items:center; gap: 12px;
  padding: 4px 4px 18px;
  margin-bottom: 14px;
  border-bottom: 1px solid rgba(255,255,255,.08);
}
[data-testid="stSidebar"] .sidebar-logo img{
  width: 44px; height: 44px; display:block;
  filter: drop-shadow(0 4px 12px rgba(0,0,0,.25));
}
[data-testid="stSidebar"] .sidebar-logo .brand-text{
  display:flex; flex-direction:column; line-height:1.15;
}
[data-testid="stSidebar"] .sidebar-logo .brand-text .brand-name{
  font-family: 'Fraunces', serif; font-weight: 600; font-size: 17px;
  color: #ffffff !important; letter-spacing: -0.01em;
}
[data-testid="stSidebar"] .sidebar-logo .brand-text .brand-sub{
  font-size: 9.5px; letter-spacing: .22em; text-transform: uppercase;
  color: var(--orange-400) !important; font-weight: 600; margin-top: 2px;
}
.sidebar-divider{
  height:1px; background: rgba(255,255,255,.10);
  margin: 6px 0 14px;
}
.sidebar-nav-title{
  font-size:11px; letter-spacing:.18em; text-transform:uppercase;
  color: rgba(232,238,252,.55) !important; margin: 10px 4px 8px;
}
.sidebar-cta{
  margin-top: 22px; padding: 16px;
  background: linear-gradient(135deg, rgba(249,115,22,.18), rgba(249,115,22,.05));
  border: 1px solid rgba(249,115,22,.35);
  border-radius: var(--radius);
}
.sidebar-cta h4{ color:#fff !important; font-size:15px; margin:0 0 6px; font-family:'Fraunces',serif !important; }
.sidebar-cta p{ color: rgba(232,238,252,.75) !important; font-size:12px; margin:0; }

/* ============ Top brand header (sticky, full-width) ============ */
/* Push Streamlit's default top padding down so our header sits at the very top */
[data-testid="stAppViewContainer"] > .main .block-container{
  padding-top: 0.5rem;
}
.top-header{
  position: sticky;
  top: 0;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  padding: 12px 20px;
  margin: 0 0 22px;
  background: rgba(255,255,255,0.85);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid var(--line);
  border-radius: 16px;
  box-shadow: 0 4px 18px rgba(15,31,68,.06);
}
.top-header .brand-logo{
  display:flex; align-items:center; gap: 12px;
}
.top-header .brand-logo img{
  height: 44px; width: auto; display:block;
}
.top-header .brand-meta{
  display:flex; align-items:center; gap: 18px;
  font-size: 12.5px; color: var(--muted); letter-spacing:.02em;
}
.top-header .brand-meta .status{
  display:inline-flex; align-items:center; gap: 8px;
  padding: 6px 12px; border-radius: 999px;
  background: rgba(34,197,94,.08);
  color: #15803d;
  font-weight: 600;
  border: 1px solid rgba(34,197,94,.22);
}
.top-header .brand-meta .status .dot{
  width:7px; height:7px; border-radius:50%;
  background: #22c55e;
  box-shadow: 0 0 0 4px rgba(34,197,94,.18);
  animation: pulseDot 2.2s ease-in-out infinite;
}
@keyframes pulseDot{
  0%, 100%{ box-shadow: 0 0 0 4px rgba(34,197,94,.18); }
  50%{ box-shadow: 0 0 0 7px rgba(34,197,94,.06); }
}
.top-header .header-cta{
  display:inline-flex; align-items:center; gap: 6px;
  padding: 9px 18px;
  border-radius: 999px;
  background: var(--grad-accent);
  color: #fff !important;
  font-weight: 600;
  font-size: 13px;
  text-decoration: none;
  box-shadow: 0 6px 18px rgba(249,115,22,.30);
  transition: transform .2s ease, box-shadow .2s ease;
}
.top-header .header-cta:hover{
  transform: translateY(-1px);
  box-shadow: 0 10px 22px rgba(249,115,22,.40);
}
@media (max-width: 720px){
  .top-header{ padding: 10px 14px; flex-wrap: wrap; }
  .top-header .brand-logo img{ height: 36px; }
  .top-header .brand-meta{ gap: 10px; font-size: 11.5px; }
  .top-header .brand-meta .status span:last-child{ display:none; }
  .top-header .header-cta{ padding: 8px 14px; font-size: 12px; }
}

/* ============ Hero ============ */
.hero{
  position: relative;
  border-radius: var(--radius-lg);
  background: var(--grad-brand);
  padding: 44px 48px;
  overflow: hidden;
  box-shadow: var(--shadow-lg);
  margin-bottom: 28px;
}
.hero::before{
  content:""; position:absolute; inset:0;
  background:
    radial-gradient(600px 300px at 85% 20%, rgba(249,115,22,.22), transparent 60%),
    radial-gradient(500px 280px at 10% 100%, rgba(37,70,163,.40), transparent 60%);
  pointer-events:none;
}
.hero::after{
  content:""; position:absolute; right:-80px; top:-80px;
  width: 320px; height: 320px; border-radius:50%;
  background: radial-gradient(circle, rgba(249,115,22,.18), transparent 70%);
  filter: blur(20px); pointer-events:none;
}
.hero-inner{ position: relative; z-index: 2; }
.hero-grid{
  display:grid; grid-template-columns: 1.4fr 1fr; gap: 32px; align-items:center;
}
@media (max-width: 900px){
  .hero{ padding: 32px 26px; }
  .hero-grid{ grid-template-columns: 1fr; }
}
.hero h1{
  color:#ffffff !important;
  font-size: clamp(34px, 4.2vw, 54px);
  line-height: 1.04;
  margin: 14px 0 16px;
  font-weight: 600 !important;
}
.hero h1 .accent{
  background: linear-gradient(135deg, var(--orange-400), var(--orange-500));
  -webkit-background-clip: text; background-clip: text; color: transparent;
  font-style: italic;
  font-weight: 500 !important;
}
.hero p.lede{
  color: rgba(232,238,252,.82); font-size: 16px; line-height:1.65; max-width: 56ch;
  margin: 0 0 22px;
}
.hero .eyebrow{ color: var(--orange-400); }
.hero .eyebrow::before{ background: var(--orange-400); }
.hero-actions{ display:flex; gap:12px; flex-wrap:wrap; }
.btn{
  display:inline-flex; align-items:center; gap:8px;
  padding: 12px 22px; border-radius: 999px;
  font-weight:600; font-size: 14px; text-decoration:none;
  transition: transform .2s ease, box-shadow .2s ease;
}
.btn-primary{
  background: var(--grad-accent); color:#fff !important;
  box-shadow: 0 8px 24px rgba(249,115,22,.35);
}
.btn-primary:hover{ transform: translateY(-2px); box-shadow: 0 12px 28px rgba(249,115,22,.45); }
.btn-ghost{
  background: rgba(255,255,255,.06); color:#fff !important;
  border:1px solid rgba(255,255,255,.18);
}
.btn-ghost:hover{ background: rgba(255,255,255,.12); }

/* Hero stats card */
.hero-stats{
  background: rgba(255,255,255,.06);
  border: 1px solid rgba(255,255,255,.12);
  border-radius: var(--radius);
  padding: 22px;
  backdrop-filter: blur(8px);
}
.hero-stat{ padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,.08); }
.hero-stat:last-child{ border-bottom: none; }
.hero-stat .num{
  font-family:'Fraunces',serif; font-size: 30px; font-weight: 600;
  color:#fff; line-height:1; display:block;
}
.hero-stat .num .unit{ color: var(--orange-400); font-style: italic; }
.hero-stat .lbl{
  color: rgba(232,238,252,.65); font-size: 12px; margin-top:6px; display:block;
  letter-spacing:.04em;
}

/* ============ Cards ============ */
.card{
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 24px;
  box-shadow: var(--shadow-sm);
  transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
  height: 100%;
}
.card:hover{
  transform: translateY(-3px);
  box-shadow: var(--shadow);
  border-color: var(--line-strong);
}
.card h3{ font-size: 19px; margin: 0 0 8px; }
.card p{ font-size: 14px; line-height: 1.6; margin: 0; }

.card-icon{
  width:46px; height:46px; border-radius: 12px;
  display:inline-flex; align-items:center; justify-content:center;
  font-size: 22px; margin-bottom: 14px;
  background: linear-gradient(135deg, rgba(30,58,138,.08), rgba(249,115,22,.08));
  border: 1px solid var(--line);
}

/* Service card */
.svc{
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 22px;
  box-shadow: var(--shadow-sm);
  height: 100%;
  transition: all .25s ease;
  position: relative; overflow:hidden;
}
.svc::before{
  content:""; position:absolute; left:0; top:0; bottom:0; width:3px;
  background: var(--grad-accent); opacity:0; transition: opacity .25s ease;
}
.svc:hover{ transform: translateY(-3px); box-shadow: var(--shadow); }
.svc:hover::before{ opacity:1; }
.svc h4{ font-size:16px; margin:0 0 10px; color: var(--navy-700) !important; }
.svc ul{ margin:0; padding-left: 18px; }
.svc li{ font-size:13.5px; color: var(--ink-soft); margin: 4px 0; line-height:1.55; }

/* ============ Pricing ============ */
.price{
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 26px 22px;
  box-shadow: var(--shadow-sm);
  height: 100%;
  position: relative;
  transition: all .25s ease;
}
.price:hover{ transform: translateY(-3px); box-shadow: var(--shadow); }
.price .tier{ font-size:12px; letter-spacing:.16em; text-transform:uppercase; color: var(--muted); margin-bottom: 10px; }
.price h3{ font-size:20px; margin: 0 0 10px; }
.price .amt{
  font-family:'Fraunces', serif;
  font-size: 26px; font-weight:600; color: var(--navy-700);
  margin: 6px 0 16px; line-height:1.1;
}
.price ul{ list-style:none; padding:0; margin:0; }
.price li{
  display:flex; gap:10px; align-items:flex-start;
  padding: 8px 0; border-top:1px dashed var(--line);
  font-size:13.5px; color: var(--ink-soft);
}
.price li:first-child{ border-top: none; }
.price li::before{
  content:"✓"; color: var(--orange-500); font-weight:700; flex-shrink:0;
}
.price.featured{
  background: linear-gradient(180deg, var(--surface), var(--surface-2));
  border: 1.5px solid var(--navy-700);
  box-shadow: 0 18px 40px rgba(30,58,138,.14);
}
.price.featured .ribbon{
  position:absolute; top:-12px; right:18px;
  background: var(--grad-accent); color:#fff; font-size:10.5px;
  letter-spacing:.14em; text-transform:uppercase; font-weight:700;
  padding: 5px 12px; border-radius: 999px;
  box-shadow: 0 6px 16px rgba(249,115,22,.4);
}

/* ============ About / Process ============ */
.process{
  display:grid; grid-template-columns: repeat(4, 1fr); gap: 14px;
  margin-top: 6px;
}
@media (max-width: 900px){ .process{ grid-template-columns: repeat(2, 1fr); } }
.step{
  background: var(--surface);
  border:1px solid var(--line);
  border-radius: var(--radius);
  padding: 18px;
  position:relative;
}
.step .num{
  font-family:'Fraunces',serif; font-style:italic;
  font-size: 36px; font-weight:600; color: var(--orange-500);
  line-height:1; display:block; margin-bottom: 6px;
}
.step h4{ font-size:15px; margin: 0 0 6px; }
.step p{ font-size: 13px; color: var(--muted); margin:0; line-height:1.55; }

.principle-row{
  display:flex; flex-wrap:wrap; gap:8px; margin-top:14px;
}
.pill{
  padding: 7px 14px; border-radius: 999px;
  background: rgba(30,58,138,.06); color: var(--navy-700);
  font-size: 12.5px; font-weight: 600; border: 1px solid rgba(30,58,138,.12);
}

/* ============ Contact ============ */
.contact-card{
  background: var(--grad-brand);
  color:#fff;
  border-radius: var(--radius-lg);
  padding: 30px;
  box-shadow: var(--shadow);
  position: relative; overflow: hidden;
}
.contact-card::before{
  content:""; position:absolute; right:-60px; bottom:-60px;
  width: 220px; height: 220px; border-radius: 50%;
  background: radial-gradient(circle, rgba(249,115,22,.25), transparent 70%);
}
.contact-card h3{ color:#fff !important; margin: 6px 0 10px; font-size: 24px; position: relative; }
.contact-card p{ color: rgba(232,238,252,.78); position: relative; margin:0; }
.contact-card .eyebrow{ color: var(--orange-400); }
.contact-card .eyebrow::before{ background: var(--orange-400); }

/* Streamlit form inputs */
.stTextInput input, .stTextArea textarea{
  background: var(--surface) !important;
  border: 1px solid var(--line-strong) !important;
  border-radius: 12px !important;
  color: var(--ink) !important;
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  padding: 10px 14px !important;
}
.stTextInput input:focus, .stTextArea textarea:focus{
  border-color: var(--navy-700) !important;
  box-shadow: 0 0 0 3px rgba(30,58,138,.12) !important;
}
.stTextInput label, .stTextArea label{
  color: var(--ink) !important; font-weight: 600 !important; font-size: 13px !important;
}
.stForm [data-testid="stFormSubmitButton"] button{
  background: var(--grad-accent) !important;
  color: #fff !important;
  border: none !important;
  border-radius: 999px !important;
  padding: 10px 28px !important;
  font-weight: 600 !important;
  box-shadow: 0 8px 22px rgba(249,115,22,.32);
  transition: transform .2s ease;
}
.stForm [data-testid="stFormSubmitButton"] button:hover{
  transform: translateY(-2px);
}

/* Tabs styling */
.stTabs [data-baseweb="tab-list"]{
  gap: 4px; background: var(--surface);
  padding: 6px; border-radius: 14px;
  border: 1px solid var(--line);
  box-shadow: var(--shadow-sm);
}
.stTabs [data-baseweb="tab"]{
  background: transparent !important;
  border-radius: 10px !important;
  color: var(--ink-soft) !important;
  font-weight: 600 !important;
  font-size: 14px !important;
  padding: 10px 18px !important;
  border: none !important;
}
.stTabs [aria-selected="true"]{
  background: var(--grad-brand) !important;
  color: #fff !important;
  box-shadow: 0 4px 12px rgba(15,31,68,.18);
}

/* Section heading */
.section-head{ margin: 8px 0 18px; }
.section-head h2{ margin: 6px 0 4px; font-size: 28px; }
.section-head p{ color: var(--muted); margin:0; font-size: 14px; }

/* Footer note */
.footer-note{
  text-align:center; font-size: 12px; color: var(--muted);
  padding: 28px 0 6px; border-top: 1px solid var(--line); margin-top: 32px;
}
.footer-note strong{ color: var(--navy-700); }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# ---------- Sidebar ----------
with st.sidebar:
    if ICON_SRC:
        st.markdown(
            f"""
<div class="sidebar-logo">
  <img src="{ICON_SRC}" alt="Aditya Analytics mark"/>
  <div class="brand-text">
    <span class="brand-name">Aditya</span>
    <span class="brand-sub">Analytics Consulting</span>
  </div>
</div>
""",
            unsafe_allow_html=True,
        )
    else:
        st.markdown("### Aditya Analytics")

    st.markdown('<div class="sidebar-nav-title">Navigation</div>', unsafe_allow_html=True)
    st.markdown(
        """
- **Home** — Overview
- **Services** — What we deliver
- **Pricing** — Transparent tiers
- **About** — Our approach
- **Contact** — Book a session
"""
    )

    st.markdown('<div class="sidebar-nav-title" style="margin-top:22px;">Get in touch</div>', unsafe_allow_html=True)
    st.markdown(
        """
📧 hello@aditya-analytics.com  
🌐 www.aditya-analytics.com  
📍 India · Remote-first
"""
    )

    st.markdown(
        """
<div class="sidebar-cta">
  <h4>Free Diagnostic</h4>
  <p>30-min review of your current reporting setup with quick-win recommendations.</p>
</div>
""",
        unsafe_allow_html=True,
    )

# ---------- Hero ----------
# ---------- Top brand header (sticky, top-left logo) ----------
if LOGO_SRC:
    st.markdown(
        f"""
<div class="top-header">
  <div class="brand-logo">
    <img src="{LOGO_SRC}" alt="Aditya Analytics Consulting"/>
  </div>
  <div class="brand-meta">
    <span class="status"><span class="dot"></span><span>Available · Q2 2026</span></span>
    <a class="header-cta" href="#contact">Book a call →</a>
    <a class="header-cta" href="https://calendly.com/hello-aditya-analytics/30min" target="_blank">Book a call →</a>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

st.markdown(
    f"""
<div class="hero">
  <div class="hero-inner">
    <div class="hero-grid">
      <div>
        <div class="eyebrow">Turning Data into Decisions</div>
        <h1>Analytics that drive <span class="accent">measurable</span> business outcomes.</h1>
        <p class="lede">
          We help leaders unify messy data, build executive-ready KPI dashboards, and apply
          forecasting and AI — so decisions get faster, sharper, and more confident.
        </p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="https://calendly.com/hello-aditya-analytics/30min">Book a free diagnostic →</a>
          <a class="btn btn-ghost" href="#services">Explore services</a>
        </div>
      </div>
      <div class="hero-stats">
        <div class="hero-stat">
          <span class="num">40<span class="unit">%</span></span>
          <span class="lbl">Avg. reporting time saved</span>
        </div>
        <div class="hero-stat">
          <span class="num">3<span class="unit">x</span></span>
          <span class="lbl">Faster executive decisions</span>
        </div>
        <div class="hero-stat">
          <span class="num">100<span class="unit">%</span></span>
          <span class="lbl">Outcome-based pricing</span>
        </div>
      </div>
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ---------- Tabs ----------
tabs = st.tabs(["🏠  Home", "🧰  Services", "💼  Pricing", "ℹ️  About", "✉️  Contact"])

# ===== HOME =====
with tabs[0]:
    st.markdown(
        """
<div class="section-head">
  <div class="eyebrow">What we do</div>
  <h2>Three ways we move the needle</h2>
  <p>From clarity to foresight — covering the full analytics value chain.</p>
</div>
""",
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3, gap="medium")
    cards = [
        (c1, "📊", "Executive Dashboards",
         "KPI dashboards with drill-downs so leaders see what matters — and what to do next."),
        (c2, "🔮", "Forecasting & AI",
         "Revenue, demand and churn forecasts with confidence intervals and what-if scenarios."),
        (c3, "⚙️", "Reporting Automation",
         "Eliminate manual reporting with scheduled refreshes, alerts and exception monitoring."),
    ]
    for col, icon, title, desc in cards:
        with col:
            st.markdown(
                f"""
<div class="card">
  <div class="card-icon">{icon}</div>
  <h3>{title}</h3>
  <p class="muted">{desc}</p>
</div>
""",
                unsafe_allow_html=True,
            )

    st.markdown("<br/>", unsafe_allow_html=True)

    st.markdown(
        """
<div class="section-head">
  <div class="eyebrow">Our process</div>
  <h2>How we work</h2>
  <p>A clear four-step path from problem to scalable solution.</p>
</div>
<div class="process">
  <div class="step">
    <span class="num">01</span>
    <h4>Discover</h4>
    <p>Audit current data, KPIs and reporting gaps. Align on outcomes.</p>
  </div>
  <div class="step">
    <span class="num">02</span>
    <h4>Build</h4>
    <p>Clean, model and visualize. Ship a working dashboard in weeks.</p>
  </div>
  <div class="step">
    <span class="num">03</span>
    <h4>Deliver</h4>
    <p>Train your team. Document logic. Hand off with confidence.</p>
  </div>
  <div class="step">
    <span class="num">04</span>
    <h4>Scale</h4>
    <p>Automate, alert and add forecasting layers as you grow.</p>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

# ===== SERVICES =====
with tabs[1]:
    st.markdown(
        """
<div class="section-head" id="services">
  <div class="eyebrow">Services</div>
  <h2>End-to-end analytics capability</h2>
  <p>Pick a single engagement or combine them into a roadmap.</p>
</div>
""",
        unsafe_allow_html=True,
    )

    services = [
        ("🧭", "Data Strategy & Roadmap",
         ["Data audit & maturity assessment", "KPI framework design", "30–90 day roadmap"]),
        ("🧱", "Data Engineering & Integration",
         ["Cleanup & transformation", "SQL data layer", "Automated refresh pipelines"]),
        ("📈", "BI & Dashboards",
         ["Executive dashboards", "Operational dashboards", "Reporting packs"]),
        ("🔎", "Diagnostic Analytics",
         ["Root-cause analysis", "Cohort & funnel analysis", "Customer segmentation"]),
        ("🔮", "Predictive Analytics",
         ["Revenue & demand forecasting", "Churn & risk prediction", "Scenario modeling"]),
        ("🧠", "Decision Support",
         ["What-if analysis", "Optimization models", "Recommendation engines"]),
        ("🤖", "AI / ML Solutions",
         ["NLP & text insights", "Anomaly detection", "Model monitoring"]),
        ("⚙️", "Automation & Alerts",
         ["Scheduled reporting", "Threshold-based alerts", "Exception monitoring"]),
        ("🎓", "Training & Enablement",
         ["Power BI / SQL training", "Data literacy programs", "Executive KPI coaching"]),
    ]

    rows = [services[i:i + 3] for i in range(0, len(services), 3)]
    for row in rows:
        cols = st.columns(3, gap="medium")
        for col, (icon, name, bullets) in zip(cols, row):
            with col:
                bullets_html = "".join([f"<li>{b}</li>" for b in bullets])
                st.markdown(
                    f"""
<div class="svc">
  <div class="card-icon">{icon}</div>
  <h4>{name}</h4>
  <ul>{bullets_html}</ul>
</div>
""",
                    unsafe_allow_html=True,
                )
        st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

# ===== PRICING =====
with tabs[2]:
    st.markdown(
        """
<div class="section-head">
  <div class="eyebrow">Pricing</div>
  <h2>Outcome-based, transparent tiers</h2>
  <p>Project-based engagements or ongoing retainers — choose what fits.</p>
</div>
""",
        unsafe_allow_html=True,
    )

    p1, p2, p3, p4 = st.columns(4, gap="medium")

    def price_card(col, tier, title, price, points, featured=False):
        klass = "price featured" if featured else "price"
        ribbon = '<span class="ribbon">Most popular</span>' if featured else ""
        items = "".join([f"<li>{p}</li>" for p in points])
        with col:
            st.markdown(
                f"""
<div class="{klass}">
  {ribbon}
  <div class="tier">{tier}</div>
  <h3>{title}</h3>
  <div class="amt">{price}</div>
  <ul>{items}</ul>
</div>
""",
                unsafe_allow_html=True,
            )

    price_card(
        p1, "Starter", "Analytics Kickstart", "₹30k – ₹50k",
        ["Data audit + KPI framework", "One core dashboard", "Quick-win recommendations"],
    )
    price_card(
        p2, "Growth", "Growth Intelligence", "₹75k – ₹1.5L",
        ["Data cleanup & integration", "Multiple dashboards", "Forecasting + segmentation"],
        featured=True,
    )
    price_card(
        p3, "Advanced", "Decision Intelligence", "₹2L+",
        ["Predictive + prescriptive models", "What-if simulations", "Decision dashboards"],
    )
    price_card(
        p4, "Custom", "AI Solutions", "Let’s talk",
        ["AI use-case assessment", "Build, deploy & integrate", "Monitoring + automation"],
    )

    st.markdown("<div style='height:22px'></div>", unsafe_allow_html=True)

    st.markdown(
        """
<div class="card" style="display:flex; align-items:center; justify-content:space-between; gap: 18px; flex-wrap:wrap;">
  <div>
    <div class="eyebrow">Monthly Retainers</div>
    <h3 style="margin:6px 0 4px;">Ongoing partnership, predictable cost</h3>
    <p class="muted small" style="margin:0;">For teams that want continuous improvement, not one-off projects.</p>
  </div>
  <div style="display:flex; gap:10px; flex-wrap:wrap;">
    <span class="pill">Essential · ₹25k/mo</span>
    <span class="pill">Growth · ₹50k/mo</span>
    <span class="pill">Strategic · ₹1L+/mo</span>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

# ===== ABOUT =====
with tabs[3]:
    st.markdown(
        """
<div class="section-head">
  <div class="eyebrow">About</div>
  <h2>A boutique studio focused on outcomes</h2>
  <p>Less reporting theater, more decisions made.</p>
</div>
""",
        unsafe_allow_html=True,
    )

    a1, a2 = st.columns([1.3, 1], gap="large")
    with a1:
        st.markdown(
            """
<div class="card">
  <p style="font-size:15.5px; line-height:1.75; color: var(--ink);">
    Aditya Analytics Consulting is a boutique analytics studio built around a simple belief:
    <strong style="color:var(--navy-700);">good analytics doesn’t end with a dashboard — it ends with a decision.</strong>
    We help leaders unify scattered data, design KPIs that actually matter, and build the
    forecasting + AI muscle to act ahead of the curve.
  </p>
  <p style="font-size:14.5px; line-height:1.7; color: var(--ink-soft); margin-top:14px;">
    Every engagement is anchored to a measurable outcome — faster reporting, clearer visibility,
    higher forecast accuracy, or a specific revenue/cost number you’re trying to move.
  </p>
  <div class="principle-row">
    <span class="pill">Clarity</span>
    <span class="pill">Trust</span>
    <span class="pill">Action</span>
    <span class="pill">Speed</span>
  </div>
</div>
""",
            unsafe_allow_html=True,
        )
    with a2:
        st.markdown(
            """
<div class="card">
  <div class="eyebrow">By the numbers</div>
  <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top:14px;">
    <div>
      <div style="font-family:'Fraunces',serif; font-size:30px; font-weight:600; color:var(--navy-700);">15+</div>
      <div class="muted small">Industries served</div>
    </div>
    <div>
      <div style="font-family:'Fraunces',serif; font-size:30px; font-weight:600; color:var(--orange-500);">40%</div>
      <div class="muted small">Avg. time saved</div>
    </div>
    <div>
      <div style="font-family:'Fraunces',serif; font-size:30px; font-weight:600; color:var(--navy-700);">100+</div>
      <div class="muted small">Dashboards delivered</div>
    </div>
    <div>
      <div style="font-family:'Fraunces',serif; font-size:30px; font-weight:600; color:var(--orange-500);">2 wks</div>
      <div class="muted small">Typical first delivery</div>
    </div>
  </div>
</div>
""",
            unsafe_allow_html=True,
        )

# ===== CONTACT =====
with tabs[4]:
    st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
    st.markdown(
        """
<div class="contact-card">
  <div class="eyebrow">Get started</div>
  <h3>Book a free Analytics Diagnostic</h3>
  <p>Share your current reporting setup — we’ll suggest quick wins and a clear next-step roadmap. No commitment.</p>
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

    f1, f2 = st.columns([1.2, 1], gap="large")
    with f1:
        with st.form("contact_form", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                name = st.text_input("Full name", placeholder="Your name")
            with c2:
                email = st.text_input("Work email", placeholder="you@company.com")
            company = st.text_input("Company", placeholder="Company name")
            message = st.text_area(
                "What would you like to improve?",
                placeholder="Dashboards, forecasting, automation, AI…",
                height=130,
            )
            submitted = st.form_submit_button("Send request →")
            if submitted:
                if not (name and email and message):
                    st.warning("Please fill in your name, email, and a short message.")
                else:
                    st.success(
                        f"Thanks, {name.split()[0] if name else 'there'}! Your request is recorded. "
                        "We’ll get back within 2-3 business working days."
                    )

    with f2:
        st.markdown(
            """
<div class="card">
  <div class="eyebrow">Direct channels</div>
  <h3 style="margin:6px 0 14px; font-size:18px;">Prefer to reach us directly?</h3>
  <p class="small" style="margin:8px 0;"><strong style="color:var(--ink);">📧 Email</strong><br/>
  <a href="mailto:hello@aditya-analytics.com" style="color:var(--navy-700); text-decoration:none;">hello@aditya-analytics.com</a></p>
  <p class="small" style="margin:8px 0;"><strong style="color:var(--ink);">🌐 Website</strong><br/>
  <a href="https://www.aditya-analytics.com" target="_blank" rel="noopener" style="color:var(--navy-700); text-decoration:none;">www.aditya-analytics.com</a></p>
  <p class="small" style="margin:8px 0;"><strong style="color:var(--ink);">📍 Location</strong><br/>
  <span class="muted">India · Remote-first, global delivery</span></p>
  <p class="small" style="margin:8px 0;"><strong style="color:var(--ink);">⏱ Response time</strong><br/>
  <span class="muted">Within 2-3 business working days</span></p>
</div>
""",
            unsafe_allow_html=True,
        )

# ---------- Footer ----------
st.markdown(
    """
<div class="footer-note">
  © 2026 <strong>Aditya Analytics Consulting</strong> · Turning data into decisions.
</div>
""",
    unsafe_allow_html=True,
)
