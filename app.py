import streamlit as st

from config.settings import (
    APP_NAME,
    APP_VERSION,
    APP_DESCRIPTION,
    get_groq_api_key,
)

from ui.components import (
    render_header,
    render_inputs,
)

from ui.results import render_results

from workflow.runner import (
    run_workflow,
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title=APP_NAME,
    page_icon="📚",
    layout="wide",
)


# ============================================================
# SESSION STATE
# ============================================================

if "study_pack" not in st.session_state:
    st.session_state.study_pack = None


# ============================================================
# HEADER
# ============================================================

render_header()

st.caption(
    f"Version {APP_VERSION} — {APP_DESCRIPTION}"
)

st.divider()


# ============================================================
# INPUT SECTION
# ============================================================

request = render_inputs()

if request is None:
    st.stop()


# ============================================================
# GENERATE STUDY PACK
# ============================================================

if st.button(
    "🚀 Generate Study Pack",
    type="primary",
    use_container_width=True,
):

    try:
        # ----------------------------------------------------
        # Get Groq API Key
        # ----------------------------------------------------

        api_key = get_groq_api_key()

        # ----------------------------------------------------
        # Progress Display
        # ----------------------------------------------------

        progress_bar = st.progress(0)
        status_text = st.empty()

        def update_progress(stage, progress):
            progress_bar.progress(progress)
            status_text.info(stage)

        # ----------------------------------------------------
        # Run Multi-Stage AI Workflow
        # ----------------------------------------------------

        with st.spinner("Generating your study pack..."):

            result = run_workflow(
                request=request,
                api_key=api_key,
                progress_callback=update_progress,
            )

        # ----------------------------------------------------
        # Save Result
        # ----------------------------------------------------

        st.session_state.study_pack = result

        progress_bar.progress(100)
        status_text.success(
            "Study pack generated successfully!"
        )

        st.success(
            "Your AI study pack is ready."
        )

    except Exception as error:

        st.error(
            "Something went wrong while generating "
            "the study pack."
        )

        st.exception(error)


# ============================================================
# RESULTS
# ============================================================

if st.session_state.study_pack is not None:

    st.divider()

    st.header("📖 Your Study Pack")

    render_results(
        st.session_state.study_pack
    )