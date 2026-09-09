import os
import streamlit as st


# ============================================================
# APPLICATION SETTINGS
# ============================================================

APP_NAME = "AI Study Pack Generator"

APP_VERSION = "1.0.0"

APP_DESCRIPTION = (
    "A multi-stage AI-powered study pack generator using Groq."
)


# ============================================================
# GROQ SETTINGS
# ============================================================

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "llama-3.3-70b-versatile",
)


# ============================================================
# WORKFLOW SETTINGS
# ============================================================

MAX_API_RETRIES = 3

MAX_REFINEMENT_ITERATIONS = 2

RETRY_BASE_DELAY = 2


# ============================================================
# API KEY
# ============================================================

def get_groq_api_key() -> str:
    """
    Get the Groq API key from Streamlit Secrets
    or an environment variable.
    """

    try:
        api_key = st.secrets.get("GROQ_API_KEY")
    except Exception:
        api_key = None

    if not api_key:
        api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not configured. "
            "Add it to Streamlit Cloud Secrets."
        )

    return api_key