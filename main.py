# in main.py
import time

import streamlit as st

name = st.text_input("Name")
name = name

st.query_params.names = name
time.sleep(0.1)

if st.button("switch"):
    st.switch_page("pages/a.py")
