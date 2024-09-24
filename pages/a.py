import streamlit as st
import time

from streamlit import rerun

rerun()
st.write(st.query_params)
time.sleep(5)
st.write(st.query_params)
