# in main.py
import streamlit as st

st.query_params.from_dict({"bar": "foo"})
if st.button("switch"):
    st.switch_page("pages/a.py")