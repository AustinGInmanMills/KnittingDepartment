import streamlit as st
import time

if "names" in st.query_params:
    st.write(st.query_params.names)