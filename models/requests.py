from pydantic import BaseModel, Field, field_validator


class StudyPackRequest(BaseModel):
    subject: str = Field(..., min_length=1)
    topic: str = Field(..., min_length=1)
    academic_level: str = Field(..., min_length=1)
    difficulty: str = Field(..., min_length=1)
    study_time: str = Field(..., min_length=1)
    question_count: int = Field(default=10, ge=1, le=30)
    additional_instructions: str = ""

    @field_validator(
        "subject",
        "topic",
        "academic_level",
        "difficulty",
        "study_time",
    )
    @classmethod
    def validate_required_text(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("This field cannot be empty.")

        return value

    @field_validator("additional_instructions")
    @classmethod
    def clean_additional_instructions(cls, value: str) -> str:
        return value.strip()