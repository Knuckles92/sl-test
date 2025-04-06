import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
from PIL import Image

# Set page config
st.set_page_config(
    page_title="Charts & Media - Streamlit Demo",
    page_icon="✨",
    layout="wide"
)

# Page header
st.title("Charts and Media")

# Line chart
st.subheader("Line Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

# Bar chart
st.subheader("Bar Chart")
bar_data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [5, 9, 3, 7, 4]
})
st.bar_chart(bar_data.set_index('Category'))

# Matplotlib
st.subheader("Matplotlib Integration")
fig, ax = plt.subplots()
x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), label='sin(x)')
ax.plot(x, np.cos(x), label='cos(x)')
ax.legend()
st.pyplot(fig)

# Altair
st.subheader("Altair Chart")
alt_data = pd.DataFrame({
    'x': range(10),
    'y': range(10)
})
chart = alt.Chart(alt_data).mark_circle().encode(
    x='x',
    y='y',
    size='y',
    color='y'
).interactive()
st.altair_chart(chart, use_container_width=True)

# Images
st.subheader("Image Display")
st.write("Streamlit can display images from URLs or local files")
# Create a simple image for demo
img_array = np.zeros((100, 100, 3), dtype=np.uint8)
img_array[:50, :50] = [255, 0, 0]  # Red square
img_array[:50, 50:] = [0, 255, 0]  # Green square
img_array[50:, :50] = [0, 0, 255]  # Blue square
img_array[50:, 50:] = [255, 255, 0]  # Yellow square
img = Image.fromarray(img_array)
st.image(img, caption="Sample image created with NumPy")

# Footer
st.divider()
st.caption("Made with ❤️ using Streamlit") 