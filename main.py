import streamlit as st
import time

placeholder1 = st.empty()
placeholder2 = st.empty()



    

with st.form("help"):
    st.write("help")
   with st.form_submit_button("click"):
      st.write("agaha")

if st.button("click me"):
    st.write("yep")
    