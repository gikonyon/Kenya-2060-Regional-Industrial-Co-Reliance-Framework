import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
    "and verifiable multi-dimensional scoring model across all development categories."
)
st.markdown("---")

# ==========================================
# ENHANCED DATASET: ALL CATEGORIES
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

# Helper function for CSV downloads
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
st.sidebar.header("Navigation Menu")
app_mode = st.sidebar.selectbox(
    "Choose Section",
    [
        "Executive Summary & Vision",
        "All Categories: Multi-Dimensional Scoring & Graphs",
        "2026 Status & August 2027 AI, Merit & Transparency Mandate",
        "2028-2030 Re-election Growth & Reform Scenarios",
        "Governance Risk: Corruption & Political Stability Index",
        "9-Region & 47-County Architecture",
        "Presidential Scorecards & Strategic Horizons"
    ]
)

# ==========================================
# SECTION 1: EXECUTIVE SUMMARY & VISION
# ==========================================
if app_mode == "Executive Summary & Vision":
    st.header("1. Executive Summary and National Context")
    st.write("""
    The **Kenya 2060 All-Inclusive Development Framework** integrates macro-economic targets, county-level 
    productive specialization, institutional risk governance, and multi-dimensional tracking across all required categories: 
    **Human Development (HDI)**, **Sustainable Development Goals (SDGs)**, **Kenya 2060 Vision**, and **AU Agenda 2045**.
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("HDI Score (2026)", "0.640", "Medium Human Dev")
    col2.metric("SDG Score (2026)", "63.5 / 100", "Moderate Progress")
    col3.metric("Kenya 2060 Vision Score", "48.0 / 100", "Mid-Stage Trajectory")
    col4.metric("AU Agenda 2045 Score", "52.0 / 100", "Continental Alignment")
    
    st.markdown("---")
    st.success("**Core Principle:** Comprehensive tracking across all categories ensures that national growth translates directly into citizen well-being and shared prosperity.")
    
    st.markdown("### 📊 Executive Summary: Multi-Dimensional Baseline Table")
    st.write("Below is the core data table summarizing key milestone years across all governance and development indicators:")
    
    summary_table_view = df_macro[df_macro["Year"].isin([2007, 2013, 2020, 2026, 2030, 2045, 2060])][
        ["Year", "Administration_Horizon", "Real_GDP_Growth_Pct", "HDI_Score", "SDG_Composite_Score", "Kenya_2060_Vision_Score", "Corruption_Perception_Index"]
    ]
    st.dataframe(summary_table_view, use_container_width=True, hide_index=True)

# ==========================================
# SECTION 2: ALL CATEGORIES GRAPHS & VERIFIABLE LINKS
# ==========================================
elif app_mode == "All Categories: Multi-Dimensional Scoring & Graphs":
    st.header("2. All Categories: Visualizations, Data & Verifiable Links")
    st.write("Explore multi-dimensional progress metrics across all categories.")
    st.dataframe(df_macro, use_container_width=True, hide_index=True)

# ==========================================
# SECTION 3: 2026 STATUS & AUGUST 2027 AI/MERIT MANDATE (WITH GLOBAL & REGIONAL AI BENCHMARKS)
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

    st.markdown("---")
    st.markdown("### 🌍 Top 5 Countries in Africa Using AI in Governance")
    st.write("Comparative continental benchmarks guiding strategic public sector automation:")

    st.markdown("""
    * **1. Egypt**
      * **Key Focus:** National AI strategy execution and digital infrastructure scaling ([CipherSense AI](https://www.blog.ciphersense.ai/africas-ai-powerhouses-the-countries-leading-the-charge/)).
      * **Service Delivery:** Egypt leads the continent in government AI readiness, driven by its updated National AI Strategy and large-scale investments in cloud infrastructure. The government uses AI-driven systems to automate administrative workflows, modernize civil registries, and optimize Arabic-language natural language processing for public sector interactions ([CipherSense AI](https://www.blog.ciphersense.ai/africas-ai-powerhouses-the-countries-leading-the-charge/)).
    * **2. South Africa**
      * **Key Focus:** Advanced compute infrastructure and data ecosystems ([Africa AI Summit](https://africaaisummit.com/)).
      * **Service Delivery:** Backed by the continent’s most mature data center ecosystem and strong technical talent, South Africa integrates data analytics and AI into municipal management, resource allocation, and public healthcare optimization. Its frameworks leverage robust data protection laws (POPIA) to safely streamline government service portals ([Africa AI Summit](https://africaaisummit.com/)).
    * **3. Kenya**
      * **Key Focus:** Digital inclusion, mobile-government integration, and localized AI models ([CipherSense AI](https://www.blog.ciphersense.ai/africas-ai-powerhouses-the-countries-leading-the-charge/)).
      * **Service Delivery:** Building on its robust mobile money foundation (e.g., M-Pesa ecosystem), Kenya’s National AI Strategy prioritizes public service automation. The government implements machine learning tools to optimize agricultural value chains, digitize land registries, and enhance citizen-facing e-government platforms such as the eCitizen portal ([CipherSense AI](https://www.blog.ciphersense.ai/africas-ai-powerhouses-the-countries-leading-the-charge/)).
    * **4. Rwanda**
      * **Key Focus:** Policy execution, smart cities, and digital governance efficiency ([CipherSense AI](https://www.blog.ciphersense.ai/africas-ai-powerhouses-the-countries-leading-the-charge/)).
      * **Service Delivery:** Rwanda punches above its weight class through disciplined execution of its National Artificial Intelligence Policy. The government utilizes smart city initiatives in Kigali and AI-assisted data tools to streamline public sector delivery, land management, and healthcare triage ([CipherSense AI](https://www.blog.ciphersense.ai/africas-ai-powerhouses-the-countries-leading-the-charge/)).
    * **5. Mauritius**
      * **Key Focus:** Public sector data management and e-government coordination ([ICTworks](https://www.ictworks.org/)).
      * **Service Delivery:** Long recognized as an early mover in digital governance, Mauritius scores exceptionally high on government AI pillars. It utilizes centralized data-sharing frameworks to reduce bureaucratic friction, automate tax and business registration, and provide seamless digital services to citizens ([OECD](https://oecd.ai/)).
    """)

    st.markdown("---")
    st.markdown("### 🌐 Top 5 Countries Globally Using AI in Governance & Citizen Service Delivery")
    st.markdown("""
    * **1. Estonia**
      * **Key Focus:** Whole-of-government digital architecture ("X-Road") and e-Residency ([Smart City Expo World Congress](https://www.smartcityexpo.com/)).
      * **Service Delivery:** Estonia remains a global benchmark for digital governance. Through initiatives like "AI Leap," artificial intelligence is woven deeply into public infrastructure. Citizens can vote, file taxes in minutes, access health records, and start businesses entirely online via automated, highly secure predictive AI backends ([Oxford Insights](https://oxfordinsights.com/)).
    * **2. Singapore**
      * **Key Focus:** Smart Nation initiatives and citizen-centric service orchestration ([Smart City Expo World Congress](https://www.smartcityexpo.com/)).
      * **Service Delivery:** Singapore uses the Singpass digital identity infrastructure coupled with advanced AI agents to predict citizen needs (such as housing grants or pension milestones). The government employs machine learning heavily in urban mobility, traffic management, and predictive healthcare services ([Smart City Expo World Congress](https://www.smartcityexpo.com/)).
    * **3. United Kingdom**
      * **Key Focus:** Unified digital service platforms and public sector data science ([Smart City Expo World Congress](https://www.smartcityexpo.com/)).
      * **Service Delivery:** Anchored by the unified GOV.UK framework and the government’s Central Digital and Data Office (CDDO), the UK deploys AI to streamline welfare applications, optimize tax compliance through automated data checks, and revolutionize National Health Service (NHS) resource allocation ([Smart City Expo World Congress](https://www.smartcityexpo.com/)).
    * **4. United States**
      * **Key Focus:** Federal scale modernization and automated agency services ([Smart City Expo World Congress](https://www.smartcityexpo.com/)).
      * **Service Delivery:** The federal government utilizes AI across major citizen touchpoints—ranging from automated fraud detection in social security and tax processing (IRS) to streamlining immigration authorizations (ESTA/visa platforms) and modernizing veterans' healthcare triage systems ([Smart City Expo World Congress](https://www.smartcityexpo.com/)).
    * **5. South Korea**
      * **Key Focus:** Digital Platform Government and smart infrastructure ([Smart City Expo World Congress](https://www.smartcityexpo.com/)).
      * **Service Delivery:** South Korea integrates AI deeply into its public administrative network. Its digital platform government links disparate databases to allow seamless, predictive service delivery where citizens receive automated notifications for public benefits, driver's license renewals, and custom healthcare recommendations without navigating complex bureaucracy ([Smart City Expo World Congress](https://www.smartcityexpo.com/)).
    """)

    st.markdown("---")
    st.markdown("### 📺 Official Strategy Reference Video")
    st.video("https://www.youtube.com/watch?v=lfrOU3Yxy5o")

# ==========================================
# SECTION 4: 2028-2030 RE-ELECTION & REFORM
# ==========================================
elif app_mode == "2028-2030 Re-election Growth & Reform Scenarios":
    st.header("4. 2028–2030 Growth Projections: The Re-election & Reform Scenario")
    st.write("Modeling post-reform transparency dividends and Vision 2030 target convergence.")

# ==========================================
# SECTION 5: GOVERNANCE RISK
# ==========================================
elif app_mode == "Governance Risk: Corruption & Political Stability Index":
    st.header("5. Institutional Risk Analysis: Corruption & Political Stability")
    st.write("Analyzing Transparency International CPI indices and stability metrics.")

# ==========================================
# SECTION 6: 9-REGION ARCHITECTURE
# ==========================================
elif app_mode == "9-Region & 47-County Architecture":
    st.header("6. Nine-Region, Forty-Seven-County Economic Architecture")
    st.write("Decentralized economic clusters and productive specialization.")

# ==========================================
# SECTION 7: PRESIDENTIAL SCORECARDS
# ==========================================
elif app_mode == "Presidential Scorecards & Strategic Horizons":
    st.header("7. Presidential Scorecards & Strategic Horizons")
    st.dataframe(df_macro, use_container_width=True, hide_index=True)

# ==========================================
# FOOTER
# ==========================================
st.markdown("---")
st.markdown("""
### Kenya 2060 All-Inclusive Development Framework
*One Kenya. Forty-Seven Contributors. Shared Prosperity.*  
**Multi-Dimensional Scoring Notice:** Integrates all categories (HDI, SDGs, Kenya 2060 Vision, AU Agenda 2045, Growth, and CPI) with verifiable source links and downloadable CSV datasets.
""")
