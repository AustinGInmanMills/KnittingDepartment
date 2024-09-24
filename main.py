import streamlit as st
import time

placeholder1 = st.empty()
placeholder2 = st.empty()


def page1():
    with st.container():
        hey = st.button("1")
        if hey:
            st.write("Hello")
            
            page2()
    
def page2():
    with st.container():
        bye = st.button("2")
        if bye:
            st.write("Bye")
            

            
            
            
            
page1()