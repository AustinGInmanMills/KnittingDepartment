import streamlit as st
import time

time.sleep(2)

if "names" not in st.query_params:
    st.rerun()
else:
    st.write(st.query_params.names)
