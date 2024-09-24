# in main.py
import streamlit as st

st.query_params.names = "Austin"
if st.button("switch"):
    st.switch_page("pages/a.py")