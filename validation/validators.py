from pydantic import ValidationError as PydanticValidationError

from models.schemas import (
    Assessment,
    ReviewResult,
    StudyContent,
    StudyPack,
    StudyPlan,
)
from utils.errors import ValidationError


def validate_study_plan(
    data: dict,
) -> StudyPlan:

    try:

        return StudyPlan.model_validate(
            data
        )

    except PydanticValidationError as error:

        raise ValidationError(
            f"Invalid study plan: {error}"
        ) from error


def validate_content(
    data: dict,
) -> StudyContent:

    try:

        return StudyContent.model_validate(
            data
        )

    except PydanticValidationError as error:

        raise ValidationError(
            f"Invalid study content: {error}"
        ) from error


def validate_assessment(
    data: dict,
) -> Assessment:

    try:

        return Assessment.model_validate(
            data
        )

    except PydanticValidationError as error:

        raise ValidationError(
            f"Invalid assessment: {error}"
        ) from error


def validate_review(
    data: dict,
) -> ReviewResult:

    try:

        return ReviewResult.model_validate(
            data
        )

    except PydanticValidationError as error:

        raise ValidationError(
            f"Invalid review: {error}"
        ) from error


def validate_final_pack(
    data: dict,
) -> StudyPack:

    try:

        return StudyPack.model_validate(
            data
        )

    except PydanticValidationError as error:

        raise ValidationError(
            f"Invalid final study pack: {error}"
        ) from error