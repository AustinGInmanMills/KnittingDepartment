import streamlit as st
import time



placeholder = st.empty()

def page1():
    with placeholder.form("Hey"):
        submit = st.form_submit_button("click1")
        if submit: 
            st.write("hey")
            st.session_state.form1 = True
            time.sleep(1)
            placeholder.empty()
            time.sleep(1)
            page2()
        
def page2():
    with placeholder.form("Bye"):
        submit = st.form_submit_button("click2")
        if submit: 
            st.write("bye")
            st.session_state.form2 = True
            time.sleep(1)
            placeholder.empty()
            time.sleep(1)
            page1()
            
            
def test():
    st.write("hello")
            
st.button("1", on_click=test) 
st.button("2", on_click=page2)