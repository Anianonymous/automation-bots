import streamlit as st
import webbrowser as wb
base="dark"
#enter your name
name=st.text_input("enter your name: ")
# choose your choice
choice=st.radio("select your required websites:",("Github","Blogger"))

# create a function
def result():
    if choice=="Github":
        wb.open("https://github.com/Anianonymous/automation-bots")
    elif choice=="Blogger":
        wb.open("https://anoanymousphotos.blogspot.com/")
    else:
        pass

if st.button("result"):
    # call the function
    result()
# import streamlit as st
# base="dark"

# st.write("---")
# n1=st.number_input(label="enter your first number: ")
# def fin():
#     st.success(n1)
# if st.button('final'):
#     fin()
