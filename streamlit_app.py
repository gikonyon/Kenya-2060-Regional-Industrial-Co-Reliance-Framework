import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="Kenya 2060 Development Proposal",
    page_icon="🇰🇪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling & Header
st.title("🇰🇪 Kenya 2060 All-Inclusive Development Framework")
st.markdown("### *One Kenya. Forty-Seven Contributors. Shared Prosperity.*")
st.markdown("---")

# Sidebar Navigation
st.sidebar.header("Navigation Menu")
app_mode = st.sidebar.selectbox(
    "Choose Section",
    [
        "Executive Summary & Vision",
        "Constitutional Alignment & Governance",
        "Global Benchmarking (Morocco & China vs. Kenya)",
        "9-Region & 47-County Architecture",
        "Infrastructure-to-Industry Mandate"
    ]
)

# --- SECTION 1: EXECUTIVE SUMMARY ---
if app_mode == "Executive Summary & Vision":
    st.header("1. Executive Summary and National Context")
    st.write("""
    Kenya possesses a young population, a strategic geographical location, a devolved system of government, 
    and rich resources. However, economic opportunity, industrial development, and quality public services 
    remain unevenly distributed. 
    
    The **Kenya 2060 All-Inclusive Development Proposal** presents a long-term framework organizing all 47 counties 
    into nine functional economic regions. Moving away from raw-material dependency, the framework anchors 
    itself on domestic value addition, county-based industrial specialization, regional co-reliance, and rigorous 
    public accountability.
    """)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Functional Regions", "9 Zones", "All 47 Counties")
    col2.metric("Target Initial Jobs", "500,000+", "Direct & Supportive")
    col3.metric("Core Vision Year", "2060", "Mature Innovation Economy")

# --- SECTION 2: CONSTITUTIONAL ALIGNMENT ---
elif app_mode == "Constitutional Alignment & Governance":
    st.header("2. Constitutional Alignment & Bulletproof Governance")
    st.write("""
    To prevent the legal vulnerabilities and court injunctions that have historically stalled major national infrastructure 
    projects, this proposal is explicitly preemptive and compliant with the **Constitution of Kenya (2010)**.
    """)
    
    st.info("💡 **Why projects won't stall in court:** By embedding mandatory public participation at the county level and strict adherence to public finance laws from day one, public trust is secured and legal challenges are eliminated.")
    
    tab1, tab2, tab3 = st.tabs(["Article 10 (Inclusiveness)", "Article 201 (Public Finance)", "Chapter 11 (Devolution)"])
    
    with tab1:
        st.subheader("National Values & Principles (Article 10)")
        st.write("Binds state organs to patriotism, national unity, and social justice. The framework eliminates regional marginalization by assigning clear productive economic mandates to every county.")
        
    with tab2:
        st.subheader("Principles of Public Finance (Article 201)")
        st.write("Mandates prudent, responsible use of public money. Capital expenditure must promote equitable development without creating idle assets or wasteful debt.")
        
    with tab3:
        st.subheader("Objects of Devolution (Articles 174 & 175)")
        st.write("Empowers county governments to drive local economic development and revenue generation rather than relying exclusively on shared revenue transfers.")

# --- SECTION 3: GLOBAL BENCHMARKING ---
elif app_mode == "Global Benchmarking (Morocco & China vs. Kenya)":
    st.header("3. Comparative Growth Models: Learning from Global Success")
    st.write("""
    The framework borrows structural lessons from **Morocco (Tanger Med Integration)** and **China (Export-Led Growth & Spatial Sequencing)**, 
    integrated directly with national infrastructure and asset monetization visions.
    """)
    
    comparison_data = {
        "Strategic Dimension": [
            "Infrastructure Philosophy",
            "Spatial & Regional Sequencing",
            "Legal & Governance Protection",
            "Industrial Integration"
        ],
        "China Model": [
            "Massive capital into transport and SEZs tied to global supply chains.",
            "Gradient Theory ('Flying Geese') cascading investment from coast inward.",
            "Top-down unitary execution with minimal judicial friction.",
            "Strict coupling of infrastructure to manufacturing."
        ],
        "Morocco (Tanger Med)": [
            "Mega-ports interlinked directly with free-zone industrial platforms.",
            "Targeted maritime gateways scaled outward to regional plans.",
            "Royal long-term strategy backed by autonomous specialized agencies.",
            "High integration rates (e.g., automotive/aerospace clusters)."
        ],
        "Kenya 2060 Proposal": [
            "**Infrastructure-to-Industry Mandate**: Outlaws standalone civil works.",
            "**9-Region Architecture**: Simultaneous county specialization from day one.",
            "**Constitutional Anchoring**: Preempts court delays via Article 10 & public participation.",
            "**Pre-committed Offtake**: Every shilling unlocks measurable export readiness."
        ]
    }
    
    df_comp = pd.DataFrame(comparison_data)
    st.dataframe(df_comp, use_container_width=True)

# --- SECTION 4: 9-REGION ARCHITECTURE ---
elif app_mode == "9-Region & 47-County Architecture":
    st.header("4. Nine-Region, Forty-Seven-County Economic Architecture")
    st.write("Every community contributes a specialized economic pillar to the national fabric:")
    
    regions = {
        "Nairobi Region": "Financial, technology, AI, big data, and diplomatic headquarters.",
        "Central Region": "Coffee/tea processing, blending, and high-value agro-exports.",
        "Western Region": "Sugar processing, agro-processing, and cross-border supply chain integration.",
        "Nyanza Region": "Lake logistics, port/SEZ development, fisheries, and regional trade.",
        "North Rift Region": "National food security, grain production, livestock, and transport corridors.",
        "South Rift Region": "Tea, dairy, tourism, and integrated livestock value chains.",
        "Eastern Region": "Dryland innovation, livestock, agro-processing, and gateway infrastructure.",
        "North Eastern Region": "Cross-border livestock commerce and integrated trade logistics.",
        "Coast Region": "Maritime gateway, ports, logistics, and international trade corridors."
    }
    
    selected_region = st.selectbox("Select Economic Region to Inspect", list(regions.keys()))
    st.success(f"**Core Mandate for {selected_region}**: {regions[selected_region]}")

# --- SECTION 5: INFRASTRUCTURE MANDATE ---
elif app_mode == "Infrastructure-to-Industry Mandate":
    st.header("5. Infrastructure-to-Industry Co-Investment Mandate")
    st.write("""
    To ensure public resources are never wasted on idle assets (avoiding historical mistakes seen in uncoordinated global projects), 
    the proposal mandates strict interlinkage:
    """)
    
    st.warning("""
    🛑 **The Anti-Waste Rule:** 
    Drawing from Morocco's Tanger Med model, all major infrastructure (rail, ports, special economic zones) 
    must be strictly interlinked with pre-committed industrial growth, private sector demand, and active value-chains before ground breaks.
    """)
    
    st.markdown("""
    * **No Speculative Civil Works:** Capital expenditure must unlock measurable, localized productive capacity.
    * **Constitutional Compliance:** Direct fulfillment of Article 201 mandates for prudent and responsible management of public funds.
    """)

# Footer
st.markdown("---")
st.markdown("*Repository maintained under Git version control. Contributions and policy pull requests open for stakeholders.*")
