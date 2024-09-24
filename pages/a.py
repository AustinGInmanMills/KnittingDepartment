import streamlit as st
import time

if "names" not in st.query_params:
    st.rerun()
else:
    st.write(st.query_params.names)