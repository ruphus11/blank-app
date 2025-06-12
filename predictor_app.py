import streamlit as st
import csv
from model import regModel

job_list = []
gend_list = []
edu_list = []
with open("salaryData.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        job = row[3]
        gend = row[1]
        edu = row[2]
        if job not in job_list:
            job_list.append(job)
        if gend not in gend_list:
            gend_list.append(gend)
        if edu not in edu_list:
            edu_list.append(edu)


job_index = []
for i in job_list:
    job_index.append(job_list.index(i))


st.title("ⴍage")

st.write("A simple web app to predict salary")
gender = st.radio("Pick your gender", gend_list)
age = st.slider("Pick your age", 21, 55)
education = st.selectbox("Pick your education level", edu_list )
job_title = st.selectbox("Pick your job title", job_list)
experience = st.slider("Pick your years of experience", 0.0, 25.0, 0.0, 0.5, "%1f")

predict_button = st.button("Predict salary")

if predict_button:
    input1 = int(gend_list.index(gender))
    input2 = int(age)
    input3 = int(edu_list.index(education))
    input4 = int(job_index[job_list.index(job_title)])
    input5 = float(experience)

    X = [input1, input2, input3, input4, input5]
    salary = regModel.predict([X])

    st.text(f"Estimate salary: ${int(salary[0])}")
