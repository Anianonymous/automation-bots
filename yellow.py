import streamlit as st
import webbrowser as wb
op1=st.radio("select your required websites:",("Github","Blogger"))
def res():
    if op1=="Github":
        wb.open("https://github.com/Anianonymous/automation-bots")
    elif op1=="Blogger":
        wb.open("https://anoanymousphotos.blogspot.com/")
    else:
        st.text("try text time")
if st.button("result"):
    res()