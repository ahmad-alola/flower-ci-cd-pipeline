import os
import pandas as pd
import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://localhost:8000")

images = {
    "setosa": "images/setosa.jpg",
    "versicolor": "images/versicolor.jpg",
    "virginica": "images/virginica.jpg",
}

descriptions = {
    "setosa": "Small petals and compact structure.",
    "versicolor": "Intermediate size and balanced structure.",
    "virginica": "Larger petals and elongated structure.",
}

colors = {
    "setosa": "#4CAF50",
    "versicolor": "#2196F3",
    "virginica": "#9C27B0",
}

examples = {
    "setosa": {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    },
    "versicolor": {
        "sepal_length": 6.0,
        "sepal_width": 2.9,
        "petal_length": 4.5,
        "petal_width": 1.5,
    },
    "virginica": {
        "sepal_length": 6.9,
        "sepal_width": 3.1,
        "petal_length": 5.4,
        "petal_width": 2.1,
    },
}

averages = {
    "setosa": {
        "Sepal length": 5.0,
        "Sepal width": 3.4,
        "Petal length": 1.5,
        "Petal width": 0.2,
    },
    "versicolor": {
        "Sepal length": 5.9,
        "Sepal width": 2.8,
        "Petal length": 4.3,
        "Petal width": 1.3,
    },
    "virginica": {
        "Sepal length": 6.5,
        "Sepal width": 3.0,
        "Petal length": 5.5,
        "Petal width": 2.0,
    },
}

st.set_page_config(page_title="Iris Predictor", layout="centered")

if "sepal_length" not in st.session_state:
    st.session_state.sepal_length = 5.1
    st.session_state.sepal_width = 3.5
    st.session_state.petal_length = 1.4
    st.session_state.petal_width = 0.2

st.title("Iris Predictor")
st.write("Enter the measurements to predict the flower species test webhock.")

st.markdown("### Example values")
st.table(
    {
        "Class": ["setosa", "versicolor", "virginica"],
        "Sepal length": [5.1, 6.0, 6.9],
        "Sepal width": [3.5, 2.9, 3.1],
        "Petal length": [1.4, 4.5, 5.4],
        "Petal width": [0.2, 1.5, 2.1],
    }
)

col_btn1, col_btn2, col_btn3 = st.columns(3)

if col_btn1.button("Load Setosa"):
    for key, value in examples["setosa"].items():
        st.session_state[key] = value

if col_btn2.button("Load Versicolor"):
    for key, value in examples["versicolor"].items():
        st.session_state[key] = value

if col_btn3.button("Load Virginica"):
    for key, value in examples["virginica"].items():
        st.session_state[key] = value

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input("Sepal length", key="sepal_length")
    sepal_width = st.number_input("Sepal width", key="sepal_width")

with col2:
    petal_length = st.number_input("Petal length", key="petal_length")
    petal_width = st.number_input("Petal width", key="petal_width")

if st.button("Predict"):
    try:
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

        prediction = response.json()["prediction"]

        st.markdown("---")
        st.markdown("### Result")

        st.markdown(
            f"<h4 style='color:{colors[prediction]}'>Class: {prediction}</h4>",
            unsafe_allow_html=True
        )

        col1, col2 = st.columns([1, 2])

        with col1:
            if prediction in images:
                st.image(images[prediction], use_container_width=True)

        with col2:
            st.write(descriptions[prediction])

        st.markdown("### Comparison with average values")
        st.write(
            "The chart below compares the entered values with the average measurements of the three iris species."
        )

        chart_data = pd.DataFrame(
            {
                "Your input": [sepal_length, sepal_width, petal_length, petal_width],
                "Setosa avg": list(averages["setosa"].values()),
                "Versicolor avg": list(averages["versicolor"].values()),
                "Virginica avg": list(averages["virginica"].values()),
            },
            index=["Sepal length", "Sepal width", "Petal length", "Petal width"]
        )

        st.line_chart(chart_data)

        st.dataframe(chart_data)

    except Exception as e:
        st.error(f"Error: {e}")