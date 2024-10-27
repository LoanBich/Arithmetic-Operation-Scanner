import streamlit as st
from PIL import Image

from math_recognizer import MathRecognizer

# Initialize the MathRecognizer
math_recognizer = MathRecognizer()

# Streamlit app layout
st.title("Arithmetic Operations Scanner")
st.write("Upload an image containing arithmetic operations to get the result.")

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

    # Clean up the recognized operation text
    clean_operation = math_recognizer.clean_operation(operation_text)

    # Display the cleaned operation in LaTeX
    st.latex(clean_operation)

    # Calculate the result
    try:
        result = eval(clean_operation)
        st.write(f"Result: **{result}**")
    except Exception as e:
        st.write(f"Error in calculation: **{str(e)}**")
