import streamlit as st

st.set_page_config(
    page_title="Aditya Analytics Consulting",
    page_icon="📊",
    layout="wide",
)

CSS = """
<style>
:root{
  --bg:#0b1220;
  --panel:#0f1b33;
  --panel2:#0c162d;
  --text:#e8eefc;
  --muted:#b6c3e6;
  --line:rgba(255,255,255,.12);
  --shadow: 0 12px 35px rgba(0,0,0,.35);
  --radius: 18px;
}
html, body, [data-testid="stAppViewContainer"]{
  background: radial-gradient(1200px 650px at 18% 10%, rgba(122,167,255,.18), transparent 60%),
              radial-gradient(950px 550px at 82% 20%, rgba(110,242,214,.14), transparent 55%),
              radial-gradient(1000px 750px at 50% 92%, rgba(122,167,255,.10), transparent 60%),
              var(--bg) !important;
  color: var(--text) !important;
}
.block-container{padding-top: 1.25rem;}
.card{
  border: 1px solid var(--line);
  border-radius: 22px;
  background: rgba(15,27,51,.55);
  padding: 18px;
  box-shadow: var(--shadow);
}
.hero{
  border: 1px solid var(--line);
  border-radius: 26px;
  background: linear-gradient(180deg, rgba(15,27,51,.88), rgba(12,22,45,.88));
  padding: 26px;
  box-shadow: var(--shadow);
}
.badge{
  display:inline-block;
  padding: 7px 10px;
  border-radius: 999px;
  border:1px solid rgba(122,167,255,.35);
  background: rgba(122,167,255,.08);
  color: var(--muted);
  font-size: 12px;
  margin-bottom: 12px;
}
.muted{color: var(--muted);}
.small{font-size: 13px;}
hr{border-color: rgba(255,255,255,.10);}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# Header
st.markdown(
    """
<div class="hero">
  <div class="badge">✅ Turning Data into Decisions</div>
  <h1 style="margin:0; font-size:38px; line-height:1.1;">Aditya Analytics Consulting</h1>
  <p class="muted" style="margin-top:10px; font-size:15px; max-width:72ch;">
    We help businesses unify messy data, build executive-ready KPI dashboards, and apply forecasting + AI
    so leaders can make faster, smarter decisions with confidence.
  </p>
</div>
""",
    unsafe_allow_html=True,
)

tabs = st.tabs(["Home", "Services", "Pricing", "About", "Contact"])

with tabs[0]:
    c1, c2, c3 = st.columns(3)
    for col, title, desc in [
        (c1, "📊 Dashboards", "Executive KPI dashboards with drill-downs for fast decisions."),
        (c2, "🔮 Forecasting", "Revenue/demand/churn forecasts with scenarios and confidence."),
        (c3, "⚙️ Automation", "Automated reports + alerts to eliminate manual reporting."),
    ]:
        with col:
            st.markdown(f"""
<div class="card">
  <h3 style="margin:0;">{title}</h3>
  <p class="muted small" style="margin:8px 0 0;">{desc}</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown("""
<div class="card">
  <h3 style="margin:0;">How we work</h3>
  <p class="muted small" style="margin-top:8px;">
    1) Discover → 2) Build → 3) Deliver → 4) Scale (automation + continuous improvement)
  </p>
</div>
""", unsafe_allow_html=True)

with tabs[1]:
    st.subheader("Services")
    services = [
        ("🧭 Data Strategy & Analytics Roadmap", ["Data audit", "KPI framework", "30–90 day roadmap"]),
        ("🧱 Data Engineering & Integration", ["Cleanup & transformation", "SQL data layer", "Automated refresh"]),
        ("📈 BI & Dashboards", ["Executive dashboards", "Operational dashboards", "Reporting packs"]),
        ("🔎 Diagnostic Analytics", ["Root-cause analysis", "Cohort/funnel analysis", "Segmentation"]),
        ("🔮 Predictive Analytics", ["Forecasting", "Churn/risk prediction", "Scenario modeling"]),
        ("🧠 Decision Support", ["What-if analysis", "Optimization", "Recommendations"]),
        ("🤖 AI/ML Solutions", ["NLP insights", "Anomaly detection", "Model monitoring"]),
        ("⚙️ Automation & Alerts", ["Scheduled reporting", "Threshold alerts", "Exception monitoring"]),
        ("🎓 Training & Enablement", ["Power BI/SQL training", "Data literacy", "Executive KPI coaching"]),
    ]
    cols = st.columns(3)
    for i, (name, bullets) in enumerate(services):
        with cols[i % 3]:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown(f"**{name}**")
            st.write("\n".join([f"- {b}" for b in bullets]))
            st.markdown("</div>", unsafe_allow_html=True)

with tabs[2]:
    st.subheader("Pricing (Outcome-Based)")
    p1, p2, p3, p4 = st.columns(4)

    def price_card(col, title, price, points, highlight=False):
        bg = "linear-gradient(180deg, rgba(122,167,255,.15), rgba(15,27,51,.55))" if highlight else "rgba(15,27,51,.55)"
        border = "rgba(122,167,255,.55)" if highlight else "var(--line)"
        with col:
            st.markdown(f"""
<div class="card" style="background:{bg}; border-color:{border};">
  <h3 style="margin:0;">{title}</h3>
  <div style="font-size:26px; font-weight:700; margin-top:6px;">{price}</div>
  <div class="muted small" style="margin-top:10px;">
    {"<br/>".join([f"• {p}" for p in points])}
  </div>
</div>
""", unsafe_allow_html=True)

    price_card(p1, "Analytics Kickstart", "₹30k – ₹50k",
               ["Data audit + KPI framework", "1 core dashboard", "Quick-win recommendations"])
    price_card(p2, "Growth Intelligence", "₹75k – ₹1.5L",
               ["Data cleanup/integration", "Multiple dashboards", "Forecasting + segmentation"], highlight=True)
    price_card(p3, "Decision Intelligence", "₹2L+",
               ["Predictive + prescriptive models", "What-if simulations", "Decision dashboards"])
    price_card(p4, "AI Solutions", "Custom",
               ["AI use-case assessment", "Build + deploy", "Monitoring + automation"])

    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown("""
<div class="card">
  <h3 style="margin:0;">Monthly Retainers</h3>
  <p class="muted small" style="margin-top:8px;">
    Essential: ₹25k/month • Growth: ₹50k/month • Strategic: ₹1L+/month
  </p>
</div>
""", unsafe_allow_html=True)

with tabs[3]:
    st.subheader("About")
    st.markdown("""
<div class="card">
  <p class="muted small">
    Aditya Analytics Consulting is a boutique analytics studio focused on measurable outcomes:
    better visibility, faster reporting, smarter forecasting, and decision-ready insights.
  </p>
  <hr/>
  <p class="muted small"><b>Principles:</b> Clarity • Trust (clean data + documented logic) • Action • Speed</p>
</div>
""", unsafe_allow_html=True)

with tabs[4]:
    st.subheader("Contact")
    st.markdown("""
<div class="card">
  <h3 style="margin:0;">Book a Free Analytics Diagnostic</h3>
  <p class="muted small" style="margin-top:8px;">
    Share your current reporting/data setup. We’ll suggest quick wins + a clear next-step roadmap.
  </p>
</div>
""", unsafe_allow_html=True)
    st.write("")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        company = st.text_input("Company")
        message = st.text_area("What do you want to improve? (Dashboards / forecasting / automation)")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Thanks! Your request is recorded (wire this to email/CRM in production).")