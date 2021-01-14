import streamlit as st
import numpy as np
from PIL import Image
import cv2

# convert the image into pencil sketch


def pencilSketch(input_image):
    image_grey = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    image_invert = cv2.bitwise_not(image_grey)
    image_smoothing = cv2.GaussianBlur(
        image_invert, (21, 21), sigmaX=0, sigmaY=0)
    final_image = cv2.divide(image_grey, 255-image_smoothing, scale=256)
    return(final_image)


st.title("PencilScatcher App")
st.write('This web app is to help convert your photos to realistic Pencil Sketches')

# File uploader on sidebar

image = st.sidebar.file_uploader(
    "Upload your photo", type=['jpeg', 'jpg', 'png'])

if image is None:
    st.write("You have not uploaded any image")
else:
    input_image = Image.open(image)
    final_sketch = pencilSketch(np.array(input_image))
    st.write("**Input Photo**")
    st.image(image, use_column_width=True)
    st.write("**Output Pencil Photo**")
    st.image(final_sketch, use_column_width=True)
