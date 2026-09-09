from ai.generator import AIGenerator
from ai.prompts import review_prompt
from models.requests import StudyPackRequest
from validation.validators import validate_review


def run_review_stage(
    generator: AIGenerator,
    request: StudyPackRequest,
    plan: dict,
    content: dict,
    assessment: dict,
):

    prompt = review_prompt(
        request.model_dump(),
        plan,
        content,
        assessment,
    )

    raw_result = generator.generate_json(
        prompt=prompt,
        stage_name="Review",
    )

    validated = validate_review(
        raw_result
    )

    return validated.model_dump()