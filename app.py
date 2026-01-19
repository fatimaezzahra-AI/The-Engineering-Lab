import streamlit as st

# 1. Page Config (t-y-biyyeni l-icon o s-smiya f l-browser tab)
st.set_page_config(page_title="Fatima ezzahra Boukhorssa | AI Lab", page_icon="🤖", layout="wide")

# 2. Custom CSS bach n-zido l-jamaliya
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stHeading h1 {
        color: #ff4b4b;
        font-size: 3rem;
    }
    .project-card {
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #4b4b4b;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/6134/6134346.png", width=100) # T-swira sghira
    st.title("Navigation")
    selection = st.radio("Go to:", ["🏠 Home", "🚀 My Projects", "📩 Contact Me"])

if selection == "🏠 Home":
    # Columns bach t-koun l-wajha wa3ra
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title("The Engineering Lab 🚀")
        st.subheader("Hi, I'm Fatima-Ezzahra Boukhorssa")
        st.write("I am an **Aspiring AI Engineer** dedicated to building scalable solutions and interactive data stories.")
        st.markdown("---")
        st.write("### ✨ Current Focus:")
        st.write("✅ **Building Scalable AI Applications**")
        st.write("✅ **Data Engineering & Analysis**")
        st.write("✅ **Interactive Web Dashboards**")

    with col2:
        # Hna t-qdri t-diri t-swira dialek f l-mustaqbal
        st.image("https://img.freepik.com/free-vector/ai-technology-concept-illustration_114360-10020.jpg", caption="AI Innovation")

elif selection == "🚀 My Projects":
    st.title("My AI Portfolio")
    st.write("Explore my latest technical projects:")
    
    # Project Cards
    with st.container():
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.subheader("Project 1: Name & AI Analyzer")
        st.write("A tool that uses Streamlit to analyze text inputs in real-time.")
        if st.button("Open Project 1"):
            st.info("Check the 'pages' menu in the sidebar for the full demo!")
        st.markdown('</div>', unsafe_allow_html=True)

elif selection == "📩 Contact Me":
    st.title("Get In Touch")
    st.write("Let's connect on LinkedIn or GitHub!")
    st.write("[LinkedIn](https://www.linkedin.com/in/your-profile) | [GitHub](https://github.com/fatimaezzahra-ai)")