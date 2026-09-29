import streamlit as st
import pandas as pd
import joblib

model = joblib.load("housing_model.pkl")
columns = joblib.load("model_columns.pkl")

st.title("Sydney Housing Price Predictor")

suburb = st.selectbox("Suburb", ["Bankstown", "Manly", "Parramatta"])
property_type = st.selectbox("Property Type", ["Apartment", "House"])

beds = st.number_input("Bedrooms", 1, 10, 2)
baths = st.number_input("Bathrooms", 1, 10, 1)
parking = st.number_input("Parking", 0, 10, 1)
floor_size = st.number_input("Floor Size (m²)", 20.0, 500.0, 100.0)
sale_month = st.number_input("Sale Month", 1, 12, 9)
sale_day = st.number_input("Sale Day", 1, 31, 15)

if st.button("Predict Price"):
    data = pd.DataFrame([{
        "Beds": beds,
        "Baths": baths,
        "Parking": parking,
        "Floor_size_m2": floor_size,
        "Sale_Month": sale_month,
        "Sale_Day": sale_day,
        "Suburb_Manly": int(suburb == "Manly"),
        "Suburb_Parramatta": int(suburb == "Parramatta"),
        "Property_Type_House": int(property_type == "House")
    }])

    data = data[columns]
    prediction = model.predict(data)[0]

    st.success(f"Predicted Sale Price: ${prediction:,.0f}")