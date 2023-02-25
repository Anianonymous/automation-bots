import streamlit as st
import webbrowser as wb
base="dark"
#enter your name
name=st.text_input("enter your name: ")
# choose your choice
choice=st.radio("select your required websites:",("Github","Blogger"))
fin=""
# create a function
def result():
    if choice=="Github":
        fin="https://github.com/Anianonymous/automation-bots"
    elif choice=="Blogger":
        fin="https://anoanymousphotos.blogspot.com/"
    else:
        fin="undefined"
    st.success(fin)
if st.button("result"):
    # call the function
    result()

