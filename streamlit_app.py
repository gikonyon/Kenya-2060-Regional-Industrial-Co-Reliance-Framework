import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Kenya 2060 Development Framework",
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
    "An interactive policy, accountability and development architecture "
    "for inclusive industrialization and shared prosperity."
)
st.markdown("---")

# ==========================================
# DATA INGESTION DATASET
# ==========================================
@st.cache_data
def get_ingestion_dataset():
    """
    Kenya 2060 development dataset.
    IMPORTANT DATA GOVERNANCE NOTE:
    Historical observations, current estimates and future policy targets
    are explicitly separated using the Data_Status column.
    """
    data = {
        "Year": [
            2004, 2007, 2010, 2013, 2018, 
            2020, 2023, 2026, 2030, 2045, 2060
        ],
        "Administration_Horizon": [
            "Mwai Kibaki", "Mwai Kibaki", "Mwai Kibaki",
            "Uhuru Kenyatta", "Uhuru Kenyatta", "Uhuru Kenyatta",
            "William Ruto", "William Ruto",
            "Vision 2030 Milestone", "AU Agenda Horizon", "Kenya Vision 2060"
        ],
        "Real_GDP_Growth_Pct": [
            5.1, 7.0, 5.8, 5.9, 6.3, 
            -0.3, 5.6, 5.3, 6.0, 7.2, 8.0
        ],
        "Industrialization_Share_Pct": [
            10.2, 10.8, 11.1, 11.5, 11.2, 
            10.5, 11.0, 11.4, 13.5, 16.0, 22.0
        ],
        "SDG_Composite_Score": [
            45.2, 48.1, 51.0, 53.5, 57.2, 
            58.1, 61.4, 63.5, 70.0, 85.0, 96.5
        ],
        "HDI_Score": [
            0.512, 0.535, 0.559, 0.575, 0.601, 
            0.611, 0.628, 0.640, 0.675, 0.730, 0.810
        ],
        "Data_Status": [
            "Historical / To Be Verified", "Historical / To Be Verified", "Historical / To Be Verified",
            "Historical / To Be Verified", "Historical / To Be Verified", "Historical / To Be Verified",
            "Historical / To Be Verified", "Current Estimate / Scenario", "Kenya 2060 Policy Target",
            "Kenya 2060 Scenario Projection", "Kenya 2060 Long-Term Target"
        ],
        "Data_Source_Verification": [
            "KNBS Economic Survey / World Bank", "KNBS Economic Survey / World Bank",
            "KNBS / UNDP Human Development Reports", "KNBS Statistical Abstract",
            "KNBS Economic Survey", "KNBS Macroeconomic / Economic Survey",
            "KNBS / UNDP World Bank", "Current estimate update from official release",
            "Vision 2030 / Kenya 2060 Policy Target", "Kenya 2060 Scenario Projection",
            "Kenya 2060 Long-Term Policy Target"
        ]
    }
    return pd.DataFrame(data)

df_ingestion = get_ingestion_dataset()

# ==========================================
# PRESIDENTIAL SCORECARD HELPER FUNCTIONS
# ==========================================
def create_presidential_scorecard(data, administration_name):
    """Displays four headline development metrics for an administration."""
    if data.empty:
        st.warning(f"No data is currently available for {administration_name}.")
        return
    latest = data.iloc[-1]
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Latest GDP Growth", f"{latest['Real_GDP_Growth_Pct']:.1f}%")
    col2.metric("Industrialization Share", f"{latest['Industrialization_Share_Pct']:.1f}%")
    col3.metric("HDI Score", f"{latest['HDI_Score']:.3f}")
    col4.metric("SDG Framework Score", f"{latest['SDG_Composite_Score']:.1f}/100")

def create_presidential_graphs(data, administration_name):
    """Displays GDP, industrialization, HDI and SDG graphs directly below the presidential scorecards."""
    if data.empty:
        return
    
    # GDP GROWTH GRAPH
    st.subheader("📈 Economic Growth Performance")
    fig_gdp = px.line(
        data, x="Year", y="Real_GDP_Growth_Pct", markers=True,
        title=f"{administration_name}: Real GDP Growth Trajectory",
        labels={"Year": "Year", "Real_GDP_Growth_Pct": "Real GDP Growth (%)"},
        hover_data=["Data_Status"]
    )
    fig_gdp.update_yaxes(ticksuffix="%")
    fig_gdp.update_layout(height=420)
    st.plotly_chart(fig_gdp, use_container_width=True)
    
    # INDUSTRIALIZATION GRAPH
    st.subheader("🏭 Industrialization & Value Addition")
    fig_industry = px.bar(
        data, x="Year", y="Industrialization_Share_Pct", text="Industrialization_Share_Pct",
        title=f"{administration_name}: Industrialization Share of GDP",
        labels={"Year": "Year", "Industrialization_Share_Pct": "Manufacturing / Industrial Share (%)"},
        hover_data=["Data_Status"]
    )
    fig_industry.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
    fig_industry.update_yaxes(ticksuffix="%")
    fig_industry.update_layout(height=420)
    st.plotly_chart(fig_industry, use_container_width=True)
    
    # HDI GRAPH
    st.subheader("🌐 Human Development Progress")
    fig_hdi = px.line(
        data, x="Year", y="HDI_Score", markers=True,
        title=f"{administration_name}: Human Development Index Trend",
        labels={"Year": "Year", "HDI_Score": "Human Development Index"},
        hover_data=["Data_Status"]
    )
    fig_hdi.update_layout(height=420)
    st.plotly_chart(fig_hdi, use_container_width=True)
    
    # SDG SCORE GRAPH
    st.subheader("🌍 Sustainable Development Goals Progress")
    fig_sdg = px.area(
        data, x="Year", y="SDG_Composite_Score",
        title=f"{administration_name}: SDG Framework Progress Score",
        labels={"Year": "Year", "SDG_Composite_Score": "SDG Framework Score (0-100)"},
        hover_data=["Data_Status"]
    )
    fig_sdg.update_yaxes(range=[0, 100])
    fig_sdg.update_layout(height=420)
    st.plotly_chart(fig_sdg, use_container_width=True)

def display_scorecard_table(data):
    """Displays the underlying data used to generate scorecards and graphs."""
    if data.empty:
        st.warning("No underlying data available.")
        return
    display_columns = [
        "Year", "Administration_Horizon", "Real_GDP_Growth_Pct",
        "Industrialization_Share_Pct", "HDI_Score", "SDG_Composite_Score",
        "Data_Status", "Data_Source_Verification"
    ]
    st.dataframe(data[display_columns], use_container_width=True, hide_index=True)

def display_validated_sources():
    """Displays the official source registry used for peer verification."""
    st.markdown("---")
    st.subheader("🔗 Validated Data Sources & Citation Registry")
    st.markdown("""
    ### Kenya National Bureau of Statistics (KNBS)
    Kenya's principal source for official economic, demographic and sectoral statistics.
    * **KNBS Official Website:** https://www.knbs.or.ke/
    * **Key indicators:** GDP growth, sector performance, manufacturing, employment and national socio-economic statistics.

    ### World Bank Open Data
    Internationally comparable development and macroeconomic indicators.
    * **Kenya Data Profile:** https://data.worldbank.org/country/kenya
    * **Key indicators:** GDP growth, poverty, population, investment and international development comparisons.

    ### UNDP Human Development Reports
    The authoritative international source for Human Development Index data.
    * **UNDP Human Development Data Center:** https://hdr.undp.org/data-center
    * **Key indicators:** Human Development Index, education, life expectancy and income dimensions.

    ### Sustainable Development Goals Kenya
    Official national SDG reporting should be used to validate individual SDG indicators.
    * **United Nations SDG Data:** https://unstats.un.org/sdgs/dataportal/
    * **Methodology Notice:** The Kenya 2060 SDG Composite Score is a framework indicator unless formally adopted and independently validated.

    ### Central Bank of Kenya (CBK)
    Official monetary, financial and macro-financial information.
    * **CBK Official Website:** https://www.centralbank.go.ke/
    * **Key indicators:** Inflation, exchange rates, reserves and financial sector conditions.
    """)

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
st.sidebar.header("Navigation Menu")
app_mode = st.sidebar.selectbox(
    "Choose Section",
    [
        "Executive Summary & Vision",
        "Constitutional Alignment & Governance",
        "Global Benchmarking (Morocco & China vs. Kenya)",
        "9-Region & 47-County Architecture",
        "Visualized Scorecards & Multi-Dimensional Metrics",
        "Presidential Scorecards & Strategic Horizons (2004-2060)",
        "Data Ingestion & Peer Verification Portal",
        "Infrastructure-to-Industry Mandate"
    ]
)

# ==========================================
# SECTION 1: EXECUTIVE SUMMARY
# ==========================================
if app_mode == "Executive Summary & Vision":
    st.header("1. Executive Summary and National Context")
    st.write("""
    Kenya possesses a young population, a strategic geographical location, a devolved system of government, 
    and rich natural and human resources. However, economic opportunity, industrial development and quality 
    public services remain unevenly distributed.
    
    The **Kenya 2060 All-Inclusive Development Framework** presents a long-term model organizing all 47 counties 
    into nine functional economic regions. Moving away from raw-material dependency, the framework anchors 
    itself on domestic value addition, county-based industrial specialization, regional co-reliance and rigorous 
    public accountability.
    """)
    col1, col2, col3 = st.columns(3)
    col1.metric("Functional Regions", "9 Zones", "All 47 Counties")
    col2.metric("Target Initial Jobs", "500,000+", "Direct & Supportive")
    col3.metric("Core Vision Year", "2060", "Mature Innovation Economy")
    st.markdown("---")
    st.subheader("The Kenya 2060 Development Principle")
    st.success("""
    **Every county contributes. Every region produces. Every Kenyan participates in shared prosperity.**
    """)

# ==========================================
# SECTION 2: CONSTITUTIONAL ALIGNMENT
# ==========================================
elif app_mode == "Constitutional Alignment & Governance":
    st.header("2. Constitutional Alignment & Resilient Governance")
    st.write("""
    The Kenya 2060 Framework is designed to reduce legal and implementation risks by embedding constitutional compliance, 
    meaningful public participation, transparent public finance and devolved development principles from the earliest stages of project design.
    """)
    st.info("""
    **Governance Principle:** Constitutional compliance and meaningful public participation cannot guarantee the absence of legal challenges, 
    but they can significantly strengthen legitimacy, accountability and implementation resilience.
    """)
    tab1, tab2, tab3 = st.tabs([
        "Article 10 (Inclusiveness)",
        "Article 201 (Public Finance)",
        "Chapter 11 (Devolution)"
    ])
    with tab1:
        st.subheader("National Values & Principles")
        st.write("The framework promotes national unity, inclusiveness, social justice and equitable opportunity by ensuring that every county has a meaningful productive role within the national economy.")
    with tab2:
        st.subheader("Principles of Public Finance")
        st.write("Capital expenditure should promote equitable development and productive capacity while avoiding idle assets, inefficient projects and unsustainable public financial obligations.")
    with tab3:
        st.subheader("Objects of Devolution")
        st.write("County governments are positioned as active development partners, enabling locally appropriate economic development and strengthening productive capacity across all regions.")

# ==========================================
# SECTION 3: GLOBAL BENCHMARKING
# ==========================================
elif app_mode == "Global Benchmarking (Morocco & China vs. Kenya)":
    st.header("3. Comparative Growth Models: Learning from Global Success")
    st.write("""
    The framework draws structural lessons from international development experiences, including Morocco's industrial-logistics 
    integration and China's spatial and export-oriented industrial development.
    """)
    comparison_data = {
        "Strategic Dimension": [
            "Infrastructure Philosophy",
            "Spatial & Regional Sequencing",
            "Governance & Long-Term Planning",
            "Industrial Integration"
        ],
        "China Model": [
            "Large-scale investment in transport and industrial zones linked to supply chains.",
            "Spatial sequencing and gradual expansion of industrial development.",
            "Long-term strategic planning and coordinated implementation.",
            "Strong linkage between infrastructure and productive manufacturing."
        ],
        "Morocco (Tanger Med)": [
            "Ports integrated with industrial and logistics platforms.",
            "Strategic gateways connected to regional economic development.",
            "Specialized institutions supporting long-term industrial development.",
            "Integration of automotive, aerospace and export-oriented clusters."
        ],
        "Kenya 2060 Proposal": [
            "Infrastructure-to-Industry Mandate linking assets to productive demand.",
            "Nine functional regions supporting simultaneous national specialization.",
            "Constitutional alignment, participation and transparent accountability.",
            "Pre-planned value chains and export readiness."
        ]
    }
    df_comp = pd.DataFrame(comparison_data)
    st.dataframe(df_comp, use_container_width=True, hide_index=True)

# ==========================================
# SECTION 4: 9-REGION ARCHITECTURE
# ==========================================
elif app_mode == "9-Region & 47-County Architecture":
    st.header("4. Nine-Region, Forty-Seven-County Economic Architecture")
    st.write("""
    Every community contributes a specialized economic pillar to the national fabric. The objective is regional co-reliance rather than competition between counties.
    """)
    regions_detailed = {
        "Nairobi Region": {
            "Counties": ["Nairobi City"],
            "Core Mandate": "Financial, technology, AI, big data and diplomatic headquarters.",
            "Industrial Focus": "Fintech, software engineering, digital services, BPO and capital markets."
        },
        "Central Region": {
            "Counties": ["Kiambu", "Murang'a", "Nyeri", "Kirinyaga", "Nyandarua"],
            "Core Mandate": "Coffee, tea processing and high-value agro-exports.",
            "Industrial Focus": "Value addition, packaging, cold chains, leather processing and light manufacturing."
        },
        "Western Region": {
            "Counties": ["Kakamega", "Vihiga", "Bungoma", "Busia"],
            "Core Mandate": "Sugar processing, agro-processing and cross-border trade.",
            "Industrial Focus": "Sugar modernization, bagasse energy, grain processing and trade logistics."
        },
        "Nyanza Region": {
            "Counties": ["Kisumu", "Siaya", "Homa Bay", "Migori", "Kisii", "Nyamira"],
            "Core Mandate": "Lake logistics, fisheries and regional trade.",
            "Industrial Focus": "Inland logistics, fish processing, cotton value chains and aquaculture."
        },
        "North Rift Region": {
            "Counties": ["Uasin Gishu", "Trans Nzoia", "Nandi", "Elgeyo Marakwet", "West Pokot", "Turkana"],
            "Core Mandate": "Food security, livestock and strategic transport corridors.",
            "Industrial Focus": "Grain handling, agricultural machinery, renewable energy and resource logistics."
        },
        "South Rift Region": {
            "Counties": ["Nakuru", "Kericho", "Bomet", "Narok", "Kajiado"],
            "Core Mandate": "Tea, dairy, tourism and livestock value chains.",
            "Industrial Focus": "Dairy processing, geothermal industrial development, tourism and leather."
        },
        "Eastern Region": {
            "Counties": ["Machakos", "Kitui", "Makueni", "Embu", "Meru", "Tharaka Nithi", "Isiolo"],
            "Core Mandate": "Dryland innovation, livestock, agro-processing and gateway infrastructure.",
            "Industrial Focus": "Fruit processing, logistics, meat processing and renewable energy."
        },
        "North Eastern Region": {
            "Counties": ["Garissa", "Wajir", "Mandera"],
            "Core Mandate": "Cross-border livestock commerce and trade logistics.",
            "Industrial Focus": "Export-oriented abattoirs, hides and skins, solar energy and livestock systems."
        },
        "Coast Region": {
            "Counties": ["Mombasa", "Kwale", "Kilifi", "Tana River", "Lamu", "Taita Taveta"],
            "Core Mandate": "Maritime gateway, logistics and international trade.",
            "Industrial Focus": "Ports, maritime logistics, ship repair, fisheries processing and tourism."
        }
    }
    selected_region = st.selectbox("Select Economic Region to Inspect", list(regions_detailed.keys()))
    reg_data = regions_detailed[selected_region]
    st.success(f"**Core Mandate for {selected_region}:** {reg_data['Core Mandate']}")
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Constituent Counties")
        for county in reg_data["Counties"]:
            st.markdown(f"- {county}")
    with col_b:
        st.subheader("Industrial Specialization & Focus")
        st.write(reg_data["Industrial Focus"])

# ==========================================
# SECTION 5: NATIONAL VISUALIZED SCORECARDS
# ==========================================
elif app_mode == "Visualized Scorecards & Multi-Dimensional Metrics":
    st.header("5. Visualized National Scorecards & Multi-Dimensional Metrics")
    st.info("""
    Historical observations and future policy targets are shown together for strategic visualization. 
    Future values should not be interpreted as verified historical outcomes.
    """)
    st.subheader("📈 1. Economic Growth Scorecard")
    fig_gdp = px.line(
        df_ingestion, x="Year", y="Real_GDP_Growth_Pct", color="Administration_Horizon",
        markers=True, title="Historical and Kenya 2060 GDP Growth Trajectory", hover_data=["Data_Status"]
    )
    fig_gdp.update_yaxes(ticksuffix="%")
    st.plotly_chart(fig_gdp, use_container_width=True)

    st.subheader("🏭 2. Industrialization Scorecard")
    fig_ind = px.line(
        df_ingestion, x="Year", y="Industrialization_Share_Pct", markers=True,
        title="Industrial Value-Addition Trajectory Toward Kenya 2060", hover_data=["Data_Status"]
    )
    fig_ind.update_yaxes(ticksuffix="%")
    st.plotly_chart(fig_ind, use_container_width=True)

    st.subheader("🌐 3. Human Development Scorecard")
    fig_hdi = px.line(
        df_ingestion, x="Year", y="HDI_Score", markers=True,
        title="Human Development Index Trajectory", hover_data=["Data_Status"]
    )
    st.plotly_chart(fig_hdi, use_container_width=True)

    st.subheader("🌍 4. SDG Framework Scorecard")
    fig_sdg = px.area(
        df_ingestion, x="Year", y="SDG_Composite_Score",
        title="Kenya 2060 Sustainable Development Progress Framework", hover_data=["Data_Status"]
    )
    fig_sdg.update_yaxes(range=[0, 100])
    st.plotly_chart(fig_sdg, use_container_width=True)

# ==========================================
# SECTION 6: PRESIDENTIAL SCORECARDS
# ==========================================
elif app_mode == "Presidential Scorecards & Strategic Horizons (2004-2060)":
    st.header("6. Presidential Performance Scorecards & Strategic Horizons")
    st.write("""
    Each administration is assessed using four development dimensions: **Economic Growth, Industrialization, Human Development and Sustainable Development Progress**. 
    The scorecards are followed directly by graphs, underlying tables and source verification information.
    """)
    st.warning("""
    **Methodology Notice:** Presidential performance cannot be attributed exclusively to one administration because development outcomes 
    are influenced by global conditions, institutions, policies and long-term investments.
    """)
    tab_kibaki, tab_uhuru, tab_ruto, tab_horizons = st.tabs([
        "Mwai Kibaki (2003-2013)",
        "Uhuru Kenyatta (2013-2022)",
        "William Ruto (2022-Present)",
        "Strategic Horizons (2026-2060)"
    ])
    
    with tab_kibaki:
        st.subheader("President Mwai Kibaki Administration")
        st.markdown("""
        **Development Context**
        * Economic recovery and expansion during the Economic Recovery Strategy period.
        * Expansion of education and social services.
        * Launch of Kenya Vision 2030 and investment in infrastructure.
        """)
        kibaki_data = df_ingestion[df_ingestion["Year"].between(2004, 2012)].copy()
        st.markdown("### Presidential Development Scorecard")
        create_presidential_scorecard(kibaki_data, "Mwai Kibaki Administration")
        st.markdown("---")
        st.markdown("## Development Graphs")
        create_presidential_graphs(kibaki_data, "Mwai Kibaki Administration")
        st.markdown("## Underlying Data Table")
        display_scorecard_table(kibaki_data)

    with tab_uhuru:
        st.subheader("President Uhuru Kenyatta Administration")
        st.markdown("""
        **Development Context**
        * Expansion of transport, logistics and energy infrastructure.
        * Consolidation of Kenya's devolved governance system and digital government services.
        """)
        uhuru_data = df_ingestion[df_ingestion["Year"].between(2013, 2022)].copy()
        st.markdown("### Presidential Development Scorecard")
        create_presidential_scorecard(uhuru_data, "Uhuru Kenyatta Administration")
        st.markdown("---")
        st.markdown("## Development Graphs")
        create_presidential_graphs(uhuru_data, "Uhuru Kenyatta Administration")
        st.markdown("## Underlying Data Table")
        display_scorecard_table(uhuru_data)

    with tab_ruto:
        st.subheader("President William Ruto Administration")
        st.markdown("""
        **Development Context**
        * Agricultural productivity and digital transformation initiatives.
        * Financial inclusion, health reforms, and public-private partnerships.
        """)
        ruto_data = df_ingestion[df_ingestion["Year"].between(2023, 2026)].copy()
        st.markdown("### Presidential Development Scorecard")
        create_presidential_scorecard(ruto_data, "William Ruto Administration")
        st.markdown("---")
        st.markdown("## Development Graphs")
        create_presidential_graphs(ruto_data, "William Ruto Administration")
        st.markdown("## Underlying Data Table")
        display_scorecard_table(ruto_data)

    with tab_horizons:
        st.subheader("Kenya 2060 Strategic Development Horizons")
        st.markdown("""
        | Horizon | Period | Strategic Objective |
        |---|---|---|
        | Short-Term | 2026-2030 | Fiscal stabilization and inclusive productivity |
        | Medium-Term | 2030-2045 | Regional industrial integration and human development |
        | Long-Term | 2045-2060 | Knowledge-based and climate-resilient economy |
        """)
        future_data = df_ingestion[df_ingestion["Year"] >= 2030].copy()
        st.warning("""
        **Policy Target Notice:** The following values are Kenya 2060 policy targets or scenario projections. 
        They are not historical observations and should not be used to evaluate past presidential performance.
        """)
        st.markdown("### Strategic Development Targets")
        create_presidential_scorecard(future_data, "Kenya 2060 Strategic Horizons")
        st.markdown("---")
        st.markdown("## Target & Scenario Graphs")
        create_presidential_graphs(future_data, "Kenya 2060 Strategic Horizons")
        st.markdown("## Target & Scenario Data")
        display_scorecard_table(future_data)

    display_validated_sources()

# ==========================================
# SECTION 7: DATA INGESTION & PEER VERIFICATION
# ==========================================
elif app_mode == "Data Ingestion & Peer Verification Portal":
    st.header("7. Data Ingestion & Peer Verification Portal")
    st.write("""
    This portal provides a transparent audit trail for the Kenya 2060 development framework. Stakeholders can inspect the underlying 
    indicators, distinguish historical observations from targets and download the dataset for independent review.
    """)
    selected_status = st.multiselect(
        "Filter by Data Status",
        options=df_ingestion["Data_Status"].unique(),
        default=df_ingestion["Data_Status"].unique()
    )
    filtered_data = df_ingestion[df_ingestion["Data_Status"].isin(selected_status)]
    st.subheader("Kenya 2060 Development Data Registry")
    st.dataframe(filtered_data, use_container_width=True, hide_index=True)

    csv_bytes = filtered_data.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Kenya 2060 Audit Dataset (CSV)",
        data=csv_bytes,
        file_name="kenya_2060_development_audit.csv",
        mime="text/csv",
        help="Download the selected dataset for independent analysis."
    )
    st.markdown("---")
    st.subheader("Data Verification Principles")
    st.markdown("""
    * **Historical data** should be traceable to an official or authoritative source.
    * **Current estimates** should be updated when official releases become available.
    * **Scenario projections** must disclose their underlying assumptions.
    * **Kenya 2060 targets** must never be presented as historical outcomes.
    """)
    display_validated_sources()

# ==========================================
# SECTION 8: INFRASTRUCTURE-TO-INDUSTRY MANDATE
# ==========================================
elif app_mode == "Infrastructure-to-Industry Mandate":
    st.header("8. Infrastructure-to-Industry Co-Investment Mandate")
    st.write("""
    The Kenya 2060 Framework proposes that major infrastructure investment should demonstrate a credible relationship 
    with productive economic activity, industrial demand and sustainable value creation.
    """)
    st.warning("""
    **The Infrastructure Productivity Principle**
    Major infrastructure should be evaluated alongside its connection to industrial growth, private-sector demand, 
    value chains, environmental sustainability and long-term financial viability.
    """)
    st.markdown("""
    ### Kenya 2060 Infrastructure Investment Gate
    Before major infrastructure projects proceed, policymakers should assess:
    1. **Economic Demand:** Is there measurable productive demand?
    2. **Industrial Linkage:** What value chain will the asset support?
    3. **Financial Sustainability:** Are lifecycle costs affordable?
    4. **Environmental Responsibility:** Are climate and environmental risks addressed?
    5. **Public Participation:** Have affected communities been meaningfully engaged?
    6. **Regional Inclusion:** Does the project strengthen equitable development?
    """)
    st.success("""
    **Kenya 2060 Principle:** Infrastructure is not an end in itself. Every major public asset should contribute 
    to productive capacity, employment, resilience or measurable improvements in public welfare.
    """)

# ==========================================
# FOOTER
# ==========================================
st.markdown("---")
st.markdown("""
### Kenya 2060 All-Inclusive Development Framework
*One Kenya. Forty-Seven Contributors. Shared Prosperity.*  
**Data Governance Principle:** Evidence, estimates and aspirations must always be transparently distinguished.
""")
st.caption("Repository maintained under version control. Policy contributions, data corrections and stakeholder review are encouraged.")
