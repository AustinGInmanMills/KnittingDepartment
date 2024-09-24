import streamlit as st
import time

placeholder = st.empty()

def page1():
    with placeholder.form("Bye"):
        submit = st.form_submit_button()
        if submit:
            st.write("Bye")
            time.sleep(3)
            placeholder.empty()
            time.sleep(1)
            page2()
    
def page2():
    with placeholder.form("Hello"):
        submit = st.form_submit_button()
        if submit:
            st.write("Hello")
            
            
page1()