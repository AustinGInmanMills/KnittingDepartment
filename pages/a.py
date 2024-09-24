import streamlit as st

if st.query_params.names == "Austin":
    st.write("Hello Austin")

st.write(st.query_params)