import streamlit as st
import time

placeholder = st.empty()


def page1():
    with placeholder.container():
        hey = st.button()
        if hey:
            st.write("Hello")
            time.sleep(3)
            placeholder.empty()
            time.sleep(2)
            page2()
    
def page2():
    with placeholder.container():
        hey = st.button()
        if hey:
            st.write("Bye")
            
            
            
            
page1()