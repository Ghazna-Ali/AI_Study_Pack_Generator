from ai.generator import AIGenerator
from config.settings import (
    MAX_REFINEMENT_ITERATIONS,
)
from models.requests import StudyPackRequest
from utils.errors import WorkflowError
from workflow.assessment import (
    run_assessment_stage,
)
from workflow.content import (
    run_content_stage,
)
from workflow.planning import (
    run_planning_stage,
)
from workflow.refinement import (
    run_refinement_stage,
)
from workflow.review import (
    run_review_stage,
)
from workflow.state import WorkflowState


def run_workflow(
    api_key: str,
    request: StudyPackRequest,
    progress_callback=None,
) -> WorkflowState:

    state = WorkflowState(
        user_request=request
    )

    generator = AIGenerator(
        api_key
    )

    def progress(
        stage: str,
        status: str,
        message: str = "",
    ):

        if progress_callback:
            progress_callback(
                stage,
                status,
                message,
            )

    try:

        # ==================================================
        # STAGE 1 — PLANNING
        # ==================================================

        progress(
            "Planning",
            "running",
        )

        state.study_plan = (
            run_planning_stage(
                generator,
                request,
            )
        )

        state.mark_complete(
            "Planning"
        )

        progress(
            "Planning",
            "complete",
        )


        # ==================================================
        # STAGE 2 — CONTENT GENERATION
        # ==================================================

        progress(
            "Content Generation",
            "running",
        )

        state.study_content = (
            run_content_stage(
                generator,
                request,
                state.study_plan,
            )
        )

        state.mark_complete(
            "Content Generation"
        )

        progress(
            "Content Generation",
            "complete",
        )


        # ==================================================
        # STAGE 3 — ASSESSMENT
        # ==================================================

        progress(
            "Assessment",
            "running",
        )

        state.assessment = (
            run_assessment_stage(
                generator,
                request,
                state.study_plan,
                state.study_content,
            )
        )

        state.mark_complete(
            "Assessment"
        )

        progress(
            "Assessment",
            "complete",
        )


        # ==================================================
        # STAGES 4 + 5
        # REVIEW / REFINEMENT LOOP
        # ==================================================

        for iteration in range(
            MAX_REFINEMENT_ITERATIONS + 1
        ):

            state.refinement_iteration = (
                iteration
            )

            # ----------------------------------------------
            # REVIEW
            # ----------------------------------------------

            progress(
                "Review",
                "running",
            )

            state.review = (
                run_review_stage(
                    generator,
                    request,
                    state.study_plan,
                    state.study_content,
                    state.assessment,
                )
            )

            state.mark_complete(
                "Review"
            )

            progress(
                "Review",
                "complete",
            )


            # ----------------------------------------------
            # APPROVED
            # ----------------------------------------------

            if state.review["approved"]:

                state.final_pack = {
                    **state.study_content,
                    **state.assessment,
                    "study_plan": (
                        state.study_plan[
                            "time_allocation"
                        ]
                    ),
                }

                return state


            # ----------------------------------------------
            # REFINEMENT LIMIT
            # ----------------------------------------------

            if (
                iteration
                >= MAX_REFINEMENT_ITERATIONS
            ):

                raise WorkflowError(
                    "The study pack did not pass "
                    "quality review after the maximum "
                    "number of refinement attempts."
                )


            # ----------------------------------------------
            # REFINEMENT
            # ----------------------------------------------

            progress(
                "Refinement",
                "running",
            )

            refined = (
                run_refinement_stage(
                    generator,
                    request,
                    state.study_plan,
                    state.study_content,
                    state.assessment,
                    state.review,
                )
            )

            state.study_content = {
                key: refined[key]
                for key in [
                    "overview",
                    "learning_objectives",
                    "key_concepts",
                    "definitions",
                    "detailed_notes",
                    "examples",
                    "common_mistakes",
                    "flashcards",
                    "quick_revision",
                ]
            }

            state.assessment = {
                key: refined[key]
                for key in [
                    "mcqs",
                    "short_answer_questions",
                    "long_answer_questions",
                    "answer_key",
                ]
            }

            progress(
                "Refinement",
                "complete",
            )


        raise WorkflowError(
            "Workflow ended without a final result."
        )

    except Exception as error:
        import traceback

        traceback.print_exc()

        raise WorkflowError(
            f"Study-pack workflow failed: "
            f"{type(error).__name__}: {error}"
        ) from error