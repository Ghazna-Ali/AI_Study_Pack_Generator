from ai.generator import AIGenerator
from ai.prompts import assessment_prompt
from models.requests import StudyPackRequest
from validation.validators import validate_assessment


def run_assessment_stage(
    generator: AIGenerator,
    request: StudyPackRequest,
    plan: dict,
    content: dict,
):

    prompt = assessment_prompt(
        request.model_dump(),
        plan,
        content,
    )

    raw_result = generator.generate_json(
        prompt=prompt,
        stage_name="Assessment",
    )

    validated = validate_assessment(
        raw_result
    )

    return validated.model_dump()