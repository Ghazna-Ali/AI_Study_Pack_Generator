from typing import Any

from pydantic import BaseModel, Field


# ============================================================
# PLANNING
# ============================================================

class StudyPlan(BaseModel):

    title: str

    learning_objectives: list[str]

    core_concepts: list[str]

    study_sequence: list[str]

    difficulty_progression: list[str]

    time_allocation: list[Any]

    emphasis: list[str]

    assessment_strategy: list[str]


# ============================================================
# CONTENT
# ============================================================

class StudyContent(BaseModel):

    overview: str

    learning_objectives: list[str]

    key_concepts: list[Any]

    definitions: list[Any]

    detailed_notes: list[Any]

    examples: list[Any]

    common_mistakes: list[str]

    flashcards: list[Any]

    quick_revision: list[Any]


# ============================================================
# ASSESSMENT
# ============================================================

class Assessment(BaseModel):

    mcqs: list[Any]

    short_answer_questions: list[Any]

    long_answer_questions: list[Any]

    answer_key: list[Any]


# ============================================================
# REVIEW
# ============================================================

class ReviewResult(BaseModel):

    approved: bool

    quality_score: float = Field(
        ge=0,
        le=100,
    )

    issues: list[str]

    required_changes: list[str]

    assessment_issues: list[str]


# ============================================================
# FINAL STUDY PACK
# ============================================================

class StudyPack(BaseModel):

    overview: str

    learning_objectives: list[Any]

    key_concepts: list[Any]

    definitions: list[Any]

    detailed_notes: list[Any]

    examples: list[Any]

    common_mistakes: list[str]

    flashcards: list[Any]

    quick_revision: list[Any]

    mcqs: list[Any]

    short_answer_questions: list[Any]

    long_answer_questions: list[Any]

    answer_key: list[Any]

    study_plan: list[Any]