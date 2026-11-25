from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

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


@st.fragment(run_every=2)
def watch_for_changes():
    """Re-run the app whenever index.html changes on disk (local use)."""
    mtime = PAGE.stat().st_mtime
    if st.session_state.get("page_mtime") not in (None, mtime):
        st.session_state["page_mtime"] = mtime
        st.rerun()
    st.session_state["page_mtime"] = mtime


# Read the file fresh on every run (no static-file caching)
components.html(PAGE.read_text(encoding="utf-8"), height=900, scrolling=False)
watch_for_changes()
