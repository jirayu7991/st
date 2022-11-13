import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import pickle

st.image('./pic/005.png')

html_8="""
<div style="background-color:#66CCCC;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:Bisque">
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
<div style="background-color:#66CCCC;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:Bisque">
<center><h5>การทำนายข้อมูล</h5></center>
</div>
"""
st.markdown(html_8,unsafe_allow_html=True)
st.markdown("")

pH=st.number_input("กรุณาเลือกข้อมูล pH")
Tture=st.slider("กรุณาเลือกข้อมูล Temprature")
Tae= st.radio("กรุณาเลือกข้อมูล Taste: 0 ไม่เหมาะสม, 1 เหมาะสม",(0, 1))
Or= st.radio("กรุณาเลือกข้อมูล Odor: 0 ไม่เหมาะสม, 1 เหมาะสม",(0, 1))
Fat= st.radio("กรุณาเลือกข้อมูล Fat: 0 ไม่เหมาะสม, 1 เหมาะสม",(0, 1))
Tty= st.radio("กรุณาเลือกข้อมูล Turbidity: 0 ไม่เหมาะสม, 1 เหมาะสม",(0, 1))
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
   if prediction == 'low':
        st.image('./pic/20-percent.png')
   elif prediction == 'medium':
        st.image('./pic/50-percent.png')
   else:
        st.image('./pic/100-percent.png')
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")
