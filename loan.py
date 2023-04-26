import streamlit as st
import pickle
import sklearn
import numpy as np

st.title("Loan approval")
st.header("Enter your loan details")

gender=st.selectbox("select gender",['male','female'])
applicant=st.number_input('Enter applicat income',0,50000)
coapplicant=st.number_input("Enter coapplicat income",0,5000)
total_income=st.number_input("Enter total income",0,50000)
predict_click=st.button("Get the loan status")

if predict_click==True:
    model=pickle.load(open("D:\\web development\\lr.pkl",'rb'))
    if gender=='Male':
        gender=1
    else:
        gender=0

 #load the test data into numpy array
    data=[np.array([gender,applicant,coapplicant,total_income])]

    #call the model to predict the price
    result=np.round(model.predict(data))

    #display the predicted price on the webpage
    st.success("loan status :"+str(result[0]))
    