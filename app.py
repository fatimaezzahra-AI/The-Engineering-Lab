import streamlit as st
from streamlit_option_menu import option_menu

# 1. Page Settings (Dark mode layout)
st.set_page_config(
    page_title="Fatima-Ezzahra | Data Portfolio", 
    layout="wide"
)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("##### Welcome to my Professional Space")
st.title("Applied Mathematics & Machine Intelligence")
st.write("""
Welcome to my world, where mathematical theory meets machine intelligence. 
As a Master's student, I leverage advanced algorithms and statistical modeling to solve complex problems, 
while applying these frameworks to extract actionable Business Insights through Data Analytics.
""")
st.markdown("[Explore My GitHub](https://github.com/fatimaezzahra-AI) | (https://www.linkedin.com/in/Fatima_ezzahra_Boukhorssa)")
st.markdown("---")

# 3. The Professional Navigation Bar (The Horizontal Cadre from your image)
# This creates the exact exact buttons styled beautifully in the center
selected = option_menu(
    menu_title=None, # No title needed on top
    options=["About", "Projects", "Contact"], # The tabs
    icons=["person", "code-slash", "envelope"], # The icons next to text
    menu_icon="cast", 
    default_index=0, 
    orientation="horizontal", # Horizontal orientation like the screen
    styles={
        "container": {"padding": "0!important", "background-color": "#1E1E24"},
        "icon": {"color": "#FF4B4B", "font-size": "16px"}, 
        "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "--hover-color": "#2D2D34"},
        "nav-link-selected": {"background-color": "#FF4B4B"}, # Color when selected (Red/Coral like the screen)
    }
)

# 4. Content routing based on the selected Tab
if selected == "About":
    st.markdown("### I am Fatima-Ezzahra Boukhorssa")
    
    col1, col2 = st.columns([2, 1], gap="large")
    with col1:
        st.subheader("Bridging Applied Mathematics, AI, and Autonomous Systems")
        st.write("""
        I am a Data and Machine Learning professional driven by a unique combination of **analytical rigor and right-brain creativity**. 
        While my Master's degree in Applied Mathematics provides me with a strong foundation in complex logic and algorithmic design, 
        my high visual intelligence motivates me to look beyond just raw code.
        
        I actively bridge the gap between theoretical AI and the physical world by exploring **Robotics, IoT, and intuitive application development**. 
        I thrive f-the intersections where mathematical models power smart, automated, and human-centric systems.
        """)
        
        st.markdown("####  My Multi-Dimensional Core:")
        st.success(" **The Analytical Core:** Applied Mathematics, Machine Learning, and Predictive Modeling.")
        st.success(" **The Creative Exploration:** IoT, Robotics, and Real-time Smart System Automation.")
        st.success(" **The Data Layer:** Advanced SQL, Relational Architecture, and Business Intelligence.")
        
    with col2:

        st.image("https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=500", width=250)

elif selected == "Projects":
    st.markdown("###  Technical Project Portfolio")
    st.write("Welcome to my project hub. Select a category below to explore my solutions.")
    
   
    tab_ai, tab_data, tab_iot = st.tabs([" Artificial Intelligence", " Data Analytics (SQL)", " IoT & Robotics"])
    
   # AI Tab
    with tab_ai:
        st.markdown("#### Machine Learning & Predictive Analytics")
        with st.expander(" Project: Superstore Sales Forecasting & Predictive AI", expanded=True):
            st.write("""
            An end-to-end Machine Learning web application built with **Python**, **Scikit-Learn**, **Plotly**, and **Streamlit**.
            It features interactive predictive models to forecast sales trends, analyze profit margins, and deliver actionable insights.
            """)
            st.link_button(" Launch AI Predictive App", "https://superstore-sales-analysis-ai5nzfwgv9n5ebzndbbhvl.streamlit.app/")
            st.link_button(" View GitHub Repository", "https://github.com/fatimaezzahra-AI/superstore-sales-analysis") 
            # Frontex & Schengen Migration Project
        with st.expander(" Project: Schengen Border Analytics & Risk Forecasting", expanded=True):
            st.write("""
            An interactive data analytics & ML dashboard analyzing European border crossing trends, detection patterns, and risk indicators using **Python**, **Pandas**, **Plotly**, and **Streamlit**.
            """)

            st.link_button(" Launch Migration Risk App", "https://schengen-border-analytics-korxhmjapzyyrktbbzxpf4.streamlit.app/")
        
            st.link_button(" View GitHub Repository", "https://github.com/fatimaezzahra-AI/schengen-border-analytics")
  # Data Analytics Tab
    with tab_data:
         st.markdown("#### Database Engineering & Data Analytics")
    
    #  Inferential A/B Testing Lab
         st.markdown("#####  Inferential A/B Testing Lab")
         st.write(
        "Interactive web application for conducting inferential statistical analysis, "
        "hypothesis testing, and A/B test evaluation."
    )
    
    # 
          st.link_button(" Open Live App", "https://inferential-ab-testing-lab-ghkzgswwphrktjdd8ici2z.streamlit.app/"
          st.link_button(" View GitHub Repository", "https://github.com/fatimaezzahra-AI/inferential-ab-testing")
    )
    # IoT & Robotics Tab
    with tab_iot:
        st.markdown("#### Smart Systems & Embedded Automation")
        st.info(" *Projects in this section are currently under development. Stay tuned!*")
elif selected == "Contact":
    st.markdown("### Get In Touch")
    st.write("I am always open to discussing new projects, Data Science / AI opportunities, or potential collaborations.")
    
    # 
    st.markdown("####  Professional Channels:")
    
    #  
    st.info(" **Professional Email:** fatimaezzahraboukhorssa@gmail.com")
    st.info(" **LinkedIn Profile:** [linkedin.com/in/fatima-ezzahra-boukhorssa](https://linkedin.com)")
    st.info(" **GitHub Repository:** [github.com/fatimaezzahra-AI](https://github.com)")
    
    st.markdown("---")
    st.caption(" Designed with precision, bridging Mathematics and Machine Intelligence.")
