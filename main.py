import streamlit as st
import time

placeholder = st.empty()

def page1():
    with placeholder.form("Hey"):
        submit = st.form_submit_button("click1")
        if submit: 
            st.write("hey")
            st.session_state.form1 = False
            time.sleep(2)
            placeholder.empty()
            time.sleep(0)
            page2()
        
def page2():
    with placeholder.form("Bye"):
        submit = st.form_submit_button("click2")
        if submit: 
            st.write("bye")

if not "form1" in st.session_state:
    page1()
else:
    page2()

