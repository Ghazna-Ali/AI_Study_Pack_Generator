from ai.generator import AIGenerator
from ai.prompts import content_prompt
from models.requests import StudyPackRequest
from validation.validators import validate_content


def run_content_stage(
    generator: AIGenerator,
    request: StudyPackRequest,
    plan: dict,
):

    prompt = content_prompt(
        request.model_dump(),
        plan,
    )

    raw_result = generator.generate_json(
        prompt=prompt,
        stage_name="Content Generation",
    )

    validated = validate_content(
        raw_result
    )

    return validated.model_dump()