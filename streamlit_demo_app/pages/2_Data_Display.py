import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(
    page_title="Data Display - Streamlit Demo",
    page_icon="✨",
    layout="wide"
)

# Page header
st.title("Data Display Elements")

# Generate sample dataframe
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Age': [24, 32, 18, 47, 29],
    'City': ['New York', 'Paris', 'London', 'Tokyo', 'Berlin'],
    'Score': [88, 75, 92, 65, 89]
})

# Display dataframe
st.subheader("DataFrame Display")
st.dataframe(df, use_container_width=True)

# Metrics
st.subheader("Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Humidity", "86%", "-4%")
col3.metric("Wind", "7 mph", "2 mph")

# Tables
st.subheader("Static Table")
st.table(df.head(3))

# JSON
st.subheader("JSON Display")
st.json({
    "name": "John",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "SQL", "JavaScript"]
})

# Footer
st.divider()
st.caption("Made with ❤️ using Streamlit") 