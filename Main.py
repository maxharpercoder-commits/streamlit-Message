import streamlit as st
password = ""
def page2():
    st.text('Messages is unlocked')
def page1():
    st.text('Messages is locked')
    password = st.text_input('Enter the password to unlock Messages', type='password')
if password == "RUNEATM11@#":
    pg = st.navigation([
    st.Page(page1, title="First page", icon="🔥"),
    st.Page(page2, title="Second page", icon=":material/favorite:"),
    ])
else:
    pass
pg.run()
