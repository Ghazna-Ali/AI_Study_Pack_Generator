from pydantic import BaseModel, Field


class StudyPackRequest(BaseModel):
    """
    User's study-pack request.
    """

    subject: str = Field(
        min_length=1,
        max_length=200,
    )

    topic: str = Field(
        min_length=1,
        max_length=300,
    )

    academic_level: str

    difficulty: str

    study_time: str

    question_count: int = Field(
        default=10,
        ge=1,
        le=30,
    )

    additional_instructions: str = Field(
        default="",
        max_length=2000,
    )