import streamlit as st
from latex2sympy2 import latex2sympy
from PIL import Image
from sympy import *

from math_recognizer import MathRecognizer

# Initialize the MathRecognizer
math_recognizer = MathRecognizer()

# Streamlit app layout
st.title("AI Math Calculator")
st.write("Upload an image containing operations to get the result.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Load and display the image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Process the image
    st.write("Processing...")
    operation_text = math_recognizer.recognize(image)

    # Display recognized text
    st.write(f"Recognized Operation: **{operation_text}**")

    # Display the Sympy operation
    st.latex(latex2sympy(operation_text))

    # Calculate the result
    try:
        result = N(latex2sympy(operation_text))
        st.write(f"Result: **{result}**")
    except Exception as e:
        st.write(f"Error in calculation: **{str(e)}**")
