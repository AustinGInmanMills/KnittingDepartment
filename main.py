import streamlit as st
import time

placeholder1 = st.empty()
placeholder2 = st.empty()



    
def page2():
    with st.container():
        bye = st.button("2")
        if bye:
            st.write("Bye")
            

            
            
            
            
with st.container():
        hey = st.button("1")
        if hey:
            st.write("Hello")
            
            page2()