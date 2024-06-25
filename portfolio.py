import streamlit as st
from PIL import Image
import base64
import streamlit.components.v1 as components

# Set page title and icon
st.set_page_config(layout="wide")  # Set the layout to wide

# Remove padding around the main content
st.markdown(
    """
    <style>
    .main .block-container {
        padding-top: 1rem;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("Navigation")
st.sidebar.markdown("[Introduction](#introduction)")
st.sidebar.markdown("[Education](#education)")
st.sidebar.markdown("[Skills](#skills)")
st.sidebar.markdown("[Projects](#projects)")




def show_introduction():


    # Personal Information
    name = "Niraj Chaudhari"
    title = "Aspiring Data Analyst/Data Scientist"
    
    description = """
Hello! I'm Niraj Chaudhari, a recent graduate with a passion for data science and analytics. Transitioning from a non-IT background, I made a conscious decision to enter this field. I completed my graduation last year and further honed my skills through an intensive 8-month-long data science bootcamp. Studying data science for quite some time, I am now 21 years old and eager to kickstart my career in this dynamic field, contributing meaningfully along the way. Currently, I am actively seeking internship opportunities to apply my skills and gain valuable experience in the industry.
"""
    

    
    

    # Introduction Section
    with st.container():
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.markdown("<br>", unsafe_allow_html=True)  # Add empty space
            profile_img = Image.open(r"C:\Users\Amruta\Desktop\Niraj's Project\images\Profile_pic.jpeg")
            st.image(profile_img, use_column_width=True)
        
        with col2:
            
            st.title(name)
            st.subheader(title)
            st.write(description)
            st.markdown("<br>", unsafe_allow_html=True)  # Add empty space

            st.markdown("""
            <div style="padding: 10px; background-color: #f0f0f0; border-radius: 5px; text-align: center;">
                <h3 style="color: #d9534f;">Currently Seeking Internship Opportunities</h3>
                <p style="color: #333;">If you have an opening for a Data Analytics internship, I'd love to connect!</p>
            </div>
            """, unsafe_allow_html=True)
                    
            # Load icons
            icon_gmail = Image.open(r"C:\Users\Amruta\Desktop\Niraj's Project\images\contact_icons\gmail_icon.png")
            icon_phone = Image.open(r"C:\Users\Amruta\Desktop\Niraj's Project\images\contact_icons\phone_icon.png")
            icon_contact = Image.open(r"C:\Users\Amruta\Desktop\Niraj's Project\images\contact_icons\contact_icon.png")
            icon_github = Image.open(r"C:\Users\Amruta\Desktop\Niraj's Project\images\contact_icons\github_icon.png")
            icon_linkedin = Image.open(r"C:\Users\Amruta\Desktop\Niraj's Project\images\contact_icons\linkedin_icon.png")

            # Create the contact section
            st.markdown("<br>", unsafe_allow_html=True)  # Add empty space
            st.subheader("Contact Details")

            with st.container():
                col1,col3,col4,col6 = st.columns([0.05,0.3,0.05,0.3])
                
            

                # Email
                with col1:
                    st.image(icon_gmail, width=30)
                    st.image(icon_phone, width=30)
                
                with col3:
                    st.write("nirajchaudhari170503@gmail.com")
                    st.write("+91-8767281554")

                

                # LinkedIn
                with col4:
                    st.image(icon_linkedin, width=30)
                    st.image(icon_github, width=30)
                
                with col6:
                    st.write("[LinkedIn](https://www.linkedin.com/in/niraj-chaudhari-50307a243/)")
                    st.write("[GitHub](https://github.com/nirajc170503)")
       
        
def show_education():
    st.write("### Non-IT Background to Data Science Transition")
    st.write("**Introduction:**")
    st.write("Coming from a non-IT background, I embarked on a journey to transition into the field of data science and analytics. My educational path reflects my determination to acquire the necessary skills and knowledge for this transition.")
    
    st.markdown("<br>", unsafe_allow_html=True)  # Add empty space
    
    with st.container():
        # Logo and Description Column
        col1, col2, col_x1 = st.columns([1, 5, 1])
        with col1:
            st.markdown("<br>", unsafe_allow_html=True)  # Add empty space
            img_logo = Image.open(r"C:\Users\Amruta\Desktop\Niraj's Project\images\Great_Learning_Logo.jpg")
            st.image(img_logo, use_column_width=True)
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)  # Add empty space
            st.write("### Professional Certification in Data Science Engineering")
            st.write("**Great Learning, Pune**")
            st.write("**Duration:** August 2023 - April 2024")
            st.write("**Program:** PGP Data Science Engineering | [Academic e-Portfolio](https://eportfolio.mygreatlearning.com/niraj-chaudhari)")
            st.write("**Description:**")
            st.write("I successfully completed a rigorous 8-month-long classroom program in Data Science Engineering from Great Learning, Pune, in association with Great Lakes Institute of Management. This comprehensive program involved mastering Python for exploratory data analysis, various visualization techniques, and machine learning, along with MySQL for database management. The program's rigorous nature required clearing 10 modules with over 60% marks, multiple vivas, and a capstone project.")
        with col_x1:
            # Certification and Transcript Column
            
            st.write("**Certification:**")
            img_cert = Image.open(r"C:\Users\Amruta\Desktop\Niraj's Project\images\GL_certificate.jpg")
            st.image(img_cert, use_column_width=True)

            st.write("**Transcript:**")
            img_transcript = Image.open(r"C:\Users\Amruta\Desktop\Niraj's Project\images\transcript1.jpg")
            st.image(img_transcript, use_column_width=True)
        
        
        st.markdown("<br>", unsafe_allow_html=True)  # Add empty space
        st.markdown("<br>", unsafe_allow_html=True)  # Add empty space

        with st.container():
            # Second Certification: IIT Madras
            col5, col6, col7 = st.columns([1, 5, 1])
            with col5:
                img_logo_iitm = Image.open(r"C:\Users\Amruta\Desktop\Niraj's Project\images\IITM _logo.jpg")
                st.image(img_logo_iitm, use_column_width=True)
            with col6:
                st.write("### Foundation Level in Programming and Data Science")
                st.write("**IIT Madras Degree Program (CODE)**")
                st.write("**Duration:** January 2022 - December 2022")
                st.write("**Program:** Foundation Level in Programming and Data Science | **CGPA:** 7.8/10.0")
                st.write("**Description:**")
                st.write("I successfully completed the Foundation Level of the BS Degree in Data Science and Programming from IIT Madras. The program was structured into three parts, with an option to exit after completing any part and receive the respective certification. I chose to conclude my studies after the first level, which took around a year to complete. This rigorous program involved both online instruction and offline proctored exams, making it a challenging journey. Over the course of the year, I cleared 8 modules, in addition to completing numerous mandatory assignments. The exams were notably difficult, reflecting the high standards of the program. Through this experience, I mastered Python programming for data manipulation, analysis, and visualization, and gained a solid understanding of essential mathematical concepts, including linear algebra, calculus, and probability theory.")
            with col7:
                
                st.write("**Certification:**")
                img_cert_iitm = Image.open(r"C:\Users\Amruta\Desktop\Niraj's Project\images\IITM_certificate_img.png")
                st.image(img_cert_iitm, use_column_width=True)    
            
                st.write("**Grade Card:**")  
                img_gradecard = Image.open(r"C:\Users\Amruta\Desktop\Niraj's Project\images\IITM_gradecard.png")
                st.image(img_gradecard, use_column_width=True)
        
        
        st.markdown("<br>", unsafe_allow_html=True)  # Add empty space
        with st.container():
            # Education Details
            # Education Details in Bullet Points
            st.subheader("Other Education Details")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("**10th Maharashtra State Board, India**")
                st.write("May 2018")
                st.write("Percentage: ****88%****")
            with col2:
                st.write("**12th Maharashtra State Board, India**")
                st.write("May 2020")
                st.write("Percentage: ****81.86%****")
            with col3:
                st.write("**Bachelor of Business Administration (Finance)**")
                st.write("Sinhgad College of Science, Pune, India")
                st.write("Aug 2020 – Jul 2023")
                st.write("CGPA: ****9.11/10.0****")   
                

def show_skills():
            
    # Define the skills in each category
    programming_skills = ["Python", "MySQL"]
    data_skills = ["Pandas", "NumPy", "Matplotlib", "Seaborn", "Power BI", "Plotly"]
    ml_skills = ["Regression", "Classification", "Clustering", "Unsupervised Learning"]
    web_scraping_skills = ["Beautiful Soup"]
    other_skills = ["Statistical Analysis", "Streamlit","Exploratory Data Analysis (EDA)"]

    # Create a dictionary to store the skills with icons
    icons = {
        "Python": "🐍", "MySQL": "🗄️", "Pandas": "🐼", "NumPy": "🔢", "Matplotlib": "📊",
        "Seaborn": "🌊", "Power BI": "📈", "Plotly": "📉", "Exploratory Data Analysis (EDA)": "🔍",
        "Regression": "📉", "Classification": "🗂️", "Clustering": "🔀", "Unsupervised Learning": "🤖",
        "Beautiful Soup": "🍲", "Statistical Analysis": "📊", "Streamlit": "🚀"
    }

    # Display skills in each category using columns
    st.markdown("<br>", unsafe_allow_html=True)  # Add empty space
    

    # Create columns
    col1, col2, col3, col4 = st.columns(4)

    # Programming and Database Management
    with col1:
        st.write("#### Programming and Database Management")
        for skill in programming_skills:
            st.write(f"{icons.get(skill, '')} {skill}")

    # Data Analysis and Visualization
    with col2:
        st.write("#### Data Analysis and Visualization")
        for skill in data_skills:
            st.write(f"{icons.get(skill, '')} {skill}")

    # Machine Learning
    with col3:
        st.write("#### Machine Learning")
        for skill in ml_skills:
            st.write(f"{icons.get(skill, '')} {skill}")

    # Web Scraping and Other Skills
    with col4:
        st.write("#### Web Scraping")
        for skill in web_scraping_skills:
            st.write(f"{icons.get(skill, '')} {skill}")
        
        st.write("#### Other Skills")
        for skill in other_skills:
            st.write(f"{icons.get(skill, '')} {skill}")


def show_projects():
    

    # Function to read HTML content from a file
    def read_html(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    st.markdown("<br>", unsafe_allow_html=True)  # Add empty space

    # Content outside the button
    st.subheader("PROJECT 1: Loan Default Analysis & Prediction")

    with st.container():
        col1, col2 = st.columns([2.5, 1])
        with col1:
            st.write("""
            This project analyzes loan applicant data to predict defaults using supervised machine learning techniques. 
            The goal is to help lenders make informed decisions and mitigate risks by identifying applicants who are likely to default.
            """)

            st.write("""
            - **Credit Risk Analysis**: Addressing a critical issue in the banking sector by predicting loan defaults to prevent non-performing loans and financial losses.
            - **Home Credit**: Analyzing data provided by Home Credit Group, a global consumer finance provider operating in 9 countries.
            - **Machine Learning Techniques**: Using supervised learning techniques such as logistic regression, decision tree, KNN, random forest, AdaBoost, and XGBoost.
            - **Comprehensive Data Processing**: Including data preprocessing, feature engineering, exploratory data analysis, and assumption testing.
            """)
            st.write("[GitHub Project Link](https://github.com/nirajc170503/Loan-Default-Prediction)")
            
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)  # Add empty space
            st.markdown("<br>", unsafe_allow_html=True)  # Add empty space

            project_img = Image.open(r"C:\Users\Amruta\Desktop\Niraj's Project\images\home_credit_img.jpeg")
            st.image(project_img, use_column_width=True)


    # Button for toggling detailed information
    if "show_details" not in st.session_state:
        st.session_state.show_details = False

    if st.button("Click here to see detailed information about the project along with jupyter notebooks"):
        st.session_state.show_details = not st.session_state.show_details

    # Detailed information shown when the button is clicked
    if st.session_state.show_details:
        with st.container():

            st.header("Detailed Description")
            st.write("""
            **Home Credit Default Risk**

            Credit-lending plays a significant role in the banking sector. But the increase in non-performing loans has made the banking sector face huge losses and also has an impact on the economy of the country or the world. Thus an existential problem for any Loan provider today is to find out the Loan applicants who are very likely to repay the loan. This way companies can avoid losses and incur huge profits.

            In this project, we are going to take the loan applicant data provided by Home Credit and identify the applicants who are most likely to default using Supervised machine learning.

            **About Home Credit**

            Home Credit Group is a global consumer finance provider founded in 1997, operating in 9 countries. 
            It empowers underserved customers with little or no credit history by enabling them to borrow easily and safely.
            """)

            st.header("Dataset")
            st.write("""
            The dataset is sourced from the Home Credit Default Risk competition on Kaggle, consisting of multiple files related to applicant data. 
            [Dataset link](https://www.kaggle.com/c/home-credit-default-risk/data)
            """)

            st.header("Project Cycle and Notebooks")

            # First Row
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("1. Data Preprocessing")
                st.write("Cleaned datasets, handled missing values, and generated new features.")
                html_file_path1 = r"C:\Users\Amruta\Desktop\Niraj's Project\html\Data Preprocessing File1.html"
                notebook_html1 = read_html(html_file_path1)
                st.components.v1.html(notebook_html1, height=300, scrolling=True)

            with col2:
                st.subheader("2. Feature Engineering")
                st.write("Used recursive feature elimination to reduce features.")
                html_file_path2 = r"C:\Users\Amruta\Desktop\Niraj's Project\html\Feature Engineering File 2.html"
                notebook_html2 = read_html(html_file_path2)
                st.components.v1.html(notebook_html2, height=300, scrolling=True)

            # Second Row
            col3, col4 = st.columns(2)
            with col3:
                st.subheader("3. Exploratory Data Analysis (EDA)")
                st.write("Analyzed data, plotted distributions, treated outliers, and scaled features.")
                html_file_path3 = r"C:\Users\Amruta\Desktop\Niraj's Project\html\EDA File3.html"
                notebook_html3 = read_html(html_file_path3)
                st.components.v1.html(notebook_html3, height=300, scrolling=True)

            with col4:
                st.subheader("4. Assumption Testing")
                st.write("Checked assumptions required for logistic regression.")
                html_file_path4 = r"C:\Users\Amruta\Desktop\Niraj's Project\html\Assumptions File4.html"
                notebook_html4 = read_html(html_file_path4)
                st.components.v1.html(notebook_html4, height=300, scrolling=True)

            # Third Row
            col5, col6 = st.columns(2)
            with col5:
                st.subheader("5. Base Model - Logistic Regression")
                st.write("Evaluated logistic regression model using confusion matrix and classification report.")
                html_file_path5 = r"C:\Users\Amruta\Desktop\Niraj's Project\html\Base model-Logistic regression File 5.html"
                notebook_html5 = read_html(html_file_path5)
                st.components.v1.html(notebook_html5, height=300, scrolling=True)

            with col6:
                st.subheader("6. Machine Learning Models")
                st.write("Implemented decision tree, KNN, random forest, AdaBoost, and XGBoost models using the SMOTE dataset.")
                html_file_path6 = r"C:\Users\Amruta\Desktop\Niraj's Project\html\ML models File 6.html"
                notebook_html6 = read_html(html_file_path6)
                st.components.v1.html(notebook_html6, height=300, scrolling=True)


    st.markdown("<br>", unsafe_allow_html=True)  # Add empty space


    
    
    st.subheader("PROJECT 2: Stock Analysis Web App  [  (Link)](https://stock-tracker-app.streamlit.app/)")

    with st.container():
        col1, col2 = st.columns([2.5, 1])
        
        with col1:
            st.write("""
            **Project Summary: Stock Analysis App**  
            
            - **Volatility Analysis**: Interactive area charts, adjustable timeframes, key metrics display.
            - **Bollinger Bands Analysis**: Customizable parameters, metrics display, interactive visualizations.
            - **Strength Analysis**: Dynamic highlighting, customizable parameters, easy identification of thresholds.
            - **Momentum Analysis**: Histogram display, customizable parameters, trend and momentum identification.
            """)
            st.write("[GitHub Project Link](https://github.com/nirajc170503/Stock-tracker-App)")

        with col2:
            project_img = Image.open(r"C:\Users\Amruta\Desktop\Niraj's Project\images\web_app_img.jpeg")
            st.image(project_img, use_column_width=True)
            
    # Button for toggling detailed information
    if "stock_analysis_show_details" not in st.session_state:
        st.session_state.stock_analysis_show_details = False

    if st.button("Click here to see detailed information about the Stock Analysis project along with Jupyter Notebook"):
        st.session_state.stock_analysis_show_details = not st.session_state.stock_analysis_show_details

    # Detailed information shown when the button is clicked
    if st.session_state.stock_analysis_show_details:
        with st.container():
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.subheader("Detailed Description")
                st.write("""
                **Overview**:
                The Stock Analysis and Visualization App is a comprehensive tool developed using Streamlit for analyzing various financial KPIs of stocks. It offers advanced interactive visualizations and machine learning models for insightful analysis and predictions.

                **Key Features**:
                - **Volatility Analysis**:
                    - Visualize stock volatility using area charts.
                    - Select timeframe for analysis (1 month to all time).
                    - Display key metrics like average and current volatility.
                - **Bollinger Bands Analysis**:
                    - Visualize Bollinger Bands for stock price movements.
                    - Adjust window size and standard deviations.
                    - Display metrics such as percentage above/below the band.
                - **RSI Analysis**:
                    - Visualize RSI to identify overbought/oversold conditions.
                    - Highlight RSI thresholds for easy identification.
                    - Set window size and thresholds for conditions.
                - **MACD Analysis**:
                    - Visualize MACD for trend changes and momentum.
                    - Show MACD histogram for trend analysis.
                    - Set short-term, long-term, and signal window sizes.
                    
                **User-Friendly Interface**:
                - Intuitive Layout: Organized containers and columns for a clean and professional look.
                - Interactive Widgets: Dropdowns, sliders, and other widgets for easy customization.
                - Dynamic Updates: Visualizations and metrics update dynamically based on user inputs.

                **Technical Implementation**:
                - Backend: Python and Streamlit framework for building the web app.
                - Data Processing: Pandas and NumPy for data manipulation and financial indicator calculation.
                - Visualization: Plotly for creating interactive and visually appealing charts.
                """)

            with col2:
                st.write("### Jupyter Notebook")
                html_file_path = r"C:\Users\Amruta\Desktop\Niraj's Project\html\web_app_code.html"
                notebook_html = read_html(html_file_path)
                st.components.v1.html(notebook_html, height=500, scrolling=True)













    st.markdown("<br>", unsafe_allow_html=True)  # Add empty space
    st.markdown("<br>", unsafe_allow_html=True)  # Add empty space

    # Project: Zomato Data Analysis
    st.header("MINI PROJECTS")
    st.subheader("Mini Project 1: Zomato Data Analysis")

    with st.container():
        col1, col2 = st.columns([2.5, 1])
        
        with col1:
            st.write("""
            **Project Summary: Indian Food Delivery Restaurant Aggregator Analysis**
            
            - **Restaurant establishment factors**: Analyzed various factors influencing restaurant success in Bengaluru.
            - **Neighborhood analysis**: Provided insights into neighborhood demographics and food preferences.
            - **Data details**: Used Zomato data including restaurant ID, name, location, cuisines, cost, ratings, and reviews.
            - **Key findings**: Identified top restaurant chains, booking preferences, and rating trends.
            """)
            st.write("[GitHub Project Link](https://github.com/nirajc170503/Analysis-of-Zomato-dataset)")
        with col2:
            project_img = Image.open(r"C:\Users\Amruta\Desktop\Niraj's Project\images\Zomato_logo.jpeg")
            st.image(project_img, use_column_width=True)
            
            
    # Button for toggling detailed information
    if "zomato_show_details" not in st.session_state:
        st.session_state.zomato_show_details = False

    if st.button("Click here to see detailed information about the Zomato project along with Jupyter Notebook"):
        st.session_state.zomato_show_details = not st.session_state.zomato_show_details

    # Detailed information shown when the button is clicked
    if st.session_state.zomato_show_details:
        with st.container():
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.subheader("Detailed Description")
                st.write("""
                **Problem Statement**: Analyzing Zomato data to understand factors influencing restaurant establishment, ratings, and neighborhood similarities in Bengaluru. This helps new restaurants in decision-making regarding themes, menus, cuisines, and costs.

                **Aim**: To help new restaurants understand neighborhood demographics, food similarities, and overall restaurant ratings.

                **Dataset**: Zomato data including details such as restaurant ID, name, location, cuisines, average cost, ratings, and reviews.

                **Key Analyses**:
                - Top restaurant chains in Bengaluru
                - Restaurants not accepting online orders
                - Ratio of restaurants providing table booking
                - Rating distribution and analysis
                - Online order acceptance and its impact on ratings and costs
                - Popular restaurant types and cuisines in Bengaluru
                """)

            with col2:
                st.write("### Jupyter Notebook")
                html_file_path = r"C:\Users\Amruta\Desktop\Niraj's Project\html\MINI_project.html"
                notebook_html = read_html(html_file_path)
                st.components.v1.html(notebook_html, height=500, scrolling=True)


    # Project2
    st.markdown("<br>", unsafe_allow_html=True)  # Add empty space
    st.subheader("Mini Project 2: Web Scraping and Text cleaning")

    with st.container():
        col1, col2 = st.columns([2.5, 1])

        with col1:
            st.write("""
            **Project Summary: Web Scraping and Text Analysis**

            - **Objective**: Extract textual data articles from the given URL and perform text analysis.
            - **Data Extraction**: Extract article text from given URLs, excluding website header, footer, etc.
            - **Data Analysis**:
              - Extracted text is analyzed to compute variables as per the given output structure.
            """)
            st.write("[GitHub Project Link](https://github.com/nirajc170503/Data-Extraction-Sentiment-Analysis)")

        with col2:
            project_img = Image.open(r"C:\Users\Amruta\Desktop\Niraj's Project\images\web_scraping_logo.jpeg")
            st.image(project_img, use_column_width=True)

    # Button for toggling detailed information
    if "web_scraping_show_details" not in st.session_state:
        st.session_state.web_scraping_show_details = False

    if st.button("Click here to see detailed information about the Web Scraping project"):
        st.session_state.web_scraping_show_details = not st.session_state.web_scraping_show_details

    # Detailed information shown when the button is clicked
    if st.session_state.web_scraping_show_details:
        with st.container():
            col1, col2 = st.columns([1, 1])
            with col1:
                st.subheader("Detailed Description")
                st.write("""
                **Detailed Description**:

                The objective of this assignment is to extract textual data articles from given URLs and perform text analysis. 
                For each article, extract the article text and save it in a text file with URL_ID as its file name. 
                Perform textual analysis to compute variables as explained in the given output structure.
                """)
            
        with col2:
                st.write("### Jupyter Notebook")
                html_file_path = r"C:\Users\Amruta\Desktop\Niraj's Project\html\Blackcoffer project.html"
                notebook_html = read_html(html_file_path)
                st.components.v1.html(notebook_html, height=300, scrolling=True)



    # project 3
    st.markdown("<br>", unsafe_allow_html=True)  # Add empty space
    st.subheader("Mini Project 3: SQL Project")

    with st.container():
        col1, col2 = st.columns([2.5, 1])

        with col1:
            st.write("""
            **Project Summary:**
            - Analyze composite data of a business organization in the 'sales and delivery' domain over the last decade.
            - Retrieve solutions for the given scenario.
            """)
            st.write("[GitHub Project Link](https://github.com/nirajc170503/SQL-Mini-Project)")

        with col2:
            project_img = Image.open(r"C:\Users\Amruta\Desktop\Niraj's Project\images\sql_image.png")
            st.image(project_img, use_column_width=True)

    # Button for toggling detailed information
    if "sql_show_details" not in st.session_state:
        st.session_state.sql_show_details = False

    if st.button("Click here to see detailed information about the SQL II project"):
        st.session_state.sql_show_details = not st.session_state.sql_show_details

    # Detailed information shown when the button is clicked
    if st.session_state.sql_show_details:
        with st.container():
            
            st.subheader("Detailed Description")
            st.write("""
            **Detailed Description:**
            Composite data of a business organization, confined to ‘sales and delivery’ domain, is given for the period of the last decade. Retrieve solutions for the given scenario.

            **Tasks:**
            1. Join all the tables and create a new table called combined_table.
            2. Find the top 3 customers who have the maximum number of orders.
            3. Create a new column DaysTakenForDelivery that contains the date difference of Order_Date and Ship_Date.
            4. Find the customer whose order took the maximum time to get delivered.
            5. Retrieve total sales made by each product from the data (use Windows function).
            6. Retrieve total profit made from each product from the data (use Windows function).
            7. Count the total number of unique customers in January and how many of them came back every month over the entire year in 2011.
            8. Retrieve month-by-month customer retention rate since the start of the business (using views).
            """)
            
                                
    # Digital Portfolio Website Project
    st.markdown("<br>", unsafe_allow_html=True)  # Add empty space
    st.subheader("Mini Project 4: Digital Portfolio Website(streamlit)")

    with st.container():
        col1, col2 = st.columns([2.5, 1])

        with col1:
            st.write("""
            This project is a digital portfolio and resume website showcasing professional information, projects, and educational background. 
            It is designed and developed entirely using Streamlit, a Python library, to create a professional and visually appealing online presence.
            """)

            st.write("""
            - **Technologies Used**: Streamlit
            - **Responsibilities**: Design and development of the entire website, including content creation and layout design
            - **Outcome**: A professional and visually appealing website serving as a digital resume and portfolio
            """)

            st.write("website link")
            
        with col2:
            

            project_img = Image.open(r"C:\Users\Amruta\Desktop\Niraj's Project\images\portfolio_image.jpeg")
            st.image(project_img, use_column_width=True)            


   






# Introduction section
st.markdown("<a name='introduction'></a>", unsafe_allow_html=True)
st.title("Introduction")
show_introduction()

# Education section
st.markdown("<a name='education'></a>", unsafe_allow_html=True)
st.title("Education")
show_education()

# Skills section
st.markdown("<a name='skills'></a>", unsafe_allow_html=True)
st.title("Skills")
show_skills()

# Projects section
st.markdown("<a name='projects'></a>", unsafe_allow_html=True)
st.title("Projects")
show_projects()