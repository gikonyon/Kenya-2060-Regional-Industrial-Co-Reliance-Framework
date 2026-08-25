import streamlit as str_lit
import pandas as pd
import plotly.express as px

# Page Configuration
str_lit.set_page_config(
    page_title="Kenya 2060 Development Proposal",
    page_icon="🇰🇪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling & Header
str_lit.title("🇰🇪 Kenya 2060 All-Inclusive Development Framework")
str_lit.markdown("### *One Kenya. Forty-Seven Contributors. Shared Prosperity.*")
str_lit.markdown("---")

# Sidebar Navigation
str_lit.sidebar.header("Navigation Menu")
app_mode = str_lit.sidebar.selectbox(
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
    str_lit.header("1. Executive Summary and National Context")
    str_lit.write("""
    Kenya possesses a young population, a strategic geographical location, a devolved system of government, 
    and rich resources. However, economic opportunity, industrial development, and quality public services 
    remain unevenly distributed. 
    
    The **Kenya 2060 All-Inclusive Development Proposal** presents a long-term framework organizing all 47 counties 
    into nine functional economic regions. Moving away from raw-material dependency, the framework anchors 
    itself on domestic value addition, county-based industrial specialization, regional co-reliance, and rigorous 
    public accountability.
    """)
    
    col1, col2, col3 = str_lit.columns(3)
    col1.metric("Functional Regions", "9 Zones", "All 47 Counties")
    col2.metric("Target Initial Jobs", "500,000+", "Direct & Supportive")
    col3.metric("Core Vision Year", "2060", "Mature Innovation Economy")

# --- SECTION 2: CONSTITUTIONAL ALIGNMENT ---
elif app_mode == "Constitutional Alignment & Governance":
    str_lit.header("2. Constitutional Alignment & Bulletproof Governance")
    str_lit.write("""
    To prevent the legal vulnerabilities and court injunctions that have historically stalled major national infrastructure 
    projects, this proposal is explicitly preemptive and compliant with the **Constitution of Kenya (2010)**.
    """)
    
    str_lit.info("💡 **Why projects won't stall in court:** By embedding mandatory public participation at the county level and strict adherence to public finance laws from day one, public trust is secured and legal challenges are eliminated.")
    
    tab1, tab2, tab3 = str_lit.tabs(["Article 10 (Inclusiveness)", "Article 201 (Public Finance)", "Chapter 11 (Devolution)"])
    
    with tab1:
        str_lit.subheader("National Values & Principles (Article 10)")
        str_lit.write("Binds state organs to patriotism, national unity, and social justice. The framework eliminates regional marginalization by assigning clear productive economic mandates to every county.")
        
    with tab2:
        str_lit.subheader("Principles of Public Finance (Article 201)")
        str_lit.write("Mandates prudent, responsible use of public money. Capital expenditure must promote equitable development without creating idle assets or wasteful debt.")
        
    with tab3:
        str_lit.subheader("Objects of Devolution (Articles 174 & 175)")
        str_lit.write("Empowers county governments to drive local economic development and revenue generation rather than relying exclusively on shared revenue transfers.")

# --- SECTION 3: GLOBAL BENCHMARKING ---
elif app_mode == "Global Benchmarking (Morocco & China vs. Kenya)":
    str_lit.header("3. Comparative Growth Models: Learning from Global Success")
    str_lit.write("""
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
    str_lit.dataframe(df_comp, use_container_width=True)

# --- SECTION 4: 9-REGION ARCHITECTURE ---
elif app_mode == "9-Region & 47-County Architecture":
    str_lit.header("4. Nine-Region, Forty-Seven-County Economic Architecture")
    str_lit.write("Every community contributes a specialized economic pillar to the national fabric with dedicated county inputs:")
    
    regions_detailed = {
        "Nairobi Region": {
            "Counties": ["Nairobi City"],
            "Core Mandate": "Financial, technology, AI, big data, and diplomatic headquarters.",
            "Industrial Focus": "Fintech hubs, software engineering parks, digital service delivery, global business process outsourcing (BPO), and capital markets."
        },
        "Central Region": {
            "Counties": ["Kiambu", "Murang'a", "Nyeri", "Kirinyaga", "Nyandarua"],
            "Core Mandate": "Coffee/tea processing, blending, and high-value agro-exports.",
            "Industrial Focus": "Value-addition factories for coffee/tea packaging, horticulture cold chains, leather processing, and light manufacturing clusters."
        },
        "Western Region": {
            "Counties": ["Kakamega", "Vihiga", "Bungoma", "Busia"],
            "Core Mandate": "Sugar processing, agro-processing, and cross-border supply chain integration.",
            "Industrial Focus": "Sugar mill modernization, cogeneration of power from bagasse, grain milling, and cross-border trade facilitation."
        },
        "Nyanza Region": {
            "Counties": ["Kisumu", "Siaya", "Homa Bay", "Migori", "Kisii", "Nyamira"],
            "Core Mandate": "Lake logistics, port/SEZ development, fisheries, and regional trade.",
            "Industrial Focus": "Inland port logistics at Kisumu, fish processing plants, cotton ginneries revival, and aquaculture zones."
        },
        "North Rift Region": {
            "Counties": ["Uasin Gishu", "Trans Nzoia", "Nandi", "Elgeyo Marakwet", "West Pokot", "Turkana"],
            "Core Mandate": "National food security, grain production, livestock, and transport corridors.",
            "Industrial Focus": "Grain silos and bulk handling facilities, agricultural machinery assembly, renewable energy development (geothermal/wind), and oil/mineral logistics."
        },
        "South Rift Region": {
            "Counties": ["Nakuru", "Kericho", "Bomet", "Narok", "Kajiado"],
            "Core Mandate": "Tea, dairy, tourism, and integrated livestock value chains.",
            "Industrial Focus": "Dairy processing hubs, geothermal-powered industrial parks (Naivasha SEZ), high-end eco-tourism infrastructure, and leather value chains."
        },
        "Eastern Region": {
            "Counties": ["Machakos", "Kitui", "Makueni", "Embu", "Meru", "Tharaka Nithi", "Isiolo"],
            "Core Mandate": "Dryland innovation, livestock, agro-processing, and gateway infrastructure.",
            "Industrial Focus": "Mango and citrus processing plants, Isiolo resort city logistics hub, leather and meat processing, and green energy solar parks."
        },
        "North Eastern Region": {
            "Counties": ["Garissa", "Wajir", "Mandera"],
            "Core Mandate": "Cross-border livestock commerce and integrated trade logistics.",
            "Industrial Focus": "Modern export-oriented abattoirs, hides and skins tanneries, solar energy generation, and livestock disease-free zones."
        },
        "Coast Region": {
            "Counties": ["Mombasa", "Kwale", "Kilifi", "Tana River", "Lamu", "Taita Taveta"],
            "Core Mandate": "Maritime gateway, ports, logistics, and international trade corridors.",
            "Industrial Focus": "Port of Mombasa and Lamu Port (LAPSSET) corridor logistics, ship repair yards, maritime fisheries processing, and coastal tourism modernization."
        }
    }
    
    selected_region = str_lit.selectbox("Select Economic Region to Inspect", list(regions_detailed.keys()))
    
    reg_data = regions_detailed[selected_region]
    
    str_lit.success(f"**Core Mandate for {selected_region}**: {reg_data['Core Mandate']}")
    
    col_a, col_b = str_lit.columns(2)
    with col_a:
        str_lit.subheader("🏛️ Constituent Counties")
        for county in reg_data["Counties"]:
            str_lit.markdown(f"- {county}")
            
    with col_b:
        str_lit.subheader("🏭 Industrial Specialization & Focus")
        str_lit.write(reg_data["Industrial Focus"])

# --- SECTION 5: INFRASTRUCTURE MANDATE ---
elif app_mode == "Infrastructure-to-Industry Mandate":
    str_lit.header("5. Infrastructure-to-Industry Co-Investment Mandate")
    str_lit.write("""
    To ensure public resources are never wasted on idle assets (avoiding historical mistakes seen in uncoordinated global projects), 
    the proposal mandates strict interlinkage:
    """)
    
    str_lit.warning("""
    🛑 **The Anti-Waste Rule:** 
    Drawing from Morocco's Tanger Med model, all major infrastructure (rail, ports, special economic zones) 
    must be strictly interlinked with pre-committed industrial growth, private sector demand, and active value-chains before ground breaks.
    """)
    
    str_lit.markdown("""
    * **No Speculative Civil Works:** Capital expenditure must unlock measurable, localized productive capacity.
    * **Constitutional Compliance:** Direct fulfillment of Article 201 mandates for prudent and responsible management of public funds.
    """)

# Footer
str_lit.markdown("---")
str_lit.markdown("*Repository maintained under Git version control. Contributions and policy pull requests open for stakeholders.*")
