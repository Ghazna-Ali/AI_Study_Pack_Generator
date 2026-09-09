import os

import streamlit as st


# ============================================================
# APPLICATION SETTINGS
# ============================================================

APP_NAME = "AI Study Pack Generator"

APP_VERSION = "1.0.0"

APP_DESCRIPTION = (
    "A multi-stage AI workflow that creates personalized "
    "study packs through planning, content generation, "
    "assessment, review, and refinement."
)


# ============================================================
# GEMINI SETTINGS
# ============================================================

# Keep the model in ONE place.
#
# If Google changes the recommended/current model,
# this is the only file you need to update.

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.5-flash",
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

def get_gemini_api_key() -> str:
    """
    Get the Gemini API key.

    Priority:
    1. Streamlit secrets
    2. Environment variable

    The API key is never hard-coded.
    """

    # Streamlit Cloud / local Streamlit
    try:
        api_key = st.secrets.get(
            "GEMINI_API_KEY"
        )

        if api_key:
            return str(api_key).strip()

    except Exception:
        pass

    # Environment variable fallback
    api_key = os.getenv(
        "GEMINI_API_KEY"
    )

    if api_key:
        return api_key.strip()

    raise RuntimeError(
        "GEMINI_API_KEY is not configured."
    )
