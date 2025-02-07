#!/usr/bin/env python
# coding: utf-8

# In[7]:


import streamlit as st
import pandas as pd
import time
import plotly.express as px
import matplotlib.pyplot as plt

# Set page config with dark theme
st.set_page_config(page_title='Akash Pathak | Portfolio', layout='wide')

st.markdown("""
    <style>
        body {background-color: #000000; color: grey;}
        .stTitle {color: #FFD700; font-size: 28px; font-weight: bold; animation: fadeIn 2s;}
        .stSidebar {background-color: #1E1E1E; color: white;}
        .stButton>button {background-color: #FFD700; color: black;}
        .stHeader {color: #FFD700; font-size: 24px; font-weight: bold;}
        .stSection {background-color: #1E1E1E; padding: 15px; border-radius: 10px; margin-bottom: 20px; color: grey;}
        .stNav {color: red; font-size: 20px; font-weight: bold;}
        .stText {color: grey;}
        .stSidebar .radio {color: white;}
        .nav-container {background-color: #000000; padding: 10px; border-radius: 10px;}
        .stSidebar .stRadio label {color: white !important;}
        .stSidebar .stRadio div {color: white !important;}
        .stContent {color: grey;}
        @keyframes fadeIn {from {opacity: 0;} to {opacity: 1;}}
    </style>
""", unsafe_allow_html=True)

# Animated Loading
with st.spinner('Loading Portfolio...'):
    time.sleep(1)

# Sidebar Navigation
st.sidebar.markdown("<h2 class='stNav'>Navigation</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color:white;'>Go to</p>", unsafe_allow_html=True)
page = st.sidebar.radio("", ["Home", "Education", "Internships", "Projects", "Skills", "Certifications", "Contact"], index=0)

# Home Page
if page == "Home":
    st.title("👋 Hi, I'm Akash Pathak")
    st.write("### Data Scientist | Machine Learning Engineer | Data Analyst")
    st.write("#### Passionate about AI, Data Science, and solving real-world problems.")
    st.write("📍 From Chhatapur, India")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/akash-pathak-44a082212) | [GitHub](https://github.com/akash0123-pride)")
    st.markdown(
        "<h3 style='color: #FFD700; font-weight: bold;'>📄 <a href='https://drive.google.com/file/d/1zfMTKiAvqE5uA0tvJwtWZOinsdrkwSAw/view?usp=sharing' target='_blank' style='color: #FFD700; text-decoration: none;'>Resume</a></h3>",
        unsafe_allow_html=True
    )


# Education Section
elif page == "Education":
    st.title("🎓 Education")
    st.write("### Bachelor's of Technology in Computer Science Enginnering-Data Science")
    st.write("Oriental Institute of Science and Technology, Bhopal (2020 - 2024)")
    st.write("CGPA: 8.32")
    st.write("### Intermediate")
    st.write("Maharishi Vidya Mandir, Jabalpur - 69.2%")
    st.write("### High School")
    st.write("Maharishi Vidya Mandir, Jabalpur - CGPA: 9.4")

# Internship Section
elif page == "Internships":
    st.title("💼 Internships")
    internships = {
        "Delhi Metro Rail Corporation": "Worked on data wrangling, slicing, cleaning, and translation. Dealt with missing data and outlier treatment for impact analysis.",
        "IBM SkillsBuild": "Built a machine learning model to predict whether a patient should be treated for mental illness. Used Random Forest for prediction and deployed it."
    }
    for company, desc in internships.items():
        st.write(f"### {company}")
        st.write(f"{desc}")
        st.write("---")

# Projects Section
elif page == "Projects":
    st.title("🚀 Projects")
    projects = [
        {"name": "Penguin Classification", "desc": "Developed a ML model to classify penguin species using Streamlit and scikit-learn."},
        {"name": "Lung Disease Detection", "desc": "Implemented a deep learning model using ResNet and TensorFlow to detect lung diseases from X-ray images."},
        {"name": "Mental Health Tracker", "desc": "Designed a mental health tracking application that analyzes user responses and provides insights."},
        {"name": "Image-to-Text Model", "desc": "Developed an OCR-based model to extract text from images, including doctors' handwriting, using Tesseract and deep learning."},
        {"name": "Indian Crime Data Analysis Dashboard", "desc": "Built an interactive dashboard using Python and Streamlit to analyze crime trends in India."},
        {"name": "Driver Drowsiness Detection", "desc": "Implemented a system using OpenCV and machine learning to detect drowsiness in drivers and alert them."}
    ]
    for proj in projects:
        st.write(f"### {proj['name']}")
        st.write(proj['desc'])
        st.write("---")

# Skills Section with Graph
elif page == "Skills":
    st.title("📊 Skills")
    skills = {"Python": 90, "Machine Learning": 80, "SQL": 90, "Data Analytics": 85, "AWS": 75, "Tableau": 85}
    df = pd.DataFrame(list(skills.items()), columns=["Skill", "Proficiency"])
    fig = px.bar(df, x='Proficiency', y='Skill', orientation='h', color='Proficiency', color_continuous_scale='Blues',range_color=[65, max(df["Proficiency"])])
    st.plotly_chart(fig, use_container_width=True)

# Certifications Section
elif page == "Certifications":
    st.title("📜 Certifications")
    certs = [
        "Data Science A-Z (Udemy)", "Machine Learning with Python (FreeCodeCamp)", 
        "Data Analysis Using Python Issued (IBM)","Python for Data Science (IBM)", "Python for Data Science & ML (Udemy)"
    ]
    for cert in certs:
        st.write(f"✅ {cert}")

# Contact Section
elif page == "Contact":
    st.title("📞 Contact")
    st.write("**Email:** akash.pathak0123@gmail.com")
    st.write("**Phone:** +91 7024426415")
    st.write("**GitHub:** [GitHub Profile](https://github.com/akash0123-pride)")
    st.write("**LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/akash-pathak-44a082212)")


# In[ ]:





# In[ ]:




