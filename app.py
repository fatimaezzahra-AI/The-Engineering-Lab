import os
import streamlit as st
from streamlit_option_menu import option_menu

# ----------------------------------------------------------------------
# Links (single source of truth)
# ----------------------------------------------------------------------
GITHUB = "https://github.com/fatimaezzahra-AI"
LINKEDIN = "https://www.linkedin.com/in/fatima-ezzahra-boukhorssa-09aa9a259"
EMAIL = "fatimaezzahraboukhorssa@gmail.com"
CV_EN = "assets/CV_Fatima_Ezzahra_Boukhorssa_EN .pdf"
CV_FR = "assets/CV_Fatima_Ezzahra_Boukhorssa_FR.pdf"

# 1. Page settings
st.set_page_config(page_title="Fatima-Ezzahra | Data & AI Portfolio", layout="wide")
st.markdown(
    """
    <style>
    .stApp { background-color: #0E1117; color: #FAFAFA; }
    .card {
        background: #1E1E24; border-left: 4px solid #FF4B4B;
        padding: 12px 16px; border-radius: 8px; margin-bottom: 10px;
        color: #FAFAFA; line-height: 1.5;
    }
    .card b { color: #FF8A8A; }
    .badge {
        display: inline-block; background: #FF4B4B22; color: #FF8A8A;
        border: 1px solid #FF4B4B; border-radius: 999px;
        padding: 3px 12px; font-size: 0.85rem; margin-bottom: 8px;
    }
    /* Download buttons: dark text on white background */
    .stApp button p,
    .stApp button span,
    .stApp [data-testid="stDownloadButton"] button * {
        color: #0E1117 !important;
    }
    .stApp [data-testid="stDownloadButton"] button {
        background-color: #FFFFFF !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def card(text: str):
    st.markdown(f'<div class="card">{text}</div>', unsafe_allow_html=True)


# 2. Hero
st.markdown('<span class="badge">Open to a 6-month end-of-studies internship, starting 2027</span>',
            unsafe_allow_html=True)
st.title("Applied Mathematics & AI")
st.write(
    "Master's student building end-to-end data & AI projects: "
    "RAG systems evaluated with RAGAS, ML pipelines on millions of records, "
    "A/B testing and predictive modeling. "
    "Looking for opportunities in Data Science, Machine Learning and Generative AI."
)

c1, c2, c3, c4, _ = st.columns([1, 1, 1.3, 1.3, 3])
with c1:
    st.link_button("GitHub", GITHUB)
with c2:
    st.link_button("LinkedIn", LINKEDIN)
with c3:
    if os.path.exists(CV_EN):
        with open(CV_EN, "rb") as f:
            st.download_button("Download CV (EN)", f, file_name="CV_Fatima_Ezzahra_Boukhorssa_EN.pdf",
                               mime="application/pdf")
with c4:
    if os.path.exists(CV_FR):
        with open(CV_FR, "rb") as f:
            st.download_button("Télécharger CV (FR)", f, file_name="CV_Fatima_Ezzahra_Boukhorssa_FR.pdf",
                               mime="application/pdf")
st.markdown("---")

# 3. Navigation
selected = option_menu(
    menu_title=None,
    options=["About", "Projects", "Contact"],
    icons=["person", "code-slash", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#1E1E24"},
        "icon": {"color": "#FF4B4B", "font-size": "16px"},
        "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px",
                     "--hover-color": "#2D2D34"},
        "nav-link-selected": {"background-color": "#FF4B4B"},
    },
)

# 4. Pages
if selected == "About":
    st.markdown("### I am Fatima-Ezzahra Boukhorssa")
    col1, col2 = st.columns([2, 1], gap="large")
    with col1:
        st.subheader("Bridging Applied Mathematics and AI")
        st.write(
            """
I am a Master's student in Applied Mathematics for AI (Mohammed First University, Nador),
with a strong foundation in statistical modeling, predictive analytics and algorithm design.

My work spans forecasting business trends, analyzing large-scale datasets, and building
interactive tools that turn raw data into actionable insights, from sales forecasting to
risk analytics on real-world data. I have also applied data-driven thinking to embedded
systems and signal processing.

I'm driven by the intersection of rigorous mathematics and practical impact: building models
and tools that are not just accurate, but usable and meaningful for real decision-making.
            """
        )
        st.markdown("#### My Core Skills")
        card("<b>Machine Learning & Predictive Modeling:</b> Scikit-Learn (Random Forest), "
             "statistical modeling, feature engineering, model evaluation.")
        card("<b>Generative AI & RAG:</b> hybrid retrieval (BM25 + Qdrant), cross-encoder "
             "re-ranking, LLMs on Groq, automated evaluation with RAGAS.")
        card("<b>Data Analysis & Visualization:</b> Python, Pandas, SQL, Plotly, Streamlit, "
             "Power BI. Interactive dashboards from raw data to insights.")
        card("<b>Embedded Systems:</b> Arduino/ESP32, real-time data acquisition.")
    with col2:
        if os.path.exists("assets/maphoto.png"):
            st.image("assets/maphoto.png", width=250)

elif selected == "Projects":
    st.markdown("### Technical Project Portfolio")
    st.write("Select a category below to explore my work.")

    tab_ai, tab_data, tab_iot = st.tabs(["Artificial Intelligence",
                                         "Data Science & Analytics",
                                         "IoT & Robotics"])

    with tab_ai:
        st.markdown("#### Generative AI & RAG")
        with st.expander("Project: Enterprise RAG, hybrid retrieval, re-ranking & RAGAS evaluation",
                         expanded=True):
            st.write(
                """
A Retrieval-Augmented Generation pipeline over company documents: **BM25 + Qdrant** hybrid
search, **cross-encoder re-ranking**, answer generation with an LLM on **Groq**, and
automated evaluation with **RAGAS** (Faithfulness, Answer Relevancy, Context Precision).

**Stack:** Python, Qdrant, rank_bm25, Sentence-Transformers, Groq, RAGAS
                """
            )
            st.link_button("View GitHub Repository", f"{GITHUB}/enterprise-rag")

        st.markdown("#### Machine Learning & Predictive Analytics")
        with st.expander("Project: Superstore Sales Forecasting & Predictive AI", expanded=False):
            st.write(
                """
An end-to-end Machine Learning web application built with **Python**, **Scikit-Learn**,
**Plotly** and **Streamlit**. Interactive predictive models to forecast sales trends,
analyze profit margins and deliver actionable insights.
                """
            )
            st.link_button("Launch AI Predictive App",
                           "https://superstore-sales-analysis-ai5nzfwgv9n5ebzndbbhvl.streamlit.app/")
            st.link_button("View GitHub Repository", f"{GITHUB}/superstore-sales-analysis")

        with st.expander("Project: Schengen Border Analytics & Risk Forecasting", expanded=False):
            st.write(
                """
An interactive data analytics & ML dashboard analyzing European border crossing trends,
detection patterns and risk indicators on **5M+ Frontex records**, using **Python**,
**Pandas**, **Scikit-Learn**, **Plotly** and **Streamlit**.
                """
            )
            st.link_button("Launch Migration Risk App",
                           "https://schengen-border-analytics-korxhmjapzyyrktbbzxpf4.streamlit.app/")
            st.link_button("View GitHub Repository", f"{GITHUB}/schengen-border-analytics")

    with tab_data:
        st.markdown("#### Statistics & Analytics")
        with st.expander("Project: Inferential A/B Testing Lab", expanded=True):
            st.write("Interactive web application for inferential statistical analysis, "
                     "hypothesis testing (Z-test) and A/B test evaluation.")
            st.link_button("Open Live App",
                           "https://inferential-ab-testing-lab-ghkzgswwphrktjdd8ici2z.streamlit.app/")
            st.link_button("View GitHub Repository", f"{GITHUB}/inferential-ab-testing")

    with tab_iot:
        st.markdown("#### Smart Systems & Embedded Automation")
        st.info("Projects in this section are currently under development.")

elif selected == "Contact":
    st.markdown("### Get In Touch")
    st.write("I am open to discussing Data Science / AI internship opportunities "
             "and collaborations.")
    st.markdown("#### Professional Channels")
    card(f"<b>Email:</b> <a href='mailto:{EMAIL}' style='color:#FF8A8A'>{EMAIL}</a>")
    card(f"<b>LinkedIn:</b> <a href='{LINKEDIN}' style='color:#FF8A8A'>Fatima-Ezzahra Boukhorssa</a>")
    card(f"<b>GitHub:</b> <a href='{GITHUB}' style='color:#FF8A8A'>github.com/fatimaezzahra-AI</a>")
    st.markdown("---")
    st.caption("Designed with precision, bridging Mathematics and Machine Intelligence.")
