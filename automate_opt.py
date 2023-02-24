import streamlit as st
import webbrowser as wb
import os
from PIL import Image

# Set directory path
os.chdir("C:\images")

# Get list of all files in directory
files = os.listdir()

# Iterate through each file
for file in files:
    # Check if file is an image (optional)
    if file.endswith(".png"):
        # Open file as image
        img = Image.open(file)
        # Display image
        st.image(img)

# create a function
def result():
    wb.open("https://github.com/Anianonymous/automation-bots")

    
name=st.text_input("enter your name: ")
if st.button("result"):
    # call the function
    result()
