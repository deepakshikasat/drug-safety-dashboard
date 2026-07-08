import pandas as pd
import streamlit as st

st.title("Drug Safety Dashboard")
st.caption("Demo dashboard structure for public FDA FAERS adverse event profiles.")
matrix = pd.read_csv("data/faers_demo_matrix.csv", index_col=0)
drug = st.selectbox("Drug", matrix.index)
st.bar_chart(matrix.loc[drug])
st.dataframe(matrix)
