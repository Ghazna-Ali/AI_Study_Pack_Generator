from ai.generator import AIGenerator
from ai.prompts import planning_prompt
from models.requests import StudyPackRequest
from validation.validators import validate_study_plan


def run_planning_stage(
    generator: AIGenerator,
    request: StudyPackRequest,
):

    prompt = planning_prompt(
        request.model_dump()
    )

    raw_result = generator.generate_json(
        prompt=prompt,
        stage_name="Planning",
    )

    validated = validate_study_plan(
        raw_result
    )

    return validated.model_dump()