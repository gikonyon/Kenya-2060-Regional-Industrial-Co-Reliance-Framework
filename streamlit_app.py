import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Kenya 2060 Development Framework & Multi-Dimensional Scoring",
    page_icon="🇰🇪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# HEADER & TITLE
# ==========================================
st.title("🇰🇪 Kenya 2060 All-Inclusive Development Framework")
st.markdown("### *One Kenya. Forty-Seven Contributors. Shared Prosperity.*")
st.caption(
    "An interactive policy, governance risk, AI transparency architecture, "
    "and multi-dimensional scoring model (HDI, SDGs, Kenya 2060, & AU Agenda 2045)."
)
st.markdown("---")

# ==========================================
# ENHANCED DATASET: MULTI-DIMENSIONAL SCORING
# ==========================================
@st.cache_data
def get_multidimensional_dataset():
    data = {
        "Year": [
            2004, 2007, 2010, 2013, 2018, 
            2020, 2023, 2026, 2027, 2028, 2030, 2045, 2060
        ],
        "Administration_Horizon": [
            "Mwai Kibaki", "Mwai Kibaki", "Mwai Kibaki",
            "Uhuru Kenyatta", "Uhuru Kenyatta", "Uhuru Kenyatta",
            "William Ruto", "William Ruto (Current Baseline)", "William Ruto (August 2027 AI & Merit Mandate)",
            "Ruto Term II (Reform Scenario)", "Vision 2030 / Milestone", "AU Agenda 2045 Horizon", "Kenya Vision 2060 Target"
        ],
        "Real_GDP_Growth_Pct": [
            5.1, 7.0, 5.8, 5.9, 6.3, 
            -0.3, 5.6, 5.3, 5.9, 6.5, 7.0, 7.2, 8.0
        ],
        "HDI_Score": [
            0.512, 0.535, 0.559, 0.575, 0.601, 
            0.611, 0.628, 0.640, 0.648, 0.665, 0.675, 0.730, 0.810
        ],
        "SDG_Composite_Score": [
            45.2, 48.1, 51.0, 53.5, 57.2, 
            58.1, 61.4, 63.5, 66.0, 68.5, 70.0, 85.0, 96.5
        ],
        "Kenya_2060_Vision_Score": [
            15.0, 18.2, 22.0, 26.5, 32.0, 
            34.5, 40.0, 48.0, 56.0, 64.0, 72.0, 90.0, 100.0
        ],
        "AU_Agenda_2045_Score": [
            20.0, 23.0, 27.0, 31.0, 37.0, 
            40.0, 45.0, 52.0, 60.0, 68.0, 75.0, 95.0, 100.0
        ],
        "Corruption_Perception_Index": [
            21, 21, 21, 27, 27, 
            31, 31, 32, 38, 44, 52, 68, 80
        ],
        "Political_Stability_Index": [
            -1.15, -1.45, -0.85, -1.05, -0.92, 
            -0.88, -0.95, -0.90, -0.80, -0.55, -0.20, +0.40, +0.80
        ],
        "Data_Status": [
            "Historical", "Historical", "Historical",
            "Historical", "Historical", "Historical",
            "Historical", "Current Baseline (2026)", "Aug 2027 AI & Meritocracy Mandate",
            "Conditional Re-election Scenario (2028)", "Strategic Policy Target (2030)",
            "AU Agenda 2045 Projection", "Kenya Vision 2060 Target"
        ]
    }
    return pd.DataFrame(data)

df_macro = get_multidimensional_dataset()

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
st.sidebar.header("Navigation Menu")
app_mode = st.sidebar.selectbox(
    "Choose Section",
    [
        "Executive Summary & Vision",
        "Multi-Dimensional Scoring (HDI, SDGs, Kenya 2060, AU 2045)",
        "2026 Status & August 2027 AI, Merit & Transparency Mandate",
        "2028-2030 Re-election Growth & Reform Scenarios",
        "Governance Risk: Corruption & Political Stability Index",
        "9-Region & 47-County Architecture",
        "Presidential Scorecards & Strategic Horizons"
    ]
)

# ==========================================
# SECTION 1: EXECUTIVE SUMMARY
# ==========================================
if app_mode == "Executive Summary & Vision":
    st.header("1. Executive Summary and National Context")
    st.write("""
    The **Kenya 2060 All-Inclusive Development Framework** integrates macro-economic targets, county-level 
    productive specialization, institutional risk governance, and multi-dimensional tracking across **Human Development (HDI)**, 
    **Sustainable Development Goals (SDGs)**, **Kenya 2060 Vision**, and **AU Agenda 2045** continental milestones.
    """)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("HDI Score (2026)", "0.640", "Medium Human Dev")
    col2.metric("SDG Score (2026)", "63.5 / 100", "Moderate Progress")
    col3.metric("Kenya 2060 Vision Score", "48.0 / 100", "Mid-Stage Trajectory")
    col4.metric("AU Agenda 2045 Score", "52.0 / 100", "Continental Alignment")
    st.markdown("---")
    st.success("**Core Principle:** Comprehensive tracking across HDI, SDGs, Kenya 2060, and AU Agenda 2045 ensures that national growth translates directly into citizen well-being and shared prosperity.")

# ==========================================
# SECTION 2: MULTI-DIMENSIONAL SCORING
# ==========================================
elif app_mode == "Multi-Dimensional Scoring (HDI, SDGs, Kenya 2060, AU 2045)":
    st.header("2. Multi-Dimensional Development Scoring Framework")
    st.write("""
    This section evaluates Kenya's progression across four critical score domains from historical baselines (2004) 
    through the **August 2027 AI & Meritocracy Mandate**, the **2028–2030 reform window**, the **AU Agenda 2045 horizon**, 
    and ultimately **Kenya Vision 2060**.
    """)
    
    # Latest / Current 2026 Scorecard metric display
    current_row = df_macro[df_macro["Year"] == 2026].iloc[0]
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Human Development (HDI)", f"{current_row['HDI_Score']:.3f}", "Target: 0.810 (2060)")
    col2.metric("SDG Progress Score", f"{current_row['SDG_Composite_Score']:.1f}/100", "Target: 96.5 (2060)")
    col3.metric("Kenya 2060 Framework Score", f"{current_row['Kenya_2060_Vision_Score']:.1f}/100", "Target: 100 (2060)")
    col4.metric("AU Agenda 2045 Score", f"{current_row['AU_Agenda_2045_Score']:.1f}/100", "Target: 100 (2045)")

    st.markdown("---")
    st.subheader("📈 Multi-Dimensional Score Trajectory (2004 - 2060)")
    
    # Plotly multi-index comparison
    fig_multi = px.line(
        df_macro, x="Year", y=["SDG_Composite_Score", "Kenya_2060_Vision_Score", "AU_Agenda_2045_Score"],
        markers=True, title="Comparative Index Progression (SDGs, Kenya 2060, & AU Agenda 2045)",
        labels={"value": "Score (0 - 100)", "variable": "Framework Dimension", "Year": "Year"}
    )
    st.plotly_chart(fig_multi, use_container_width=True)

    st.subheader("🌐 Human Development Index (HDI) Trajectory")
    fig_hdi = px.line(
        df_macro, x="Year", y="HDI_Score", markers=True,
        title="Human Development Index (HDI) Long-Term Growth",
        labels={"HDI_Score": "HDI Score", "Year": "Year"},
        hover_data=["Administration_Horizon", "Data_Status"]
    )
    st.plotly_chart(fig_hdi, use_container_width=True)

    st.markdown("### Underlying Multi-Dimensional Data Matrix")
    st.dataframe(df_macro[["Year", "Administration_Horizon", "HDI_Score", "SDG_Composite_Score", "Kenya_2060_Vision_Score", "AU_Agenda_2045_Score", "Data_Status"]], use_container_width=True, hide_index=True)

# ==========================================
# SECTION 3: 2026 STATUS & AUGUST 2027 AI/MERIT MANDATE
# ==========================================
elif app_mode == "2026 Status & August 2027 AI, Merit & Transparency Mandate":
    st.header("3. 2026 Baseline & August 2027 AI, Merit & Transparency Mandate")
    st.write("""
    Evaluating where Kenya stands in **2026** and projecting the mandatory institutional deliverables expected by **August 2027** 
    to ensure that government approvals, public processes, and resource distribution are fully transparent, automated, and merit-based.
    """)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("📍 Current Status (2026)")
        st.markdown("""
        * **Real GDP Growth:** Stabilizing around **5.3% - 5.5%**.
        * **Industrialization Share:** Hovering near **11.4%** of GDP.
        * **Administrative Challenge:** Discretionary bureaucratic approvals and manual licensing bottlenecks continue to erode citizen trust.
        * **Digital Foundation:** eCitizen platforms provide the baseline needed for advanced AI-driven transparency.
        """)
    with col_b:
        st.subheader("🤖 August 2027 AI & Meritocracy Mandate")
        st.markdown("""
        * **Automated Government Approvals:** Complete removal of human discretion in routine regulatory approvals using rule-based AI systems.
        * **Open Transparency & FOIA Portals:** Real-time public dashboards tracking county exchequer disbursements and tenders.
        * **Strict Merit-Based Public Appointments:** Institutionalizing algorithmic tracking and competitive public service examinations.
        * **Inclusive Grievance Redress:** Automated tracking of public feedback across all 47 counties.
        """)
    
    st.markdown("---")
    status_table = df_macro[df_macro["Year"].between(2026, 2027)][
        ["Year", "Administration_Horizon", "Real_GDP_Growth_Pct", "HDI_Score", "SDG_Composite_Score", "Data_Status"]
    ]
    st.dataframe(status_table, use_container_width=True, hide_index=True)

# ==========================================
# SECTION 4: 2028-2030 RE-ELECTION & REFORM SCENARIOS
# ==========================================
elif app_mode == "2028-2030 Re-election Growth & Reform Scenarios":
    st.header("4. 2028–2030 Growth Projections: The Re-election & Reform Scenario")
    st.write("""
    If President Ruto is re-elected for a second term (2028–2032) and successfully embeds the **August 2027 AI transparency, 
    automation, and meritocracy mandates**, economic and multi-dimensional scoring indicators are projected to experience a strong structural surge.
    """)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Projected 2028 Growth", "6.5%", "Post-Reform Transparency Dividend")
    col2.metric("Projected 2030 SDG Score", "70.0 / 100", "Vision 2030 Alignment")
    col3.metric("AU Agenda 2045 2030 Milestone", "75.0 / 100", "Continental Benchmarking")

    fig_growth = px.line(
        df_macro, x="Year", y="Real_GDP_Growth_Pct", markers=True,
        title="Real GDP Growth Trajectory & 2028-2030 Reform Projection",
        labels={"Real_GDP_Growth_Pct": "Real GDP Growth (%)", "Year": "Year"},
        hover_data=["Administration_Horizon", "Data_Status"]
    )
    fig_growth.update_yaxes(ticksuffix="%")
    st.plotly_chart(fig_growth, use_container_width=True)

# ==========================================
# SECTION 5: GOVERNANCE RISK (CORRUPTION & STABILITY)
# ==========================================
elif app_mode == "Governance Risk: Corruption & Political Stability Index":
    st.header("5. Institutional Risk Analysis: Corruption & Political Stability")
    st.write("""
    Economic models fail when institutional decay, political volatility, and opaque discretionary power are ignored. 
    By introducing **AI automation and meritocracy by August 2027**, Kenya can actively bend the Corruption Perceptions Index (CPI) 
    upward and stabilize political friction.
    """)
    
    col_gov1, col_gov2 = st.columns(2)
    with col_gov1:
        st.subheader("📈 Corruption Perceptions Index (CPI Trend)")
        st.write("""
        *Measured on a scale from 0 (highly corrupt) to 100 (very clean).*
        * Historically stagnant in the low 30s.
        * **The AI & Automation Solution:** Removing human middlemen from licensing and permits drastically cuts corruption.
        * **2030 Target:** Surging toward 52+ as automated procurement takes full effect.
        """)
    with col_gov2:
        st.subheader("⚖️ Political Stability & Violence Index")
        st.write("""
        *Measured from approximately -2.5 (high instability) to +2.5 (high stability).*
        * Civil unrest and tax protests often stem from perceived unfairness and lack of accountability.
        * **The Inclusion Dividend:** Transparent, merit-based governance guarantees that marginalized communities see fair representation.
        """)

    st.subheader("📊 Comparative Tracking: Corruption Index Improvement vs. GDP Growth")
    fig_gov = px.line(
        df_macro, x="Year", y=["Real_GDP_Growth_Pct", "Corruption_Perception_Index"],
        markers=True, title="Macroeconomic Growth vs. AI-Driven Governance Index",
        labels={"value": "Index Score / Growth %", "variable": "Indicator"}
    )
    st.plotly_chart(fig_gov, use_container_width=True)

# ==========================================
# SECTION 6: 9-REGION ARCHITECTURE
# ==========================================
elif app_mode == "9-Region & 47-County Architecture":
    st.header("6. Nine-Region, Forty-Seven-County Economic Architecture")
    st.write("Organizing all 47 counties into functional economic zones managed through transparent, merit-driven county frameworks.")
    regions_summary = {
        "Nairobi Region": "Financial, technology, AI, big data and diplomatic headquarters.",
        "Central Region": "Coffee, tea processing, leather, and high-value agro-exports.",
        "Western Region": "Sugar processing, bagasse energy, and grain milling.",
        "Nyanza Region": "Inland lake logistics, fisheries, and aquaculture.",
        "North Rift Region": "Food security, grain handling, and livestock corridors.",
        "South Rift Region": "Dairy processing, geothermal energy, and tourism.",
        "Eastern Region": "Dryland innovation, fruit processing, and gateway logistics.",
        "North Eastern Region": "Export abattoirs, livestock trade, and solar energy systems.",
        "Coast Region": "Maritime gateways, ship repair, and coastal tourism."
    }
    for reg, mandate in regions_summary.items():
        st.markdown(f"- **{reg}:** {mandate}")

# ==========================================
# SECTION 7: PRESIDENTIAL SCORECARDS
# ==========================================
elif app_mode == "Presidential Scorecards & Strategic Horizons":
    st.header("7. Presidential Scorecards & Strategic Horizons")
    st.write("""
    A comparative breakdown of administration horizons from Kibaki (2003) through Ruto's current term, 
    the August 2027 AI/Merit Mandate, AU Agenda 2045, and Kenya Vision 2060.
    """)
    st.dataframe(df_macro, use_container_width=True, hide_index=True)

# ==========================================
# FOOTER
# ==========================================
st.markdown("---")
st.markdown("""
### Kenya 2060 All-Inclusive Development Framework
*One Kenya. Forty-Seven Contributors. Shared Prosperity.*  
**Multi-Dimensional Scoring Notice:** Integrates HDI, SDGs, Kenya 2060 Vision, and AU Agenda 2045 scorecards.
""")
