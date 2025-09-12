import streamlit as st
import pandas as pd
import joblib

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
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(255, 255, 255, 0.3);
            z-index: -1;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set your image path here
set_bg_image("image/Toyota_bg.jpg")

# Load saved model
model = joblib.load("models/random_forest_pipeline.pkl")
    
#App Title
st.markdown(
    """
    <div style="background-color: rgba(255,255,255,0.85); padding: 20px; border-radius: 10px; text-align: center;">
        <h1 style="color: #1f77b4;">🚗 Toyota Corolla Price Prediction</h1>
        <p style="font-size: 16px;">Predict the price of a used Toyota Corolla based on its specifications.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")  # spacing

# User inputs
st.markdown("### Enter Car Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age (in months)", 1, 250, 60)
    km = st.number_input("Kilometers Driven", 0, 500000, 50000)
    hp = st.number_input("Horsepower (HP)", 40, 300, 100)
    cc = st.number_input("Engine Capacity (CC)", 800, 5000, 1600)

with col2:
    doors = st.selectbox("Doors", [2, 3, 4, 5])
    gears = st.selectbox("Gears", [4, 5, 6])
    weight = st.number_input("Weight (kg)", 800, 2000, 1200)
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])

automatic = st.selectbox("Transmission", ["Manual", "Automatic"])
automatic = 1 if automatic == "Automatic" else 0

#Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Price: ₹ {prediction:,.2f}")

