import os
import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.title("Iris Predictor")

sepal_length = st.number_input("Sepal length", value=5.1)
sepal_width = st.number_input("Sepal width", value=3.5)
petal_length = st.number_input("Petal length", value=1.4)
petal_width = st.number_input("Petal width", value=0.2)

if st.button("Predict"):
    response = requests.post(
        f"{API_URL}/predict",
        json={
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width,
        },
        timeout=10,
    )
    st.json(response.json())