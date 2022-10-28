import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

html_8="""
<div style="background-color:#EE9513;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายข้อมูลดอกไม้</h5></center>
</div>
"""

st.markdown(html_8,unsafe_allow_html=True)
st.markdown("")

dt=pd.read_csv("./data/iris.csv")
st.write(dt.head(10))
data1 = dt['sepal.length'].sum()
data2 = dt['sepal.width'].sum()
data3 = dt['petal.length'].sum()
data4 = dt['petal.width'].sum()
dx=[data1,data2,data3,data4]
dx2=pd.DataFrame(dx, index=["d1", "d2", "d3", "d4"])
if st.button("แสดงการจินตทัศน์ข้อมูล"):
   st.area_chart(dx2)
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")


