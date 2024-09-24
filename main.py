# in main.py
import time

import streamlit as st

name = st.text_input("Name")
name = name

if st.button("switch"):
    st.query_params.names = name
    time.sleep(3)
    st.switch_page("pages/a.py")
