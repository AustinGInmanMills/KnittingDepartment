import time
import streamlit as st

name = st.text_input("Name")
name = name

if st.button("switch"):
    st.query_params.names = name
    st.session_state.name = name
    time.sleep(1)
    st.switch_page("pages/a.py")
