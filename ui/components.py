import streamlit as st

from models.requests import StudyPackRequest


def render_header():

    st.title(
        "📚 AI Study Pack Generator"
    )

    st.markdown(
        """
Create a personalized study pack through a
multi-stage AI workflow:

**Planning → Content → Assessment → Review → Refinement**
"""
    )


def render_inputs():

    left, right = st.columns(2)

    with left:

        subject = st.text_input(
            "Subject",
            placeholder="e.g. Database Systems",
        )

        topic = st.text_input(
            "Topic",
            placeholder="e.g. SQL Joins",
        )

        academic_level = st.selectbox(
            "Academic Level",
            [
                "School",
                "College",
                "University",
                "Professional",
            ],
        )

        difficulty = st.selectbox(
            "Difficulty",
            [
                "Beginner",
                "Intermediate",
                "Advanced",
                "Exam Preparation",
            ],
        )

    with right:

        study_time = st.text_input(
            "Available Study Time",
            placeholder="e.g. 2 hours",
        )

        question_count = st.number_input(
            "Number of MCQs",
            min_value=1,
            max_value=30,
            value=10,
            step=1,
        )

        additional_instructions = (
            st.text_area(
                "Additional Instructions",
                placeholder=(
                    "Example: Focus on practical "
                    "examples and interview questions."
                ),
                height=160,
            )
        )

    return StudyPackRequest(
        subject=subject,
        topic=topic,
        academic_level=academic_level,
        difficulty=difficulty,
        study_time=study_time,
        question_count=question_count,
        additional_instructions=(
            additional_instructions
        ),
    )