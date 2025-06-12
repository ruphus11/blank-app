import streamlit as st
import datetime

min_date = datetime.date(1900, 1, 1)
max_date = datetime.date(2100, 12, 12)
today = datetime.datetime.now

st.title("🎈Title: Bio Data")
st.write(
    "This is a sample web app")

first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Your age", 0, 100, 30, 1)
dob = st.date_input("Your birthday", "today", min_date, max_date)
marital_status = st.radio("Marital status", ["Single", "Married"])
years_of_experience = st.slider("Years of experience", 0, 40)
