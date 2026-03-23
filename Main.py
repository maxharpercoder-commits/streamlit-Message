# streamlit_app.py
import streamlit as st
def page2():
    st.title("Second page")
def page1():
    st.title("Login")
    password = st.text_input("Enter password", type="password")
    if password == "bob":
        st.switch_page(page2())



pg = st.navigation([st.Page(page1, title="Login"), st.Page(page2, title="Second page")])
pg.run()
