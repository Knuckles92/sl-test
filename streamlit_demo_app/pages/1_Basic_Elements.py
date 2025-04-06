import streamlit as st

# Set page config
st.set_page_config(
    page_title="Basic Elements - Streamlit Demo",
    page_icon="✨",
    layout="wide"
)

# Page header
st.title("Basic UI Elements")

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

# Footer
st.divider()
st.caption("Made with ❤️ using Streamlit") 