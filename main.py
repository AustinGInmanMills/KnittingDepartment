# in main.py
import streamlit as st

name = st.text_input("Name")
name = name
st.experimental_set_query_params(
    name=name,
)
if st.button("switch"):
    st.switch_page("pages/a.py")
