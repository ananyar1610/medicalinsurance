import streamlit as st
import pandas as pd
from streamlit_app.eda_pages import univariate, bivariate
from streamlit_app.estimator import estimator_form


st.set_page_config(
    page_title="Medical Insurance Charges Prediction",
    layout="wide"
)

df = pd.read_csv("data/medical_insurance.csv")

page = st.sidebar.radio(
    "Navigation",
    [
        "Project Introduction",
        "Data Overview",
        "EDA",
        "Insurance Estimator"
    ],
)

if page == "Project Introduction":
    st.title("Medical Insurance Charge Prediction")

elif page == "Data Overview":
    st.dataframe(df)

elif page == "EDA":
    analysis = st.selectbox(
        "Analysis Type",
        ["Univariate", "Bivariate"]
    )
    if analysis == "Univariate":
        univariate(df)
    else:
        bivariate(df)

elif page == "Insurance Estimator":
    estimator_form()
