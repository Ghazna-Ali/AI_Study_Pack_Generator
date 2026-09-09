import streamlit as st

from config.settings import get_groq_api_key

from ui.components import (
    render_header,
    render_inputs,
)
from ui.results import (
    render_results,
)
from utils.errors import (
    WorkflowError,
)
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

if "workflow_result" not in st.session_state:
    st.session_state.workflow_result = None


# ============================================================
# HEADER
# ============================================================

render_header()

st.caption(
    f"Version {APP_VERSION} — {APP_DESCRIPTION}"
)

st.divider()


# ============================================================
# INPUT
# ============================================================

request = render_inputs()


# ============================================================
# GENERATE
# ============================================================

generate = st.button(
    "🚀 Generate Study Pack",
    type="primary",
    use_container_width=True,
)


if generate:

    # --------------------------------------------------------
    # Validate input
    # --------------------------------------------------------

    if not request.subject.strip():

        st.warning(
            "Please enter a subject."
        )

        st.stop()


    if not request.topic.strip():

        st.warning(
            "Please enter a topic."
        )

        st.stop()


    if not request.study_time.strip():

        st.warning(
            "Please enter the available study time."
        )

        st.stop()


    # --------------------------------------------------------
    # Get API key
    # --------------------------------------------------------

    try:

        api_key = get_groq_api_key()

    except Exception as error:

        st.error(
            "Gemini API key is not configured."
        )

        st.info(
            "Configure GEMINI_API_KEY in "
            "Streamlit Secrets."
        )

        st.stop()


    # --------------------------------------------------------
    # Workflow status UI
    # --------------------------------------------------------

    st.subheader(
        "AI Workflow"
    )

    stages = [
        "Planning",
        "Content Generation",
        "Assessment",
        "Review",
        "Refinement",
    ]

    status_placeholders = {
        stage: st.empty()
        for stage in stages
    }


    def update_progress(
        stage,
        status,
        message="",
    ):

        placeholder = (
            status_placeholders.get(
                stage
            )
        )

        if placeholder is None:
            return

        if status == "running":

            placeholder.info(
                f"🔄 {stage}"
            )

        elif status == "complete":

            placeholder.success(
                f"✅ {stage}"
            )

        elif status == "skipped":

            placeholder.write(
                f"⏭️ {stage}"
            )


    # --------------------------------------------------------
    # Run workflow
    # --------------------------------------------------------

    try:

        with st.spinner(
            "Running multi-stage AI workflow..."
        ):

            state = run_workflow(
                api_key=api_key,
                request=request,
                progress_callback=(
                    update_progress
                ),
            )


        # ----------------------------------------------------
        # Store result
        # ----------------------------------------------------

        st.session_state.workflow_result = {
            "study_plan_data": (
                state.study_plan
            ),
            "final_pack": (
                state.final_pack
            ),
            "review": (
                state.review
            ),
            "completed_stages": (
                state.completed_stages
            ),
            "iteration": (
                state.refinement_iteration
            ),
        }

        st.success(
            "🎉 Study pack generated successfully!"
        )

    except WorkflowError as error:

        st.error(
            f"❌ Workflow failed: {error}"
        )

    except Exception as error:

        st.error(
            "❌ An unexpected error occurred."
        )

        st.exception(error)


# ============================================================
# RESULTS
# ============================================================

if st.session_state.workflow_result:

    render_results(
        st.session_state.workflow_result
    )