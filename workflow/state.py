from dataclasses import dataclass, field
from typing import Any


@dataclass
class WorkflowState:
    """
    Stores all data generated throughout the study-pack workflow.
    """

    user_request: Any

    study_plan: dict | None = None

    study_content: dict | None = None

    assessment: dict | None = None

    review: dict | None = None

    final_pack: dict | None = None

    refinement_iteration: int = 0

    errors: list[dict[str, str]] = field(
        default_factory=list
    )

    completed_stages: list[str] = field(
        default_factory=list
    )

    def mark_complete(
        self,
        stage: str,
    ) -> None:
        """
        Mark a workflow stage as completed.
        """

        if stage not in self.completed_stages:
            self.completed_stages.append(stage)

    def add_error(
        self,
        stage: str,
        error: str,
    ) -> None:
        """
        Store an error together with the workflow stage
        where it occurred.
        """

        self.errors.append(
            {
                "stage": stage,
                "error": str(error),
            }
        )