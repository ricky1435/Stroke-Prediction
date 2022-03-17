#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:53:42 2022

@author: ruthvikpvs
"""
import streamlit as st 
import numpy as np 
import requests
import pandas as pd

import streamlit as st
import pandas as pd
import pickle

with open("saved_steps1.pkl", "rb") as file:
    data = pickle.load(file)
    

model = data["model"]
encoder = data['encoder']
def show_predict_page():
    st.title("Stroke Prediction")
    st.write("Some Information before prediction of stroke")
    gender = ("Male","Female")
    married = ("Yes","No")
    work = ("Private", "Self-employed", "Govt_job", "children", "Never_worked")
    residence = ("Urban", "Rural")
    smoking = ("formerly smoked", "never smoked", "smokes", "Unknown")
    
    Gender = st.selectbox("Gender",gender)
    ever_married = st.selectbox("Married or not",married)
    work_type = st.selectbox("Work Type",work)
    residence_type = st.selectbox("Residence",residence)
    smoking_status = st.selectbox("Smoking status",smoking)
    age = st.slider("Age",0,90,50)
    bmi = st.slider("Body Mass Index",0,300,100)
    glucose = st.slider("Average Glucose Level",0,300,100)
    hypertension = st.selectbox("Hypertension yes or no?",(1,0))
    heart_disease = st.selectbox("Heart disease yes or no?",(1,0))
    
    ok = st.button("Stroke or not?")
    if ok:
       #X = np.array([[Gender,age,hypertension,heart_disease,ever_married,work_type,residence_type,glucose,bmi,smoking_status]])
       X = pd.DataFrame({
    'gender':[Gender],'age':[age],'hypertension':[hypertension],'heart_disease':[heart_disease],'ever_married':[ever_married],
    'work_type':[work_type],
    'Residence_type':[residence_type],'avg_glucose_level':[glucose],'bmi':[bmi],'smoking_status':[smoking_status]
})
       X = encoder.transform(X)
     
       stroke1 = model.predict(X)
       st.subheader(stroke1)
       
show_predict_page()
