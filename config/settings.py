import os
import streamlit as st


APP_NAME = "AI Study Pack Generator"
APP_VERSION = "1.0.0"

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "openai/gpt-oss-120b"
)

MAX_API_RETRIES = 3
MAX_REFINEMENT_ITERATIONS = 2
RETRY_BASE_DELAY = 2


def get_groq_api_key() -> str:
    try:
        api_key = st.secrets.get("GROQ_API_KEY")
    except Exception:
        api_key = None

    if not api_key:
        api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not configured."
        )

    return api_key