import streamlit as st
import time

def page1():
    placeholder = st.empty()
    with placeholder.form("Bye"):
        submit = st.form_submit_button()
        if submit:
            st.write("Bye")
            time.sleep(3)
            placeholder.empty()
            time.sleep(1)
            page2()
    
def page2():
    placeholder2 = st.empty()
    with placeholder2.form("Bye"):
        submit = st.form_submit_button()
        if submit:
            st.write("Hello")
            
            
page1()