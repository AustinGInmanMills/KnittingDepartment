import streamlit as st
st.write(st.query_params)
if not st.session_state.name:
    st.write("Name not found")
else:
    st.write(f"{st.session_state.name} found")
