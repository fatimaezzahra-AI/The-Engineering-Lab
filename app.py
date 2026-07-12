import streamlit as st
from streamlit_option_menu import option_menu

# 1. Page Settings (Dark mode layout)
st.set_page_config(
    page_title="Fatima-Ezzahra | Data Portfolio", 
    page_icon="📊", 
    layout="wide"
)

st.markdown("##### Welcome to my Professional Space")
st.title("Applied Mathematics & Machine Intelligence")
st.write("""
Welcome to my world, where mathematical theory meets machine intelligence. 
As a Master's student, I leverage advanced algorithms and statistical modeling to solve complex problems, 
while applying these frameworks to extract actionable Business Insights through Data Analytics.
""")
st.markdown("[Explore My GitHub](https://github.com) | [Connect On LinkedIn](https://linkedin.com)")
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
        st.subheader("Data Analyst & SQL Specialist")
        st.write("""
        I am a diligent and enthusiastic data specialist with a strong foundational background 
        in Relational Databases (SQL), Advanced Data Aggregations, and Business Intelligence dashboards.
        My primary focus is on decoding complex relational architectures into business insights.
        """)
        st.markdown("#### Current Focus:")
        st.success("⚡ Advanced SQL Joins & Business Logic Modeling")
        st.success("📊 Interactive Web Analytics Dashboards")
        
    with col2:
        # A nice developer illustration placeholder
        st.image("https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=500", width=250)

elif selected == "Projects":
    st.markdown("### 💼 Selected Analytics Projects")
    st.write("Here you will find my production-ready SQL and Data Analytics solutions.")
    
    # Placeholder container for the SQL project we prepared earlier
    with st.expander("🚀 Project 1: Infrastructure Resource Allocation (SQL)"):
        st.write("Click to see the business case, queries, and insights using `LEFT JOIN` and data filters.")
        # Here we will inject our SQL code on the next step!

elif selected == "Contact":
    st.markdown("### ✉️ Let's Connect")
    st.write("Feel free to reach out for internship opportunities, project collaborations, or data-related inquiries.")
    
    st.markdown("- **Email:** fati.ezzahra.boukhorssa@gmail.com")
    st.markdown("- **GitHub:** github.com/yourprofile")
