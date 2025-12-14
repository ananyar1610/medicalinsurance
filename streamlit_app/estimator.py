import joblib
import streamlit as st


def estimator_form():
    model = joblib.load("models/insurance_rf_model.pkl")

    with st.form("estimator"):
        age = st.slider("Age", 18, 100, 30)
        sex = st.selectbox("Sex", ["male", "female"])
        bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
        children = st.slider("Children", 0, 5, 0)
        smoker = st.selectbox("Smoker", ["yes", "no"])
        region = st.selectbox(
            "Region",
            ["northeast", "northwest", "southeast", "southwest"],
        )

        submitted = st.form_submit_button("Estimate")

        if submitted:
            sex = 1 if sex == "male" else 0
            smoker = 1 if smoker == "yes" else 0

            region_features = [
                int(region == "northeast"),
                int(region == "northwest"),
                int(region == "southeast"),
            ]

            features = [[
                age, sex, bmi, children, smoker, *region_features
            ]]

            prediction = model.predict(features)[0]
            st.success(f"Estimated Charges: ${prediction:,.2f}")
