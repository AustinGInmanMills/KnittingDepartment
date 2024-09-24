import streamlit as st
import time

placeholder = st.empty()


def page1():
    with placeholder.container("Hey"):
        hey = st.button("1")
        if hey:
            st.write("Hello")
            
            page2()
    
def page2():
    with placeholder.container():
        bye = st.button("2")
        if bye:
            st.write("Bye")
            

            
            
            
            
page1()