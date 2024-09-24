import streamlit as st

st.rerun()

if "names" in st.query_params:
    st.write(st.query_params.names)