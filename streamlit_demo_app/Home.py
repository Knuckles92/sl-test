import streamlit as st

# Set page config
st.set_page_config(
    page_title="Streamlit Features Demo",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page title
st.title("✨ Streamlit Features Demo")
st.markdown("This app showcases various features and components of Streamlit.")

# Home page content
st.header("Welcome to the Streamlit Demo App!")
st.write("""
This multi-page app demonstrates the various features and capabilities of Streamlit.
Use the sidebar navigation to explore different sections.
""")

# Navigation instructions
st.subheader("Navigation")
st.write("""
The sidebar on the left shows all available pages:
- **Basic Elements**: Text, markdown, alerts, and basic UI components
- **Data Display**: DataFrames, tables, metrics, and JSON display
- **Charts & Media**: Various visualization options and media display
- **Widgets**: Interactive input components and controls
- **Advanced Features**: Progress bars, file uploads, caching, and session state
""")

# Footer
st.divider()
st.caption("Made with ❤️ using Streamlit. Run with `streamlit run Home.py`") 