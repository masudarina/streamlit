import streamlit as st
from PIL import Image

st.title("Welcome to our page✨")
st.write("Find a plce you wanna visit this summer!")
image = Image.open("malta.png")

st.image(image, caption='Malta Island',use_column_width=True)

