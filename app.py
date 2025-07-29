import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Title
st.title("🚗 Car Price Prediction App")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("car data.csv")
    return df

df = load_data()

# Preprocessing
df['Car_Age'] = 2025 - df['Year']
df = df.drop(['Year', 'Car_Name'], axis=1)

# Encode categorical features
le = LabelEncoder()
for col in ['Fuel_Type', 'Selling_type', 'Transmission']:
    df[col] = le.fit_transform(df[col])

X = df.drop(['Selling_Price'], axis=1)
y = df['Selling_Price']

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X, y)

# Sidebar Inputs
st.sidebar.header("Enter Car Details")

present_price = st.sidebar.number_input("Present Price (in lakhs)", 0.0, 50.0, step=0.5)
kms_driven = st.sidebar.number_input("Kilometers Driven", 0, 300000, step=500)
fuel_type = st.sidebar.selectbox("Fuel Type", df['Fuel_Type'].unique())
seller_type = st.sidebar.selectbox("Seller Type", df['Selling_type'].unique())
transmission = st.sidebar.selectbox("Transmission", df['Transmission'].unique())
owner = st.sidebar.selectbox("Owner (0 = First, 1 = Second, 2 = Third)", df['Owner'].unique())
car_age = st.sidebar.slider("Car Age", 0, 25, 5)

# Encode inputs (match with training)
input_df = pd.DataFrame({
    'Present_Price': [present_price],
    'Driven_kms': [kms_driven],
    'Fuel_Type': [fuel_type],
    'Selling_type': [seller_type],
    'Transmission': [transmission],
    'Owner': [owner],
    'Car_Age': [car_age]
})

# Apply label encoding same as training
for col in ['Fuel_Type', 'Selling_type', 'Transmission']:
    input_df[col] = le.fit(df[col]).transform(input_df[col])

# Predict
if st.button("Predict Selling Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Selling Price: ₹ {prediction:.2f} lakhs")
