import streamlit as st
from PIL import Image

st.title("Welcome to our page")
st.write("Find a plce you wanna visit this summer!")
image = Image.open('C:\Users\Systena\Pictures\ダウンロード.jfif')

st.image(image, caption='サンプル',use_column_width=True)

st.markdown("# Head1")
st.markdown("## Head2")
