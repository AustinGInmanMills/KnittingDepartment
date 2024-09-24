# in main.py
import streamlit as st

name = st.text_input("Name")
name = name
st.query_params.names = name

if st.button("switch"):
    st.switch_page("pages/a.py")
