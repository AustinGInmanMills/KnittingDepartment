import streamlit as st

def page1():
    placeholder = st.empty()
    with placeholder.form("Bye"):
    submit = st.form_submit_button
        if submit:
            st.write("Bye")
            time.sleep(3)
            placeholder.empty()
            page2()
    
def page2():
    placeholder = st.empty()
    submit = st.form_submit_button
    with submit:
        if st.form_submit_button:
            st.write("Hello")
            
            
page1()