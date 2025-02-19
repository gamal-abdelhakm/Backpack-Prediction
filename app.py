# bulid streamlit app
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# read model
model = joblib.load('model.pkl')
df = pd.DataFrame()
# sidebar

st.sidebar.header('User Input Parameters')

cat_cols = ['Brand', 'Material', 'Size', 'Compartments', 'Laptop Compartment', 'Waterproof','Style', 'Color']
for col in cat_cols:
    user_input = st.sidebar.selectbox(col, cat_cols)
    df[col] = user_input

num_cols = ['Weight Capacity (kg)']
for col in num_cols:
    user_input = st.sidebar.number_input(col)
    df[col] = user_input

print(df)

# button for prediction
if st.button('Predict'):
    result = model.predict(df)
    st.write(result)