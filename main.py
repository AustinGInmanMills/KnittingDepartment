import streamlit as st
import time

placeholder1 = st.empty()
placeholder2 = st.empty()



    
st.checkbox("test")

if st.button("click me"):
    st.write("yep")
    if st.rerun():
        st.write("app reruned")