import streamlit as st

if "names" in st.query_params:
    st.write("Hello Austin")

st.write(st.query_params)