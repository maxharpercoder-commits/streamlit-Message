import streamlit as st
password = ""
def page2():
    st.text('Messages is unlocked')
def page1():
    st.text('Messages is locked')
    pg.run()
pg = st.navigation([
st.Page(page1, title="First page", icon="🔥"),
st.Page(page2, title="Second page", icon=":material/favorite:"),
    ])
password = ""


