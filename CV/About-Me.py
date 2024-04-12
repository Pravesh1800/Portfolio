import streamlit as st


# Setting the page configarations
st.set_page_config(page_title="About-Me", page_icon="👨", layout="wide", initial_sidebar_state="expanded")

st.sidebar.markdown('## Navigation Bar')


# Adding the basic info about me nd the Display Pic
dp, details = st.columns(2)
dp.image("CV/profile-pic.png",width=270)

with details:
    st.title('Pravesh Singh')
    st.write("A Quick learning individual looking for a potential chance to work in the Machine Learning space")
    pdf_data = "CV/CV.pdf"
    st.download_button(
        label="📄Download Resume", 
        data=pdf_data, 
        file_name="Pravesh's-Resume.pdf", 
        mime="application/pdf"
    )
    email_style = """
    <style>
    .email-text {
        color: white; /* Initial color */
        font-weight: bold; /* Initial font weight */
    }
    
    .email-text a:hover {
        color: #ff69b4; /* Color on hover */
    }
    </style>
    """
    
    # Render the email with the defined CSS style
    st.write("📫", '<span class="email-text">praveshds1800@gmail.com</span>', unsafe_allow_html=True)

    # Render the CSS style
    st.markdown(email_style, unsafe_allow_html=True)




# Adding the links to my social
link_style = """
<style>
.link-text a {
    color: white; /* Initial color */
    text-decoration: none; /* Remove underline */
    font-weight: bold; /* Initial font weight */
    font-size: 20px; /* Initial font size */
}

.link-text a:hover {
    color: #ff69b4; /* Color on hover */
    font-size: 20px; /* Font size on hover */
}
</style>
"""

# Render the links with the defined CSS style
link, git, port, kaggle = st.columns(4, gap='small')

# Render the LinkedIn link
link.markdown(f'<div class="link-text"><a href="http://www.linkedin.com/in/praveshsingh1800" target="_blank">LinkedIn</a></div>', unsafe_allow_html=True)

# Render the Github link
git.markdown(f'<div class="link-text"><a href="https://github.com/Pravesh1800" target="_blank">Github</a></div>', unsafe_allow_html=True)

# Render the Portfolio link
port.markdown(f'<div class="link-text"><a href="http://localhost:8502/streamlit.link" target="_blank">Portfolio</a></div>', unsafe_allow_html=True)

# Render the Kaggle link
kaggle.markdown(f'<div class="link-text"><a href="https://www.kaggle.com/praveshsingh471" target="_blank">Kaggle</a></div>', unsafe_allow_html=True)

# Render the CSS style
st.markdown(link_style, unsafe_allow_html=True)







#--- Education ---
st.write('\n')
st.markdown(
    """
    <style>
    .heading-line h2 {
        margin-bottom: 0.25rem; /* Adjust the value as needed */
    }
    .heading-line hr {
        margin-top: 0.1rem; /* Adjust the value as needed */
        margin-bottom: 0.5rem; /* Adjust the value as needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)

import streamlit as st

# Define the CSS style for the list
list_style = """
<style>
.no-bullets {
    list-style-type: none; /* Remove bullet points */
    padding-left: 0; /* Remove default left padding */
}

.no-bullets li {
    margin-bottom: 10px; /* Add some space between list items */
}
</style>
"""

# Render the CSS style
st.markdown(list_style, unsafe_allow_html=True)

# Render the heading and horizontal rule together
st.write('<div class="heading-line"><h1>Education</h1><hr></div>', unsafe_allow_html=True)

# Render the text in an unordered list format without bullet points
st.markdown("""
<ul class="no-bullets">
    <li>🎓 GRADUATION | Bachelor of Computer Applications | GITAM AUG 2021 – APR 2024</li>
    <li>🎒 12th | Science Stream | KENDRIYA VIDYALAYA 1 (NSB VISAKHAPATNAM) | 86%</li>
    <li>🎒 10th | KENDRIYA VIDYALAYA 1 (NSB VISAKHAPATNAM) | 82%</li>
</ul>
""", unsafe_allow_html=True)



# --- EXPERIENCE ---
st.write('\n')
st.markdown(
    """
    <style>
    .heading-line h2 {
        margin-bottom: 0.25rem; /* Adjust the value as needed */
    }
    .heading-line hr {
        margin-top: 0.1rem; /* Adjust the value as needed */
        margin-bottom: 0.5rem; /* Adjust the value as needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)

import streamlit as st

# Define the CSS style for the list
list_style = """
<style>
.no-bullets {
    list-style-type: none; /* Remove bullet points */
    padding-left: 0; /* Remove default left padding */
}

.no-bullets li {
    margin-bottom: 10px; /* Add some space between list items */
}
</style>
"""

# Render the CSS style
st.markdown(list_style, unsafe_allow_html=True)

# Render the heading and horizontal rule
st.write('<div class="heading-line"><h1>Experience</h1><hr></div>', unsafe_allow_html=True)

# Render the text in an unordered list format without bullet points
st.markdown("""
<ul class="no-bullets">
    <li>✔️ Experienced in extracting actionable insights from data</li>
    <li>✔️ Strong hands-on experience and knowledge in Python and Excel</li>
    <li>✔️ Good understanding of Machine Learning models and their respective applications</li>
    <li>✔️ Excellent team-player and displaying strong sense of initiative on tasks</li>
</ul>
""", unsafe_allow_html=True)



# --- SKILLS ---
st.write('\n')
st.markdown(
    """
    <style>
    .heading-line h2 {
        margin-bottom: 0.25rem; /* Adjust the value as needed */
    }
    .heading-line hr {
        margin-top: 0.1rem; /* Adjust the value as needed */
        margin-bottom: 0.5rem; /* Adjust the value as needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Render the heading and horizontal rule together
st.write('<div class="heading-line"><h1>Hard Skills</h1><hr></div>', unsafe_allow_html=True)
st.write("""
👩‍💻 **Programming**: """)
st.write('''
    - - _Python (Scikit-learn)_
    - - _Python (Tensorflow)_
    - - _Python (Pandas)_ 
    - - _SQL_

''')

st.write("""
📊 **Data Visulization** """)
st.write('''
    - - _MS Excel_
    - - _Python(Matplotlib)_
    - - _Python(Seaborn)_ 
''')

st.write("""
📚 **Modeling** """)
st.write('''
    - - _Logistic regression_
    - - _Linear regression_
    - - _Decition trees_ 
    - - _Artificial Neural Networks_
''')

st.write("""
🗄️ **Databases** """)
st.write('''
    - - _MySQL_
''')

st.write("""
💻**Web Application** """)
st.write('''
    - - _Python(Streamlit)_
''')




# --- Projects & Accomplishments ---
st.write('\n')
st.markdown(
    """
    <style>
    .heading-line h2 {
        margin-bottom: 0.25rem; /* Adjust the value as needed */
    }
    .heading-line hr {
        margin-top: 0.1rem; /* Adjust the value as needed */
        margin-bottom: 0.5rem; /* Adjust the value as needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Render the heading and horizontal rule together
st.write('<div class="heading-line"><h1>Projects & Accomplishments</h1><hr></div>', unsafe_allow_html=True)
# --- Project 1
st.write("😞", "**Sucidal Tendency Text Classification | Machine Learning Classification Model**")
st.write("Mar 2024")
st.write(
    """
- ► Applied Support Vector Classification to predict suicidal tendencies in the text data.
- ► Conducted Exploratory Data Analysis (EDA) to understand data distributions, manage missing values,
    and remove outliers.
- ► Implemented feature engineering techniques to optimize data representation.
- ► Achieved a 94% accuracy rate, demonstrating the efficacy of the developed model in identifying
    potential suicidal behavior.
- ► Created an application using Streamlit and deployed it on the Streamlit cloud.
"""
)
# --- Project 2
st.write("")
st.write("🏠", "**Banglore House Price Prediction | Machine Learning Regression Model**")
st.write("Mar 2024")
st.write(
    """
- ► Developed this project for the Kaggle house price prediction competition.
- ► Conducted Exploratory Data Analysis (EDA) to understand data distributions, manage missing values,
    and remove outliers.
- ► Employed Linear Regression to predict house prices based on dataset from Kaggle.
- ► Achieved an outstanding accuracy rate of 86%, showcasing the effectiveness of the model.
- ► Created an application using Streamlit and deployed it on the Streamlit cloud.
"""
)
# --- Project 3
st.write("")
st.write("🛳️", "**TITANIC SURVIVAL PREDICTION | Machine Learning Classification Model**")
st.write("Apr 2024")
st.write(
    """
- ► Developed this project for the Kaggle Titanic survival prediction competition.
- ► Conducted Exploratory Data Analysis (EDA) to understand data distributions, manage missing values,
    and remove outliers.
- ► Utilized the Random Forest Algorithm for efficient prediction.
- ► Achieved an accuracy rate of 89%, ensuring reliable identification of fraudulent transactions.
- ► Created an application using Streamlit and deployed it on the Streamlit cloud.
"""
)
