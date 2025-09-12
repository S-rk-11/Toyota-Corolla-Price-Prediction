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
    "<style>\n"
    ".stApp {\n"
    "  background-image: url('image/Toyota_bg.jpg');\n"
    "  background-size: cover;\n"
    "  background-position: center;\n"
    "  background-repeat: no-repeat;\n"
    "  background-attachment: fixed;\n"
    "}\n"
    ".stApp::before {\n"
    "  content: '';\n"
    "  position: absolute;\n"
    "  top: 0;\n"
    "  left: 0;\n"
    "  width: 100%;\n"
    "  height: 100%;\n"
    "  background-color: rgba(255, 255, 255, 0.3);\n"
    "  z-index: -1;\n"
    "}\n"
    "</style>",
    unsafe_allow_html=True
)

# Set your image path here
set_bg_image("image/Toyota_bg.jpg")

# Load saved model
with open ("models/random_forest_model.pkl", "rb") as f:
  model = pickle.load(f)

with open ("models/scaler_model.pkl", "rb") as f:
  scaler = pickle.load(f)
    
#App Title
st.title("Toyota Corolla Price Prediction 🚗")

# User inputs
year = st.number_input("Year of Manufacturing", 1990, 2025, 2010)
km = st.number_input("Kilometers Driven", 0, 500000, 50000)
hp = st.number_input("Horsepower (HP)", 50, 300, 100)
cc = st.number_input("Engine Capacity (CC)", 500, 5000, 1500)
doors = st.selectbox("Doors", [2, 3, 4, 5])
seats = st.selectbox("Seats", [2, 4, 5, 7])

# Create Input DataFrame
input_df = pd.DataFrame({
    "Year": [year],
    "KM": [km],
    "HP": [hp],
    "CC": [cc],
    "Doors": [doors],
    "Seats": [seats]
})

#Prediction
if st.button("Predict Price"):
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]
    st.success(f"Estimated Price: ₹ {prediction:,.2f}")

