import streamlit as st
st.write(st.query_params)
if st.query_params.values() == "Austin":
    st.write("Austin Found!!!!")
