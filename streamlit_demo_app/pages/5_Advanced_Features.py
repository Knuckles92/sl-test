import streamlit as st
import pandas as pd
import time

# Set page config
st.set_page_config(
    page_title="Advanced Features - Streamlit Demo",
    page_icon="✨",
    layout="wide"
)

# Page header
st.title("Advanced Features")

# Progress bar
st.subheader("Progress Bar")
progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

if st.button("Run Progress Demo"):
    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 1, text=f"{progress_text} {percent_complete+1}%")
    st.success("Completed!")

# File uploader
st.subheader("File Uploader")
uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt", "xlsx"])
if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
            st.write("Preview of uploaded CSV:")
            st.dataframe(df.head())
        elif uploaded_file.name.endswith('.txt'):
            stringio = uploaded_file.getvalue().decode("utf-8")
            st.write("Content of uploaded text file:")
            st.text(stringio)
    except Exception as e:
        st.error(f"Error processing file: {e}")

# Caching example
st.subheader("Function Caching")
st.write("This helps improve app performance by caching function results")

@st.cache_data
def expensive_computation(n):
    # Simulate an expensive operation
    time.sleep(2)
    return n ** 2

number = st.number_input("Enter a number to square", value=10)
if st.button("Compute Square"):
    with st.spinner("Computing..."):
        result = expensive_computation(number)
        st.success(f"The square of {number} is {result}")
        st.info("Note: If you enter the same number again, the result is instant due to caching")

# Session state example
st.subheader("Session State")
st.write("Keeps widget values between reruns")

if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button("Increment Counter")
if increment:
    st.session_state.count += 1

st.write(f"Count: {st.session_state.count}")

if st.button("Reset Counter"):
    st.session_state.count = 0
    st.experimental_rerun()

# Footer
st.divider()
st.caption("Made with ❤️ using Streamlit") 