from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class WorkflowState:

    user_request: Any

    study_plan: Optional[dict] = None

    study_content: Optional[dict] = None

    assessment: Optional[dict] = None

    review: Optional[dict] = None

    final_pack: Optional[dict] = None

    refinement_iteration: int = 0

    errors: list[str] = field(
        default_factory=list
    )

    completed_stages: list[str] = field(
        default_factory=list
    )

    def mark_complete(
        self,
        stage: str,
    ):

        if stage not in self.completed_stages:

            self.completed_stages.append(
                stage
            )

    def add_error(
        self,
        error: str,
    ):

        self.errors.append(
            error
        )