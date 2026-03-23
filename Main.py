# Main.py
import streamlit as st

def page2():
    st.title("Second page")

def page1():
    st.title("Login")
    password = st.text_input("Enter password", type="password")
    if password == "bob":
        st.switch_page(page2_obj)  # pass the st.Page object, not the callable

page1_obj = st.Page(page1, title="First page")
page2_obj = st.Page(page2, title="Second page", icon=":material/favorite:")

pg = st.navigation([page1_obj, page2_obj])
pg.run()
