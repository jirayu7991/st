import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

st.header("Jirayu")
st.subheader("Sittichai")

html_8="""
<div style="background-color:#EE9513;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>เกณฑ์การให้คะแนน 4</h5></center>
</div>
"""
st.markdown(html_8,unsafe_allow_html=True)
st.markdown("")
dx=pd.read_excel('./data/gen.xlsx')
st.dataframe(dx)

dt=pd.read_csv('./data/iris.csv')
st.dataframe(dt)

data1 = data['sepal.length'].sum()
data2 = data['sepal.width'].sum()
data3 = data['petal.length'].sum()
data4 = data['petal.width'].sum()
dx=[data1,data2,data3,data4]
dx2=pd.DataFrame(dx, index=["d1", "d2", "d3", "d4"])

st.bar_chart(dx2)
st.balloons()



st.sidebar.markdown("# วิเคราะห์รายบุคคล ")



