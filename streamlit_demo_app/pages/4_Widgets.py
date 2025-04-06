import streamlit as st
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Widgets - Streamlit Demo",
    page_icon="✨",
    layout="wide"
)

# Page header
st.title("Interactive Widgets")

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

# Footer
st.divider()
st.caption("Made with ❤️ using Streamlit") 