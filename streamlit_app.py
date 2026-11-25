from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="The IFB Times",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's own header/footer and make the quiz fill the whole window
st.markdown(
    """
    <style>
    #MainMenu, header, footer {visibility: hidden; height: 0;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    iframe {height: 100vh !important; border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

PAGE = Path(__file__).parent / "index.html"

try:
    st.iframe(PAGE, height=900)  # Streamlit 1.56+
except AttributeError:  # older Streamlit versions
    import streamlit.components.v1 as components

    components.html(PAGE.read_text(encoding="utf-8"), height=900, scrolling=False)
