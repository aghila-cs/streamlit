import streamlit as st
import pandas as pd
import numpy as np

st.title("WELCOME")
x = st.slider('x')  # 👈 this is a widget

Y = st.slider('Y')
sum = x+Y
print(sum)
st.write('sum is',sum)