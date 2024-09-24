import streamlit as st
import time

placeholder = st.empty()
placeholder2 = st.empty()

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
    with placeholder2.form("Hello"):
        submit2 = st.form_submit_button()
        if submit2:
            st.write("Hello")
            
            
page1()