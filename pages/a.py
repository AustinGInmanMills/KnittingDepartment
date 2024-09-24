import streamlit as st
import time

time.sleep(5)

st.rerun()

if "names" in st.query_params:
    st.write(st.query_params.names)