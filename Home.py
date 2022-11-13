import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import pickle

st.image('./pic/004.jpg')

html_8="""
<div style="background-color:#EE9513;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายข้อมูลคุณภาพนม</h5></center>
</div>
"""

st.markdown(html_8,unsafe_allow_html=True)
st.markdown("")

dt=pd.read_csv("./data/milknew.csv")
st.write(dt.head(10))

data1 = dt['pH'].sum()
data2 = dt['Temprature'].sum()
data3 = dt['Taste'].sum()
data4 = dt['Odor'].sum()
data5 = dt['Fat'].sum()
data6 = dt['Turbidity'].sum()
data7 = dt['Colour'].sum()

dx=[data1,data2,data3,data4,data5,data6,data7]
dx2=pd.DataFrame(dx, index=["d1", "d2", "d3", "d4", "d5", "d6", "d7"])

if st.button("แสดงการจินตทัศน์ข้อมูล"):
   st.area_chart(dx2)
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")

html_8="""
<div style="background-color:#EE9513;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายข้อมูล</h5></center>
</div>
"""
st.markdown(html_8,unsafe_allow_html=True)
st.markdown("")

pH=st.slider("กรุณาเลือกข้อมูล pH")
Tture=st.slider("กรุณาเลือกข้อมูล Temprature")
Tae=st.number_input("กรุณาเลือกข้อมูล Taste")
Or=st.number_input("กรุณาเลือกข้อมูล Odor")
Fat=st.slider("กรุณาเลือกข้อมูล Fat")
Tty=st.number_input("กรุณาเลือกข้อมูล Turbidity")
Col=st.number_input("กรุณาเลือกข้อมูล Colour")

if st.button("ทำนายผล"):
   loaded_model = pickle.load(open('./data/milk_model.sav', 'rb'))
   input_data =  (pH,Tture,Tae,Or,Fat,Tty,Col)
   # changing the input_data to numpy array
   input_data_as_numpy_array = np.asarray(input_data)
   # reshape the array as we are predicting for one instance
   input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
   prediction = loaded_model.predict(input_data_reshaped)
   st.write(prediction)
   
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")

    