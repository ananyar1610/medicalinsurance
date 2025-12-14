

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('D:\GUVI2\Data\medical_insurance.csv')

st.set_page_config(page_title='Medical Insurance Charges Prediction', layout='wide')


st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Project Introduction', 'Data Overview', 'Exploratory Data Analysis', 'Insurance Estimator'])


if page == 'Project Introduction':
    st.markdown("""
    # Medical Insurance Charge Prediction
    
    ## Project Overview
    This project is designed to predict **medical insurance charges** based on a set of key demographic and health-related features such as **age**, **gender**, **BMI**, **smoking status**, and more. The goal is to provide predictive models that can assist healthcare providers, individuals, and organizations in better understanding and planning for future healthcare expenses.

    ## Business Use Cases
    - **Insurance Premium Estimation**: Estimate premiums based on individual attributes.
    - **Healthcare Cost Planning**: Provide individuals with more transparency regarding their expected healthcare costs.
    - **Cost Comparison for Insurance Policies**: Allow individuals to compare the potential cost of different insurance plans based on their personal profile.
    - **Healthcare Resource Allocation**: Assist organizations in allocating resources efficiently by understanding the cost dynamics associated with different demographic groups.

    ## Model Pipeline
    The project follows a systematic approach for building the prediction model:
    
    1. **Data Preprocessing**: Ensuring the dataset is clean and ready for model training.
    2. **Feature Engineering**: Identifying and creating the most relevant features for prediction.
    3. **Model Training and Evaluation**: Training machine learning models and evaluating their accuracy.
    4. **Deployment**: Making the final model accessible through a web interface built with **Streamlit**.
    
    ## Expected Outcomes
    The primary objective of this project is to offer actionable insights into healthcare expenses. By leveraging **predictive analytics**, the model empowers individuals and organizations to estimate and plan for insurance costs more effectively.
    """)


elif page == 'Data Overview':
    st.markdown("""
    # Dataset Overview
    
    The dataset comprises several key attributes that contribute to predicting **medical insurance charges**. Below is a detailed breakdown of the core features:

    ## Key Features:
    - **Age**: The individual's age in years.
    - **Sex**: Gender of the individual (male or female).
    - **BMI**: Body Mass Index, a measure of body fat based on height and weight.
    - **Children**: The number of children/dependents covered under the insurance.
    - **Smoker**: Whether the individual is a smoker (yes or no).
    - **Region**: The geographical region in which the individual resides (northeast, northwest, southeast, southwest).
    - **Charges**: The target variable representing the medical insurance charges.

    ## Data Insights
    The dataset enables the exploration of the following insights:
    - **Charge Distribution**: Understanding how medical insurance charges are distributed across different demographic factors.
    - **Impact of Health Factors**: Exploring how attributes like **BMI** and **smoking status** influence the medical charges.
    - **Geographic Trends**: Assessing how the region or location of an individual affects their medical insurance premiums.
    
    The dataset provides valuable information for building a robust predictive model that can help in **estimating medical insurance charges** accurately based on the individual's characteristics.

    ## Next Steps
    We will dive into an **exploratory data analysis (EDA)** to uncover hidden patterns and relationships between the features and the target variable. This step will guide us in **modeling** and **feature selection**.
    """)
    st.dataframe(df)


# Exploratory Data Analysis Page
elif page == 'Exploratory Data Analysis':
    st.title('Exploratory Data Analysis (EDA)')

    analysis_type = st.selectbox(
        'Select type of analysis:',
        ['Univariate Analysis', 'Bivariate Analysis', 'Multivariate Analysis', 'Outlier Detection', 'Correlation Analysis']
    )

    if analysis_type == 'Univariate Analysis':
        st.subheader('Univariate Analysis')
        question = st.selectbox('Choose a question:', [
            '1. Distribution of Medical Insurance Charges',
            '2. Age Distribution of individuals',
            '3. Smokers vs Non-Smokers',
            '4. Average BMI',
            '5. Policyholders by Region'
        ])
        if question.startswith('1'):
            st.subheader('1. What is the distribution of medical insurance charges?')
            plt.title('Charges Histplot')
            sns.histplot(x='charges', data=df)
            st.pyplot()
        elif question.startswith('2'):
            st.subheader('2.What is the age distribution of the individuals?')
            plt.title('Age Histplot')
            sns.histplot(x='age', data=df)
            st.pyplot()
        elif question.startswith('3'):
            st.subheader('3.How many people are smokers vs non-smokers?')
            sns.countplot(x='smoker', data=df)
            plt.title('Smokers v/s Non-Smokers')
            st.pyplot()
        elif question.startswith('4'):
            st.subheader('4. What is the average BMI in the dataset?')
            plt.title('BMI Histogram')
            sns.histplot(x='bmi', data=df)
            st.pyplot()
        elif question.startswith('5'):
            st.subheader('5. Which regions have the most number of policyholders?')
            sns.countplot(x='region', data=df)
            plt.title('Region with Most Number Of Policyholders')
            st.pyplot()

    elif analysis_type == 'Bivariate Analysis':
        question = st.selectbox('Choose a question:', [
            '1. How do charges vary with age?',
            '2. Is there a difference in average charges between smokers and non-smokers?',
            '3. Does BMI impact insurance charges?',
            '4. Do men or women pay more on average?',
            '5. Is there a correlation between the number of children and the insurance charges?'
        ])
        if question.startswith('1'):
            st.subheader('1. How do charges vary with age?')
            sns.scatterplot(x='age', y='charges', data=df)
            plt.title('Charges v/s Age')
            st.pyplot()
        elif question.startswith('2'):
            st.subheader('2. Is there a difference in average charges between smokers and non-smokers?')
            sns.barplot(x='smoker', y='charges', data=df)
            st.pyplot()
        elif question.startswith('3'):
            st.subheader('3. Does BMI impact insurance charges?')
            sns.scatterplot(x='bmi', y='charges', data=df)
            st.pyplot()
        elif question.startswith('4'):
            st.subheader('4. Do men or women pay more on average?')
            sns.barplot(x='sex', y='charges', data=df)
            st.pyplot()
        elif question.startswith('5'):
            st.subheader('5. Is there a correlation between the number of children and the insurance charges?')
            sns.boxplot(x='children', y='charges', data=df)
            st.pyplot()

    elif analysis_type == 'Multivariate Analysis':
        question = st.selectbox('Choose a question:', [
            '1. How does smoking status combined with age affect medical charges?',
            '2. What is the impact of gender and region on charges for smokers?',
            '3. How do age, BMI, and smoking status together affect insurance cost?',
            '4. Do obese smokers (BMI > 30) pay significantly higher than non-obese non-smokers?'
        ])
        if question.startswith('1'):
            st.subheader('1. How does smoking status combined with age affect medical charges?')
            sns.scatterplot(x='age', y='charges', hue='smoker', data=df, palette='pastel')
            st.pyplot()
        elif question.startswith('2'):
            st.subheader('2. What is the impact of gender and region on charges for smokers?')
            g = sns.FacetGrid(df[df['smoker'] == 'yes'], row='sex', col='region')
            g.map_dataframe(sns.boxplot, x='sex', y='charges')
            st.pyplot()
        elif question.startswith('3'):
            st.subheader('3. How do age, BMI, and smoking status together affect insurance cost?')
            sns.scatterplot(x='bmi', y='charges', hue='smoker', data=df)
            st.pyplot()
        elif question.startswith('4'):
            st.subheader('4. Do obese smokers (BMI > 30) pay significantly higher than non-obese non-smokers?')
            df2 = df.copy()
            df2['obese'] = df2['bmi'] > 30
            df2['group'] = df2['obese'].astype(str) + '_' + df2['smoker']
            sns.boxplot(x='group', y='charges', data=df2)
            plt.xlabel('BMI > 30 & Smoker')
            st.pyplot()

    elif analysis_type == 'Outlier Detection':
        question = st.selectbox('Choose a question:', [
            '1. Are there outliers in the charges column? Who are the individuals paying the highest costs?',
            '2. Are there extreme BMI values that could skew predictions?'
        ])
        if question.startswith('1'):
            st.subheader('1. Are there outliers in the charges column? Who are the individuals paying the highest costs?')
            sns.boxplot(y='charges', data=df)
            st.pyplot()
        elif question.startswith('2'):
            st.subheader('2. Are there extreme BMI values that could skew predictions?')
            sns.boxplot(y='bmi', data=df)
            st.pyplot()

    elif analysis_type == 'Correlation Analysis':
        question = st.selectbox('Choose a question:', [
            '1. What is the correlation between numeric features like age, BMI, number of children, and charges?',
            '2. Which features have the strongest correlation with the target variable (charges)?'
        ])
        if question.startswith('1'):
            st.subheader('1. What is the correlation between numeric features like age, BMI, number of children, and charges?')
            plt.figure(figsize=(10, 6))
            sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
            plt.title('Heatmap of Feature Correlation')
            st.pyplot()
        elif question.startswith('2'):
            st.subheader('2. Which features have the strongest correlation with the target variable (charges)?')
            corr_matrix = df.corr(numeric_only=True)
            st.dataframe(corr_matrix['charges'].sort_values(ascending=False))
elif page == 'Insurance Estimator':
    st.title("Insurance Cost Estimator")
    import joblib
    model=joblib.load('insurance_rf_model.pkl')

    with st.form("estiator_form"):
        age=st.slider("Age",18,100,30)
        sex=st.selectbox("sex",['male','female'])
        bmi=st.number_input("BMI",10.0,50.0,25.0)
        children=st.slider("Number of children", 0,5,0)
        smoker=st.selectbox("Smoker",['yes','no'])
        region=st.selectbox("Region",['northeast','northwest','southeast','southwest'])


        submitted=st.form_submit_button("Estimate Charges")
        if submitted:
            sex=1 if sex=='male' else 0
            smoker=1 if smoker=='yes' else 0
            region_northeast= 1 if region=='northeast' else 0
            region_northwest= 1 if region=='northwest' else 0
            region_southeast= 1 if region=='southeast' else 0
        
        
            input_data=[[
                age,sex,bmi,children,smoker, region_northeast,region_northwest,region_southeast
            ]]
            predicted_charge=model.predict(input_data)[0]
            st.success(f"Estimated Medical Insurance Charge: **${predicted_charge:,.2f}**")
