import pickle
import streamlit as st
import numpy as np
import pandas as pd
model=pickle.load(open('model.pkl','rb'))
st.header('Calories Burned Calculator ')
gender=st.selectbox('Select gender',('Male','Female'))
if gender=='Male':
    g=0
if gender=='Female':
    g=1
age=st.number_input('Enter Age')
height=st.number_input('Enter Height')
weight=st.number_input('Enter Weight')
duration=st.number_input('Enter Workout Duration')
heartrate=st.number_input('Enter HeartRate')
bodytemp=st.number_input('Enter BodyTemperature')
prediction=model.predict(pd.DataFrame(columns=['Gender','Age','Height','Weight','Duration','Heart_Rate','Body_Temp'],data=np.array([g,age,height,weight,duration,heartrate,bodytemp]).reshape(1,7)))
if(st.button("Predict")):
    st.write('Calories Burned')
    st.success(prediction)