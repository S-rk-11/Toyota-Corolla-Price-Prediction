import streamlit as st
import pandas as pd
import pickle

# Page Config
st.set_page_config(
    page_title="Toyota Corolla Price Prediction",
    page_icon="🚗",
    layout="centered"
)

#Background Image
def set_bg_image(image_path):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_path}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .stApp::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(255, 255, 255, 0.3); /* overlay */
            z-index: -1;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set your image path here
set_bg_image("image/Toyota_bg.jpg")

# Load saved model
with open("models/toyota_random_forest_pipeline.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Toyota Corolla Price Prediction 🚗")

# User inputs
year = st.number_input("Year of Manufacturing", 1990, 2025, 2010)
km = st.number_input("Kilometers Driven", 0, 500000, 50000)
hp = st.number_input("Horsepower (HP)", 50, 300, 100)
cc = st.number_input("Engine Capacity (CC)", 500, 5000, 1500)
doors = st.selectbox("Doors", [2, 3, 4, 5])
seats = st.selectbox("Seats", [2, 4, 5, 7])

input_df = pd.DataFrame({
    "Year": [year],
    "KM": [km],
    "HP": [hp],
    "CC": [cc],
    "Doors": [doors],
    "Seats": [seats]
})

if st.button("Predict Price"):
    prediction = model.predict(input_df)
    st.success(f"Estimated Price: ₹ {prediction[0]:,.2f}")
