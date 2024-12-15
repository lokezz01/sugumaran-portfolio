import streamlit as st
from PIL import Image

# --- General Settings ---
st.set_page_config(page_title="Digital CV", page_icon="🧑‍💻", layout="wide")
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- Load Images ---
profile_pic = "profile.jpeg"  # Replace with your profile image file
cv_pdf = "resume.pdf"  # Replace with your resume file

# --- Sidebar ---
with st.sidebar:
    st.image(profile_pic, width=150)
    st.title("👋 Hi, I'm Sugumaran")
    st.subheader("Associate Software Engineer | Data Engineer")
    st.write(""" 
    - 📧 Email: [sugumaran1102@gmail.com](mailto:sugumaran1102@gmail.com)
    - 🔗 [LinkedIn](https://www.linkedin.com/in/sugumaran-b-a4868a219)
    - 💻 [GitHub](https://github.com/lokezz01)
    - 📄 [Download CV](resume.pdf)
    """)
    st.markdown("---")

# --- Introduction ---
st.title("Digital CV 🧑‍💻")
st.write("""
Welcome to my interactive digital CV!  
Explore my background, skills, projects, and experiences in a single place.
""")

# --- About Me Section ---
st.subheader("About Me")
st.write("""
I'm Sugumaran, an **Associate Software Engineer** passionate about creating solutions to real-world problems using technology.  
With expertise in **Python**, **AWS Services**, **SQL**, **PySpark**, and **Web Development**, I aim to deliver impactful projects.
""")

# --- Skills Section ---
st.subheader("Skills")
skills = {
    "Programming Languages": ["Python", "JavaScript", "SQL", "AWS Services"],
    "Libraries & Frameworks": ["Streamlit", "Pandas", "NumPy", "Matplotlib"],
    "Tools & Platforms": ["Git", "VS Code", "Jupyter", "Docker"],
}
for category, skillset in skills.items():
    st.write(f"**{category}:** {', '.join(skillset)}")

# --- Projects Section ---
st.subheader("Projects")
col1, col2 = st.columns(2)

# Uncomment and fill project details as needed
# with col1:
#     st.markdown("### 📊 Project 1: Data Dashboard")
#     st.image("project1.jpg", caption="Data Dashboard Project", use_column_width=True)
#     st.write("""
#     - **Tools**: Python, Streamlit, Pandas  
#     - **Description**: A dashboard to analyze and visualize data.
#     - 🌐 [View Project](https://github.com)
#     """)

# with col2:
#     st.markdown("### 🌐 Project 2: Web Scraper")
#     st.image("project2.jpg", caption="Web Scraper Project", use_column_width=True)
#     st.write("""
#     - **Tools**: Python, BeautifulSoup, Pandas  
#     - **Description**: A web scraper to collect real-time data.
#     - 🌐 [View Project](https://github.com)
#     """)

# --- Work Experience ---
st.subheader("Work Experience")
st.write("""
**Associate Software Engineer**, Prodapt Solutions *(May 2022 - Present)*  
1. **Data Pipeline Development**:
   - Designed and implemented scalable ETL pipelines using **AWS Lambda**, **AWS S3**, and **AWS Glue** for data extraction, transformation, and loading from diverse sources into a central data warehouse.
   - Developed Python scripts to automate data workflows and processing tasks, reducing manual intervention by 50%.

2. **Cloud Data Architecture**:
   - Architected and maintained cloud-based data solutions on **AWS**, using services like **Amazon Redshift** for data warehousing, **AWS S3** for data storage, and **AWS Glue** for data cataloging.
   - Utilized **Amazon RDS** (PostgreSQL) to manage transactional databases and improve query performance by optimizing indexing and query design.

3. **Data Integration & SQL Optimization**:
   - Integrated data from multiple on-premise and cloud sources (**AWS S3**, databases, APIs) and optimized complex SQL queries to ensure low-latency data access.
   - Tuned SQL queries on **Amazon Redshift** and **MySQL** for performance improvements, resulting in a 30% reduction in query execution times.

4. **Data Processing with Python & Pandas**:
   - Developed Python scripts using **Pandas** and **NumPy** to preprocess and clean data, ensuring high-quality data ready for analysis and reporting.
   - Automated data quality checks and error logging within data pipelines, resulting in a 40% reduction in data-related errors.

5. **Real-Time Data Processing**:
   - Implemented real-time data processing pipelines using **AWS Kinesis** and **AWS Lambda** for streaming data ingestion and immediate analysis of IoT sensor data.
   - Created automated alerting and monitoring systems for real-time processing jobs, improving operational efficiency by providing immediate feedback on pipeline performance.

6. **Collaboration & Reporting**:
   - Collaborated with data scientists and business analysts to understand data requirements and deliver data solutions that supported advanced analytics and business intelligence.
   - Produced automated reports and dashboards using **AWS QuickSight** and **Jupyter Notebooks** to present insights and performance metrics to stakeholders.

7. **AWS Security & Best Practices**:
   - Ensured compliance with security standards by implementing encryption strategies for data in transit and at rest in **AWS S3**, **Redshift**, and **RDS**.
   - Set up **AWS IAM roles** to enforce access controls, ensuring that data is accessed securely by the appropriate services and users.
""")

# --- Contact Section ---
st.subheader("Contact Me 📞")
st.write("""
You can reach me through the following channels:

- 📧 **Email**: [sugumaran1102@gmail.com](mailto:sugumaran1102@gmail.com)
- 📱 **Phone**: +91 6383315066
""")

# --- Footer ---
st.markdown("---")
st.write("🧑‍💻 Created with Streamlit | © 2024 Sugumaran B")
