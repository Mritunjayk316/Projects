import streamlit as st
import pickle
import sklearn
import numpy as np

st.title("Welcome to price prediction")
st.header("Enter your car details")
from PIL import Image
img=Image.open("car.png")
st.image(img,width=50)

kms=st.number_input("Enter kms",0,10000,100)
car_age=st.number_input("Enter car age",0,50)
original_price=st.number_input("Enter the originalprice",100000,5000000)
fuel=st.radio("Select fuel type",('Petrol','Diesel','CNG'))
transmission=st.selectbox("Select Transmission Type",['Manual','Automatic'])
predict_click=st.button("Get The car price")

if predict_click==True:
    model=pickle.load(open("C:\\Users\\User\Desktop\\web development\\model.pkl",'rb'))
    if fuel=='Petrol':
        fuel=list([0,1])
    elif fuel=='Disel':
        fuel=list([1,0])
    else:
        fuel=list([0,0])
    
    if transmission=='Manual':
        transmission=1
    else:
        transmission=0
    
    #calling the model

    #load the test data into numpy array
    data=[np.array([kms,car_age,original_price,fuel[0],fuel[1],transmission])]

    #call the model to predict the price
    result=model.predict(data)

    #display the predicted price on the webpage
    st.success("The predict price"+str(result))
    
