import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("housepredmodel.pkl", "rb"))

st.title("🏠 House Price Prediction App")

# Inputs
sqft = st.number_input("Square Feet", min_value=500, max_value=10000, step=100)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10)
age = st.number_input("House Age", min_value=0, max_value=50)

# Predict button
if st.button("Predict Price"):
    input_data = np.array([[sqft, bedrooms, age]])
    prediction = model.predict(input_data)
    
    st.success(f"Estimated Price: ₹ {prediction[0]:,.2f}")