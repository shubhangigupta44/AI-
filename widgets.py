import streamlit as st
import pandas as pd
st.title("streamlit text input")
name = st.text_input("enter yr name:")
age = st.slider("select yr age:",0,100,25)
st.write(f"your age is {age}.")
if name:
    st.write(f"Hello,{name}")


uploaded_file = st.file_uploader("choose a csv file",type = "csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)