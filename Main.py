import streamlit as st
def page2():
    st.title("Second page")

def page1():
    st.title("Messaged is locked")
    global password=st.text_input("enter password")
    if password=="bob":
        st.Page(page2, title="Second page", icon=":material/favorite:"),

