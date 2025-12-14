import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


def univariate(df):
    st.subheader("Univariate Analysis")
    sns.histplot(df["charges"])
    st.pyplot()


def bivariate(df):
    st.subheader("Bivariate Analysis")
    sns.scatterplot(x="age", y="charges", data=df)
    st.pyplot()
