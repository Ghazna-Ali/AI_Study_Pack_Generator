from ai.generator import AIGenerator
from ai.prompts import refinement_prompt
from models.requests import StudyPackRequest
from validation.validators import validate_final_pack


def run_refinement_stage(
    generator: AIGenerator,
    request: StudyPackRequest,
    plan: dict,
    content: dict,
    assessment: dict,
    review: dict,
):

    prompt = refinement_prompt(
        request.model_dump(),
        plan,
        content,
        assessment,
        review,
    )

    raw_result = generator.generate_json(
        prompt=prompt,
        stage_name="Refinement",
    )

    validated = validate_final_pack(
        raw_result
    )

    return validated.model_dump()