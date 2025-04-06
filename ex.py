import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import altair as alt
from PIL import Image
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Streamlit Features Demo",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Basic Elements", "Data Display", "Charts & Media", "Widgets", "Advanced Features"])

# Main page title
st.title("✨ Streamlit Features Demo")
st.markdown("This app showcases various features and components of Streamlit.")

if page == "Basic Elements":
    st.header("Basic UI Elements")
    
    # Text elements
    st.subheader("Text Elements")
    st.text("This is plain text")
    st.markdown("**Markdown** is supported with *formatting*")
    st.caption("This is a small caption")
    st.latex(r"e^{i\pi} + 1 = 0")
    st.code("def hello_world():\n    print('Hello, world!')")
    
    # Alert elements
    st.subheader("Alerts and Info Boxes")
    st.info("This is an informational message")
    st.success("This is a success message")
    st.warning("This is a warning message")
    st.error("This is an error message")
    
    # Expander
    with st.expander("Click to expand"):
        st.write("This content is hidden until expanded")
        st.markdown("- You can put any content here\n- Including charts and widgets")

elif page == "Data Display":
    st.header("Data Display Elements")
    
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

elif page == "Charts & Media":
    st.header("Charts and Media")
    
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

elif page == "Widgets":
    st.header("Interactive Widgets")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Input widgets
        st.subheader("Input Widgets")
        
        text_input = st.text_input("Text Input", "Type here...")
        st.write("You entered:", text_input)
        
        number = st.number_input("Number Input", min_value=0, max_value=100, value=50)
        st.write("Value:", number)
        
        slider_val = st.slider("Slider", 0, 100, 50)
        st.write("Slider value:", slider_val)
        
        select_option = st.selectbox(
            "Select an option",
            ["Option 1", "Option 2", "Option 3"]
        )
        st.write("You selected:", select_option)
        
        multiselect = st.multiselect(
            "Multiselect",
            ["Option A", "Option B", "Option C", "Option D"],
            ["Option A", "Option C"]
        )
        st.write("You selected:", multiselect)
    
    with col2:
        # More widgets
        st.subheader("More Widgets")
        
        if st.checkbox("Show additional options"):
            st.write("You enabled additional options!")
            
        radio_val = st.radio(
            "Choose one",
            ["Cat", "Dog", "Fish"],
            horizontal=True
        )
        st.write("You chose:", radio_val)
        
        color = st.color_picker("Choose a color", "#00f900")
        st.write("Selected color:", color)
        
        date = st.date_input("Select a date", datetime.now())
        st.write("Selected date:", date)
        
        time_val = st.time_input("Set a time")
        st.write("Selected time:", time_val)

elif page == "Advanced Features":
    st.header("Advanced Features")
    
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
st.caption("Made with ❤️ using Streamlit. Run with `streamlit run ex.py`")
