import pickle
import numpy as np
import streamlit as st

# import the trained linear regression from model.py
from model import regModel


# we format the layout so as to center the content
col0, col1, col2, col3, col4, col5, col6 = st.columns([1,1,1,2,1,1,1])

#we empty columns for spacing and aligning
with col0:
    st.write('')
with col1:
    st.write('')
with col2:
    st.write('') 
#the title at the center   
with col3:
    st.title("ⴍage") 
with col4:
    st.write('')
with col5:
    st.write('')
with col6:
    st.write('')
#centered title row.
col7, col8, col9 = st.columns(3)
with col7:
    st.write('')    
with col8:
    st.markdown("<h6 style='text-align: center;'>A simple web app to predict annual salary</h6>", unsafe_allow_html=True)
with col9:
    st.write('')

#Options for the user to input
gen_list = ["Female", "Male"]
edu_list = ["Bachelor's", "Master's", "PhD"]
job_list = ["Director of Marketing", "Director of Operations", "Senior Data Scientist", "Senior Financial Analyst", "Senior Software Engineer"]

#matching each job title to a numeric code for prediction.
job_idx = [0, 1, 10, 11, 20]

#we put widgets in which users can input where they lie
gender = st.radio('Pick your gender', gen_list)
age = st.slider('Pick your age', 21, 55)
education = st.selectbox('Pick your education level', edu_list)
job = st.selectbox('Pick your job title', job_list)
experience = st.slider('Pick your years of experience', 0.0, 25.0, 0.0, 0.5, "%1f")

#we create empty columns to centre the predict button
col10, col11, col12, col13, col14 = st.columns(5)
with col10:
    st.write('')
with col11:
    st.write('')    
with col12:
    predict_btn = st.button('Predict Salary')
with col13:
    st.write('')
with col14:
    st.write('')

if(predict_btn):
    inp1 = int(age)
    inp2 = float(experience)
    #map a job to its numeric code
    inp3 = int(job_idx[job_list.index(job)])
    #convert education to numeric index
    inp4 = int(edu_list.index(education))
    #convert gender to numeric index
    inp5 = int(gen_list.index(gender))

    #Put in the final input vector
    X = [inp1, inp2, inp3, inp4, inp5]
    #predict the salary using the trained regression model
    salary = regModel.predict([X])
    col15, col16, col17 = st.columns(3)
    with col15:
        st.write('') 
    #Display the result   
    with col16:
        st.text(f"Estimated salary: ${int(salary[0])}")
    with col17:
        st.write('')
