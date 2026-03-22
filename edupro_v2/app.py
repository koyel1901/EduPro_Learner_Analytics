import streamlit as st
import pandas as pd
import plotly.express as px

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="EduPro Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
#  GLOBAL STYLES
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600;700&display=swap');

:root {
    --cream:      #f8f4ee;
    --cream-dark: #e2d6c5;
    --brown-1:    #8b6f47;
    --brown-2:    #6b5035;
    --navy:       #1c2b4a;
    --navy-mid:   #253560;
    --teal:       #2a7f7f;
    --teal-light: #3da8a8;
    --rose:       #c4614a;
    --gold:       #d4a843;
    --text-dark:  #1e1a15;
    --text-light: #8a7d6e;
    --white:      #ffffff;
}

html, body, .stApp {
    background-color: var(--cream) !important;
    font-family: 'DM Sans', sans-serif;
    color: var(--text-dark);
}

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: linear-gradient(160deg, #1c2b4a 0%, #253560 100%) !important;
    border-right: none !important;
}
[data-testid="stSidebar"] * { color: #d4c9b8 !important; }
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #f0e8da !important;
    font-family: 'DM Serif Display', serif !important;
}
[data-testid="stSidebar"] label {
    color: #c8bfb0 !important;
    font-size: 11px !important;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    font-weight: 600 !important;
}
[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background-color: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 8px !important;
}
[data-testid="stSidebar"] span[data-baseweb="tag"] {
    background-color: #8b6f47 !important;
    color: white !important;
    border-radius: 4px !important;
}
[data-testid="stSidebar"] hr { border-color: rgba(255,255,255,0.12) !important; }

/* ── TABS ── */
div[data-baseweb="tab-list"] {
    background: transparent !important;
    border-bottom: 2px solid var(--cream-dark) !important;
    gap: 0 !important;
}
button[data-baseweb="tab"] {
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    color: var(--text-light) !important;
    padding: 12px 22px !important;
    border-radius: 0 !important;
    background: transparent !important;
    border-bottom: 2px solid transparent !important;
    margin-bottom: -2px !important;
}
button[aria-selected="true"] {
    color: #8b6f47 !important;
    border-bottom: 2px solid #8b6f47 !important;
}

/* ── HEADINGS ── */
h1, h2 { font-family: 'DM Serif Display', serif !important; }
h3      { font-family: 'DM Sans', sans-serif !important; font-weight: 700 !important; }
hr      { border-color: var(--cream-dark) !important; }

/* ── CHART CARD WRAPPER ── */
.stPlotlyChart {
    background: var(--white);
    border-radius: 14px;
    border: 1px solid var(--cream-dark);
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    padding: 4px;
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--cream); }
::-webkit-scrollbar-thumb { background: var(--cream-dark); border-radius: 3px; }

/* ── SIDEBAR STAT MINI-CARDS ── */
.sb-stat {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 10px;
    padding: 12px 14px;
    margin: 6px 0;
    text-align: center;
}
.sb-stat .val {
    font-family: 'DM Serif Display', serif;
    font-size: 1.55rem;
    color: #f0e8da;
    display: block;
}
.sb-stat .lbl {
    font-size: 10px;
    color: #9a8e80;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}

/* ── 5 KPI CARDS ── */
.kpi-row {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 16px;
    margin: 20px 0 4px;
}
.kpi-card {
    background: #ffffff;
    border: 1px solid #e2d6c5;
    border-radius: 18px;
    padding: 22px 20px 18px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.055);
    position: relative;
    overflow: hidden;
    transition: transform 0.2s, box-shadow 0.2s;
}
.kpi-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 28px rgba(0,0,0,0.10);
}
.kpi-card::before {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    border-radius: 18px 18px 0 0;
}
.kpi-card.k1::before { background: linear-gradient(90deg,#1c2b4a,#2a7f7f); }
.kpi-card.k2::before { background: linear-gradient(90deg,#8b6f47,#d4a843); }
.kpi-card.k3::before { background: linear-gradient(90deg,#2a7f7f,#3da8a8); }
.kpi-card.k4::before { background: linear-gradient(90deg,#c4614a,#d4a843); }
.kpi-card.k5::before { background: linear-gradient(90deg,#6b5035,#8b6f47); }
.kpi-icon  { font-size: 22px; margin-bottom: 10px; display: block; line-height: 1; }
.kpi-name  {
    font-size: 10px; font-weight: 700; text-transform: uppercase;
    letter-spacing: 1.2px; color: #8a7d6e; margin-bottom: 8px; display: block;
}
.kpi-value {
    font-family: 'DM Serif Display', serif;
    font-size: 2rem; font-weight: 400; color: #1c2b4a;
    display: block; line-height: 1.15; margin-bottom: 5px;
}
.kpi-desc  { font-size: 11.5px; color: #8a7d6e; line-height: 1.4; display: block; }
.kpi-badge {
    display: inline-block; background: #f4efe6;
    border: 1px solid #e2d6c5; border-radius: 20px;
    padding: 2px 10px; font-size: 11px; font-weight: 600;
    color: #6b5035; margin-top: 8px;
}

/* ── SECTION LABEL ── */
.section-label {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #8b6f47;
    border-left: 3px solid #8b6f47;
    padding-left: 10px;
    margin: 28px 0 4px;
    display: block;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  DATA LOADING
#  Spec fields only:
#    Users       → UserID, UserName, Age, Gender
#    Courses     → CourseID, CourseName, CourseCategory, CourseType, CourseLevel
#    Transactions→ TransactionID, UserID, CourseID, TransactionDate
# ─────────────────────────────────────────────
@st.cache_data
def load_data():
    users   = pd.read_excel("data/users.xlsx", sheet_name="Users")[
                  ["UserID", "UserName", "Age", "Gender"]]
    courses = pd.read_excel("data/users.xlsx", sheet_name="Courses")[
                  ["CourseID", "CourseName", "CourseCategory", "CourseType", "CourseLevel"]]
    txns    = pd.read_excel("data/users.xlsx", sheet_name="Transactions")[
                  ["TransactionID", "UserID", "CourseID", "TransactionDate"]]

    # Step 1 — Data Integration: join Users ↔ Transactions ↔ Courses
    merged = txns.merge(users, on="UserID").merge(courses, on="CourseID")
    merged["TransactionDate"] = pd.to_datetime(merged["TransactionDate"])

    # Step 2 — Age band segmentation per spec
    bins   = [0,  17,    25,     35,     45,    100]
    labels = ["<18", "18–25", "26–35", "36–45", "45+"]
    merged["AgeGroup"] = pd.cut(merged["Age"], bins=bins, labels=labels)

    return users, courses, txns, merged

users, courses, txns, merged = load_data()

# ─────────────────────────────────────────────
#  COLOUR PALETTES
# ─────────────────────────────────────────────
PAL_WARM   = ["#8b6f47","#c4614a","#d4a843","#2a7f7f","#1c2b4a",
              "#a8895a","#7a4f30","#e8b86d","#3da8a8","#4a3520","#253560","#6b8fa8"]
PAL_GENDER = ["#2a7f7f","#c4614a"]
PAL_LEVEL  = ["#2a7f7f","#d4a843","#c4614a"]
PAL_TYPE   = ["#2a7f7f","#d4a843"]

BASE_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor ="rgba(0,0,0,0)",
    font         =dict(family="DM Sans, sans-serif", color="#1e1a15", size=12),
    margin       =dict(l=10, r=10, t=44, b=10),
    legend       =dict(bgcolor="rgba(0,0,0,0)", borderwidth=0),
)

def bar_style(fig):
    fig.update_traces(marker_line_width=0)
    fig.update_xaxes(showgrid=False, linecolor="#e2d6c5", tickfont_size=11)
    fig.update_yaxes(showgrid=True,  gridcolor="#efe8dc", linewidth=0, tickfont_size=11)
    return fig

def pie_style(fig):
    fig.update_traces(textfont_size=12, marker_line_width=2, marker_line_color="white")
    return fig

# ─────────────────────────────────────────────
#  SIDEBAR
#  Spec User Capabilities:
#    • Age group filters
#    • Gender filters
#    • Course category & level selectors
# ─────────────────────────────────────────────
with st.sidebar:
    try:
        c1, c2 = st.columns(2)
        with c1: st.image("assets/unified_mentor.png", use_container_width=True)
        with c2: st.image("assets/toronto.png",        use_container_width=True)
    except:
        pass

    st.markdown("---")
    st.markdown("### 🎓 EduPro Analytics")
    st.markdown("*Learner Intelligence Platform*")
    st.markdown("---")
    st.markdown("#### FILTERS")

    age_opts = sorted(merged["AgeGroup"].dropna().unique().tolist(), key=str)
    sel_age  = st.multiselect("Age Group", age_opts, default=age_opts)

    sel_gen  = st.multiselect(
        "Gender",
        merged["Gender"].unique().tolist(),
        default=merged["Gender"].unique().tolist()
    )

    sel_cat  = st.multiselect(
        "Course Category",
        sorted(merged["CourseCategory"].unique().tolist()),
        default=sorted(merged["CourseCategory"].unique().tolist())
    )

    sel_lvl  = st.multiselect(
        "Course Level",
        merged["CourseLevel"].unique().tolist(),
        default=merged["CourseLevel"].unique().tolist()
    )

    st.markdown("---")

# ─────────────────────────────────────────────
#  APPLY FILTERS
# ─────────────────────────────────────────────
F = merged[
    (merged["AgeGroup"].isin(sel_age))  &
    (merged["Gender"].isin(sel_gen))    &
    (merged["CourseCategory"].isin(sel_cat)) &
    (merged["CourseLevel"].isin(sel_lvl))
].copy()

n_enroll = F.shape[0]
n_users  = F["UserID"].nunique()

with st.sidebar:
    st.markdown(f"""
    <div class="sb-stat">
        <span class="val">{n_users:,}</span>
        <span class="lbl">Active Learners</span>
    </div>
    <div class="sb-stat">
        <span class="val">{n_enroll:,}</span>
        <span class="lbl">Total Enrollments</span>
    </div>
    <div class="sb-stat">
        <span class="val">{F["CourseCategory"].nunique()}</span>
        <span class="lbl">Categories</span>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  HEADER BANNER
# ─────────────────────────────────────────────
st.markdown("""
<div style="
    background: linear-gradient(135deg,#1c2b4a 0%,#253560 55%,#2a7f7f 100%);
    border-radius: 20px; padding: 36px 42px;
    position: relative; overflow: hidden;
">
    <div style="position:absolute;top:-40px;right:-40px;width:200px;height:200px;
                background:rgba(255,255,255,0.04);border-radius:50%;"></div>
    <div style="position:absolute;bottom:-60px;right:100px;width:260px;height:260px;
                background:rgba(255,255,255,0.03);border-radius:50%;"></div>
    <p style="color:#9ab8cc;margin:0 0 6px;font-size:11px;letter-spacing:2.5px;
              text-transform:uppercase;font-weight:700;">
        Unified Mentor &nbsp;×&nbsp; Toronto Government Parks, Forestry &amp; Recreation
    </p>
    <h1 style="color:#f0e8da;margin:0 0 8px;font-family:'DM Serif Display',serif;
               font-size:2.1rem;line-height:1.2;">
        EduPro Learner Analytics Dashboard
    </h1>
    <p style="color:#8bafc4;margin:0;font-size:14px;">
        Learner Demographics &amp; Course Enrollment Behaviour Intelligence &nbsp;·&nbsp; 2025
    </p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  5 KPI CARDS — exact project specification
# ─────────────────────────────────────────────

# KPI 1 · Total Enrollments
kpi1_val = f"{n_enroll:,}"
kpi1_sub = f"{n_users:,} unique learners"

# KPI 2 · Enrollments by Age Group
age_vc   = F["AgeGroup"].value_counts().sort_values(ascending=False)
k2_grp   = str(age_vc.index[0]) if len(age_vc) else "—"
k2_cnt   = int(age_vc.iloc[0])  if len(age_vc) else 0
k2_pct   = round(k2_cnt / n_enroll * 100, 1) if n_enroll > 0 else 0
kpi2_val = k2_grp
kpi2_sub = f"Top group · {k2_cnt:,} ({k2_pct}%)"

# KPI 3 · Gender Participation Ratio
gc          = F["Gender"].value_counts()
f_pct       = round(gc.get("Female", 0) / n_enroll * 100, 1) if n_enroll > 0 else 0
m_pct       = round(gc.get("Male",   0) / n_enroll * 100, 1) if n_enroll > 0 else 0
kpi3_val    = f"{f_pct}% F"
kpi3_sub    = f"Female {f_pct}%  ·  Male {m_pct}%"

# KPI 4 · Category Popularity Index
cat_vc   = F["CourseCategory"].value_counts()
k4_cat   = cat_vc.index[0]      if len(cat_vc) else "—"
k4_n     = int(cat_vc.iloc[0])  if len(cat_vc) else 0
k4_pct   = round(k4_n / n_enroll * 100, 1) if n_enroll > 0 else 0
kpi4_val = k4_cat
kpi4_sub = f"Top category · {k4_n:,} ({k4_pct}%)"

# KPI 5 · Level Preference Distribution
lvl_vc   = F["CourseLevel"].value_counts()
k5_lvl   = lvl_vc.index[0]      if len(lvl_vc) else "—"
k5_n     = int(lvl_vc.iloc[0])  if len(lvl_vc) else 0
k5_pct   = round(k5_n / n_enroll * 100, 1) if n_enroll > 0 else 0
kpi5_val = k5_lvl
kpi5_sub = f"Most preferred · {k5_n:,} ({k5_pct}%)"

st.markdown(f"""
<div class="kpi-row">
  <div class="kpi-card k1">
    <span class="kpi-icon">📊</span>
    <span class="kpi-name">Total Enrollments</span>
    <span class="kpi-value">{kpi1_val}</span>
    <span class="kpi-desc">Platform engagement indicator</span>
    <span class="kpi-badge">{kpi1_sub}</span>
  </div>
  <div class="kpi-card k2">
    <span class="kpi-icon">👥</span>
    <span class="kpi-name">Enrollments by Age Group</span>
    <span class="kpi-value">{kpi2_val}</span>
    <span class="kpi-desc">Demographic reach</span>
    <span class="kpi-badge">{kpi2_sub}</span>
  </div>
  <div class="kpi-card k3">
    <span class="kpi-icon">⚖️</span>
    <span class="kpi-name">Gender Participation Ratio</span>
    <span class="kpi-value" style="font-size:1.6rem;">{kpi3_val}</span>
    <span class="kpi-desc">Inclusivity metric</span>
    <span class="kpi-badge">{kpi3_sub}</span>
  </div>
  <div class="kpi-card k4">
    <span class="kpi-icon">🏆</span>
    <span class="kpi-name">Category Popularity Index</span>
    <span class="kpi-value" style="font-size:1.25rem;line-height:1.3;">{kpi4_val}</span>
    <span class="kpi-desc">Course demand</span>
    <span class="kpi-badge">{kpi4_sub}</span>
  </div>
  <div class="kpi-card k5">
    <span class="kpi-icon">🎯</span>
    <span class="kpi-name">Level Preference Distribution</span>
    <span class="kpi-value">{kpi5_val}</span>
    <span class="kpi-desc">Skill maturity insight</span>
    <span class="kpi-badge">{kpi5_sub}</span>
  </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ─────────────────────────────────────────────
#  TABS — mapped to all 4 Core Modules from spec
# ─────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "👥  Demographic Overview",
    "📊  Age-wise Enrollment",
    "♀♂  Gender & Course Preference",
    "📚  Category & Level Analysis",
])

# ══════════════════════════════════════════════════════
#  TAB 1 ── LEARNER DEMOGRAPHIC OVERVIEW
#
#  Spec Methodology: Learner Demographic Analysis
#    ✔ Segment learners into age bands (<18,18–25,26–35,36–45,45+)
#    ✔ Analyze gender distribution across the platform
#    ✔ Measure participation levels per demographic group
# ══════════════════════════════════════════════════════
with tab1:
    st.markdown("### Learner Demographic Overview")
    st.markdown(
        "*Segment learners into age bands · analyze gender distribution "
        "· measure participation levels per demographic group*"
    )

    # ── Age band segmentation
    st.markdown('<span class="section-label">Age Band Segmentation</span>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)

    with c1:
        # Unique learners per age band
        lrn_age = (F.drop_duplicates("UserID")
                    .groupby("AgeGroup", observed=True)
                    .size()
                    .reset_index(name="Learners"))
        fig = px.bar(
            lrn_age, x="AgeGroup", y="Learners",
            color="AgeGroup", color_discrete_sequence=PAL_WARM, text="Learners",
            title="Unique Learners per Age Band"
        )
        fig.update_traces(textposition="outside", textfont_size=11)
        fig.update_layout(**BASE_LAYOUT, showlegend=False)
        bar_style(fig)
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        # Age distribution histogram — spread of individual ages
        age_hist = F.drop_duplicates("UserID")[["Age", "Gender"]]
        fig = px.histogram(
            age_hist, x="Age", color="Gender",
            nbins=22, barmode="overlay", opacity=0.82,
            color_discrete_sequence=PAL_GENDER,
            title="Age Distribution of All Learners"
        )
        fig.update_layout(**BASE_LAYOUT, bargap=0.04)
        bar_style(fig)
        st.plotly_chart(fig, use_container_width=True)

    # ── Gender distribution
    st.markdown('<span class="section-label">Gender Distribution</span>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)

    with c1:
        gc_plot = F["Gender"].value_counts().reset_index()
        gc_plot.columns = ["Gender", "Count"]
        fig = px.pie(
            gc_plot, names="Gender", values="Count",
            color_discrete_sequence=PAL_GENDER, hole=0.55,
            title="Gender Participation Ratio"
        )
        fig.update_layout(**BASE_LAYOUT)
        pie_style(fig)
        dom = F["Gender"].value_counts()
        fig.add_annotation(
            text=f"<b>{dom.iloc[0]/n_enroll*100:.0f}%</b><br>{dom.index[0]}",
            x=0.5, y=0.5, showarrow=False, font_size=14, font_color="#1c2b4a"
        )
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        # Participation levels per demographic group — gender × age group
        part = F.groupby(["AgeGroup", "Gender"], observed=True).size().reset_index(name="Enrollments")
        fig = px.bar(
            part, x="AgeGroup", y="Enrollments", color="Gender",
            barmode="group", color_discrete_sequence=PAL_GENDER, text_auto=True,
            title="Participation Levels: Age Group × Gender"
        )
        fig.update_traces(textposition="outside", textfont_size=10)
        fig.update_layout(**BASE_LAYOUT)
        bar_style(fig)
        st.plotly_chart(fig, use_container_width=True)


# ══════════════════════════════════════════════════════
#  TAB 2 ── AGE-WISE ENROLLMENT CHARTS
#
#  Spec Methodology: Enrollment Distribution Analysis
#    ✔ Count enrollments by CourseCategory
#    ✔ Count enrollments by CourseType
#    ✔ Count enrollments by CourseLevel
#    ✔ Identify most and least popular categories
#
#  Spec Methodology: Behavioral Insights
#    ✔ Average courses taken per learner
#    ✔ Enrollment concentration among active users
# ══════════════════════════════════════════════════════
with tab2:
    st.markdown("### Age-wise Enrollment Charts")
    st.markdown(
        "*Enrollment distribution by CourseCategory, CourseType, CourseLevel · "
        "most & least popular categories · behavioral insights*"
    )

    # ── Enrollment count by age group
    st.markdown('<span class="section-label">Enrollment Distribution by Age Group</span>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)

    with c1:
        enrol_age = F["AgeGroup"].value_counts().reset_index()
        enrol_age.columns = ["AgeGroup", "Enrollments"]
        fig = px.bar(
            enrol_age, x="AgeGroup", y="Enrollments",
            color="AgeGroup", color_discrete_sequence=PAL_WARM, text="Enrollments",
            title="Total Enrollments per Age Group"
        )
        fig.update_traces(textposition="outside", textfont_size=10)
        fig.update_layout(**BASE_LAYOUT, showlegend=False)
        bar_style(fig)
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        enrol_pct = F["AgeGroup"].value_counts(normalize=True).mul(100).round(1).reset_index()
        enrol_pct.columns = ["AgeGroup", "Share (%)"]
        fig = px.pie(
            enrol_pct, names="AgeGroup", values="Share (%)",
            color_discrete_sequence=PAL_WARM, hole=0.45,
            title="Enrollment Share by Age Group (%)"
        )
        fig.update_layout(**BASE_LAYOUT)
        pie_style(fig)
        st.plotly_chart(fig, use_container_width=True)

    # ── Count enrollments by CourseType (spec requirement)
    st.markdown('<span class="section-label">Enrollment Count by CourseType</span>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)

    with c1:
        ct = F["CourseType"].value_counts().reset_index()
        ct.columns = ["CourseType", "Enrollments"]
        fig = px.pie(
            ct, names="CourseType", values="Enrollments",
            color_discrete_sequence=PAL_TYPE, hole=0.52,
            title="Free vs Paid Enrollment Split"
        )
        fig.update_layout(**BASE_LAYOUT)
        pie_style(fig)
        dom_type = F["CourseType"].value_counts()
        fig.add_annotation(
            text=f"<b>{dom_type.iloc[0]/n_enroll*100:.0f}%</b><br>{dom_type.index[0]}",
            x=0.5, y=0.5, showarrow=False, font_size=14, font_color="#1c2b4a"
        )
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        # CourseType by age group
        ct_age = F.groupby(["AgeGroup", "CourseType"], observed=True).size().reset_index(name="Enrollments")
        fig = px.bar(
            ct_age, x="AgeGroup", y="Enrollments", color="CourseType",
            barmode="group", color_discrete_sequence=PAL_TYPE, text_auto=True,
            title="Free vs Paid Enrollment by Age Group"
        )
        fig.update_traces(textposition="outside", textfont_size=9)
        fig.update_layout(**BASE_LAYOUT)
        bar_style(fig)
        st.plotly_chart(fig, use_container_width=True)

    # ── Most and least popular categories (spec requirement)
    st.markdown('<span class="section-label">Most & Least Popular Categories</span>', unsafe_allow_html=True)
    cat_all = F["CourseCategory"].value_counts().reset_index()
    cat_all.columns = ["Category", "Enrollments"]
    cat_all["Rank"] = ["⭐ Most Popular" if i < 3 else ("⚠️ Least Popular" if i >= len(cat_all)-3 else "Mid")
                        for i in range(len(cat_all))]

    fig = px.bar(
        cat_all, x="Enrollments", y="Category",
        orientation="h", color="Rank",
        color_discrete_map={
            "⭐ Most Popular":  "#2a7f7f",
            "Mid":              "#c8a87a",
            "⚠️ Least Popular": "#c4614a"
        },
        text="Enrollments",
        title="All Categories Ranked — Top 3 vs Bottom 3 Highlighted"
    )
    fig.update_traces(textposition="outside", textfont_size=10)
    fig.update_layout(**BASE_LAYOUT, height=440, yaxis=dict(autorange="reversed"))
    bar_style(fig)
    st.plotly_chart(fig, use_container_width=True)

    # ── Behavioral Insights
    st.markdown('<span class="section-label">Behavioral Insights</span>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)

    with c1:
        # Average courses taken per learner by age group
        avg_c = (
            F.groupby(["UserID", "AgeGroup"], observed=True)
             .size().reset_index(name="Courses")
             .groupby("AgeGroup", observed=True)["Courses"]
             .mean().round(2).reset_index()
        )
        avg_c.columns = ["AgeGroup", "Avg Courses"]
        fig = px.bar(
            avg_c, x="AgeGroup", y="Avg Courses",
            color="AgeGroup", color_discrete_sequence=PAL_WARM, text="Avg Courses",
            title="Avg Courses Taken per Learner by Age Group"
        )
        fig.update_traces(textposition="outside", textfont_size=11)
        fig.update_layout(**BASE_LAYOUT, showlegend=False)
        bar_style(fig)
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        # Enrollment concentration among active users
        user_counts = F.groupby("UserID").size().reset_index(name="Courses")
        bins_c  = [0, 1, 2, 3, 4, 5, 100]
        labels_c = ["1", "2", "3", "4", "5", "6+"]
        user_counts["Bucket"] = pd.cut(user_counts["Courses"], bins=bins_c, labels=labels_c)
        bkt = user_counts["Bucket"].value_counts().sort_index().reset_index()
        bkt.columns = ["Courses Enrolled", "No. of Learners"]
        fig = px.bar(
            bkt, x="Courses Enrolled", y="No. of Learners",
            color="Courses Enrolled", color_discrete_sequence=PAL_WARM,
            text="No. of Learners",
            title="Enrollment Concentration — Courses per Learner"
        )
        fig.update_traces(textposition="outside", textfont_size=11)
        fig.update_layout(**BASE_LAYOUT, showlegend=False)
        bar_style(fig)
        st.plotly_chart(fig, use_container_width=True)


# ══════════════════════════════════════════════════════
#  TAB 3 ── GENDER-BASED COURSE PREFERENCE ANALYSIS
#
#  Spec Methodology: Demographics × Course Preference
#    ✔ Gender vs course level comparisons
#    ✔ Identify learner segments and their preferences
#    ✔ Gender × category analysis
# ══════════════════════════════════════════════════════
with tab3:
    st.markdown("### Gender-based Course Preference Analysis")
    st.markdown(
        "*Gender vs course level · gender vs category · "
        "learner segment identification by preference*"
    )

    # ── Gender vs Course Level
    st.markdown('<span class="section-label">Gender vs Course Level</span>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)

    with c1:
        glvl = F.groupby(["Gender", "CourseLevel"]).size().reset_index(name="Enrollments")
        fig = px.bar(
            glvl, x="CourseLevel", y="Enrollments", color="Gender",
            barmode="group", color_discrete_sequence=PAL_GENDER, text_auto=True,
            title="Beginner / Intermediate / Advanced Split by Gender"
        )
        fig.update_traces(textposition="outside", textfont_size=10)
        fig.update_layout(**BASE_LAYOUT)
        bar_style(fig)
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        # Gender level share as 100% stacked
        glvl_pct = (F.groupby(["Gender", "CourseLevel"])
                     .size().reset_index(name="Count"))
        totals = glvl_pct.groupby("Gender")["Count"].transform("sum")
        glvl_pct["Share (%)"] = (glvl_pct["Count"] / totals * 100).round(1)
        fig = px.bar(
            glvl_pct, x="Gender", y="Share (%)", color="CourseLevel",
            barmode="stack", color_discrete_sequence=PAL_LEVEL, text="Share (%)",
            title="Level Preference Share (%) by Gender"
        )
        fig.update_traces(textposition="inside", textfont_size=10)
        fig.update_layout(**BASE_LAYOUT)
        bar_style(fig)
        st.plotly_chart(fig, use_container_width=True)

    # ── Gender vs Course Category
    st.markdown('<span class="section-label">Gender vs Course Category</span>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)

    with c1:
        gcat = F.groupby(["Gender", "CourseCategory"]).size().reset_index(name="Enrollments")
        fig = px.bar(
            gcat, x="CourseCategory", y="Enrollments", color="Gender",
            barmode="group", color_discrete_sequence=PAL_GENDER,
            title="Category Preference by Gender"
        )
        fig.update_layout(**BASE_LAYOUT, height=360, xaxis=dict(tickangle=-35))
        bar_style(fig)
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        # Gender × Category heatmap
        pivot_gc = pd.pivot_table(
            F, values="TransactionID", index="Gender",
            columns="CourseCategory", aggfunc="count", fill_value=0
        )
        fig = px.imshow(
            pivot_gc, text_auto=True,
            color_continuous_scale=["#f8f4ee","#3da8a8","#1c2b4a"],
            aspect="auto",
            title="Gender × Category Heatmap"
        )
        fig.update_layout(
            **BASE_LAYOUT, height=220,
            xaxis=dict(tickangle=-35, tickfont_size=10),
            coloraxis_showscale=False
        )
        st.plotly_chart(fig, use_container_width=True)

    # ── Learner Segment Identification
    st.markdown('<span class="section-label">Learner Segment Identification</span>', unsafe_allow_html=True)
    # Cross: Age Group × Gender × top category preference per segment
    seg = (F.groupby(["AgeGroup", "Gender", "CourseCategory"], observed=True)
            .size().reset_index(name="Enrollments"))
    top_seg = (seg.sort_values("Enrollments", ascending=False)
                  .groupby(["AgeGroup", "Gender"], observed=True)
                  .first()
                  .reset_index()
                  .rename(columns={"CourseCategory": "Top Category"}))

    fig = px.scatter(
        seg, x="AgeGroup", y="CourseCategory",
        size="Enrollments", color="Gender",
        color_discrete_sequence=PAL_GENDER,
        size_max=35,
        title="Learner Segments — Age Group × Category × Gender (bubble size = enrollments)"
    )
    fig.update_layout(**BASE_LAYOUT, height=440)
    bar_style(fig)
    st.plotly_chart(fig, use_container_width=True)


# ══════════════════════════════════════════════════════
#  TAB 4 ── COURSE CATEGORY POPULARITY VISUALS
#
#  Spec Methodology:
#    ✔ Age group vs course category heatmaps
#    ✔ Beginner vs advanced learner behavior patterns
#    ✔ Count enrollments by CourseLevel
# ══════════════════════════════════════════════════════
with tab4:
    st.markdown("### Course Category Popularity & Level Analysis")
    st.markdown(
        "*Age group vs category heatmap · level preference distribution · "
        "beginner vs advanced behaviour patterns*"
    )

    # ── Category popularity
    st.markdown('<span class="section-label">Category Popularity Index</span>', unsafe_allow_html=True)
    c1, c2 = st.columns([3, 2])

    with c1:
        cat_pop = F["CourseCategory"].value_counts().reset_index()
        cat_pop.columns = ["Category", "Enrollments"]
        fig = px.bar(
            cat_pop, x="Enrollments", y="Category",
            orientation="h", color="Enrollments",
            color_continuous_scale=["#efe8dc","#8b6f47","#4a3520"],
            text="Enrollments",
            title="All Categories Ranked by Enrollment"
        )
        fig.update_traces(textposition="outside", textfont_size=10)
        fig.update_layout(**BASE_LAYOUT, height=420,
                          coloraxis_showscale=False,
                          yaxis=dict(autorange="reversed"))
        bar_style(fig)
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        # Level preference distribution
        lv = F["CourseLevel"].value_counts().reset_index()
        lv.columns = ["Level", "Enrollments"]
        fig = px.pie(
            lv, names="Level", values="Enrollments",
            color_discrete_sequence=PAL_LEVEL, hole=0.52,
            title="Level Preference Distribution"
        )
        fig.update_layout(**BASE_LAYOUT)
        pie_style(fig)
        st.plotly_chart(fig, use_container_width=True)

    # ── Age group × category heatmap (spec requirement)
    st.markdown('<span class="section-label">Age Group × Course Category Heatmap</span>', unsafe_allow_html=True)
    pivot_ac = pd.pivot_table(
        F, values="TransactionID", index="AgeGroup",
        columns="CourseCategory", aggfunc="count",
        fill_value=0, observed=False
    )
    fig = px.imshow(
        pivot_ac, text_auto=True,
        color_continuous_scale=["#f8f4ee","#c8a87a","#4a3520"],
        aspect="auto",
        title="Enrollment Intensity: Age Group × Course Category"
    )
    fig.update_layout(
        **BASE_LAYOUT, height=280,
        xaxis=dict(tickangle=-35, tickfont_size=10),
        coloraxis_showscale=False
    )
    st.plotly_chart(fig, use_container_width=True)

    # ── Category × Level stacked
    st.markdown('<span class="section-label">Category × Level Breakdown</span>', unsafe_allow_html=True)
    cl = F.groupby(["CourseCategory", "CourseLevel"]).size().reset_index(name="Enrollments")
    fig = px.bar(
        cl, x="CourseCategory", y="Enrollments", color="CourseLevel",
        barmode="stack", color_discrete_sequence=PAL_LEVEL, text_auto=True,
        title="Level Composition within Each Category"
    )
    fig.update_traces(textposition="inside", textfont_size=9)
    fig.update_layout(**BASE_LAYOUT, height=360, xaxis=dict(tickangle=-30))
    bar_style(fig)
    st.plotly_chart(fig, use_container_width=True)

    # ── Beginner vs Advanced learner behaviour patterns (spec requirement)
    st.markdown('<span class="section-label">Beginner vs Advanced Learner Behaviour Patterns</span>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)

    with c1:
        beg = F[F["CourseLevel"] == "Beginner"]["CourseCategory"].value_counts().reset_index()
        beg.columns = ["Category", "Enrollments"]
        fig = px.bar(
            beg, x="Enrollments", y="Category",
            orientation="h", color="Enrollments",
            color_continuous_scale=["#d4f0f0","#2a7f7f","#1c4f4f"],
            text="Enrollments",
            title="🟢 Beginner Learners — Category Preferences"
        )
        fig.update_traces(textposition="outside", textfont_size=10)
        fig.update_layout(**BASE_LAYOUT, height=380,
                          coloraxis_showscale=False,
                          yaxis=dict(autorange="reversed"))
        bar_style(fig)
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        adv = F[F["CourseLevel"] == "Advanced"]["CourseCategory"].value_counts().reset_index()
        adv.columns = ["Category", "Enrollments"]
        fig = px.bar(
            adv, x="Enrollments", y="Category",
            orientation="h", color="Enrollments",
            color_continuous_scale=["#fce8e3","#c4614a","#7a2f20"],
            text="Enrollments",
            title="🔴 Advanced Learners — Category Preferences"
        )
        fig.update_traces(textposition="outside", textfont_size=10)
        fig.update_layout(**BASE_LAYOUT, height=380,
                          coloraxis_showscale=False,
                          yaxis=dict(autorange="reversed"))
        bar_style(fig)
        st.plotly_chart(fig, use_container_width=True)

    # Beginner vs Advanced side-by-side summary
    beg_top = F[F["CourseLevel"]=="Beginner"]["CourseCategory"].value_counts().head(5).reset_index()
    beg_top.columns = ["Category","Beginner"]
    adv_top = F[F["CourseLevel"]=="Advanced"]["CourseCategory"].value_counts().head(5).reset_index()
    adv_top.columns = ["Category","Advanced"]
    compare = beg_top.merge(adv_top, on="Category", how="outer").fillna(0)
    compare_m = compare.melt(id_vars="Category", var_name="Level", value_name="Enrollments")
    fig = px.bar(
        compare_m, x="Category", y="Enrollments", color="Level",
        barmode="group",
        color_discrete_map={"Beginner":"#2a7f7f","Advanced":"#c4614a"},
        text_auto=True,
        title="Beginner vs Advanced — Top 5 Category Preferences Side by Side"
    )
    fig.update_traces(textposition="outside", textfont_size=10)
    fig.update_layout(**BASE_LAYOUT, height=360, xaxis=dict(tickangle=-20))
    bar_style(fig)
    st.plotly_chart(fig, use_container_width=True)

# ─────────────────────────────────────────────
#  FOOTER
# ─────────────────────────────────────────────
st.divider()
st.markdown("""
<div style="text-align:center;padding:14px 0;color:#8a7d6e;font-size:12px;">
    EduPro Learner Analytics Dashboard &nbsp;·&nbsp; Built with Streamlit &amp; Plotly &nbsp;·&nbsp;
    Unified Mentor × Toronto Government Parks, Forestry &amp; Recreation &nbsp;·&nbsp; 2025
</div>
""", unsafe_allow_html=True)
