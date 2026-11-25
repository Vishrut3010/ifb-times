from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="The IFB Times",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's own UI and make the page fill exactly one window,
# with no extra scrollable blank space below it.
st.markdown(
    """
    <style>
    html, body, .stApp, [data-testid="stAppViewContainer"],
    [data-testid="stMain"], section.main {
        height: 100dvh !important;
        overflow: hidden !important;
    }
    #MainMenu, header, footer,
    [data-testid="stHeader"], [data-testid="stToolbar"],
    [data-testid="stDecoration"], [data-testid="stStatusWidget"] {
        display: none !important;
        height: 0 !important;
    }
    .block-container, [data-testid="stMainBlockContainer"] {
        padding: 0 !important;
        max-width: 100% !important;
    }
    /* remove the gap Streamlit puts between elements */
    [data-testid="stVerticalBlock"] {gap: 0 !important;}
    /* the hidden file-watcher must take no space */
    [data-testid="stElementContainer"]:has(> [data-testid="stFragment"]),
    [data-testid="stElementContainer"]:not(:has(iframe)) {
        height: 0 !important; min-height: 0 !important;
        margin: 0 !important; padding: 0 !important; overflow: hidden !important;
    }
    iframe {
        display: block;
        height: 100dvh !important;
        width: 100% !important;
        border: 0 !important;
    }
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
