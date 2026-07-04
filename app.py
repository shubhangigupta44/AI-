import streamlit as st
import pandas as pd
import numpy as np
st.title("hello streamlit")
st.write("this is a simple text")
df = pd.DataFrame({
    'first column' : [1,2,3],
    'second column' : [10,20,30]

})
st.write("here is the dataframe")
st.write(df)
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)