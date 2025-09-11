import streamlit as st
import pandas as pd
import pickle

# Load saved model
with open("models/toyota_random_forest_pipeline.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Toyota Corolla Price Prediction 🚗")

# Example inputs
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
