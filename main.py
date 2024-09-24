import streamlit as st
import time

placeholder = st.empty()


def page1():
    with placeholder.container("Bye"):
        submit = st.button()
        if submit:
            st.write("Bye")
            time.sleep(3)
            placeholder.empty()
            time.sleep(1)
            page2()
    
def page2():
    with placeholder2.container("Hello"):
        submit2 = st.button()
        if submit2:
            st.write("Hello")
            
            
page1()