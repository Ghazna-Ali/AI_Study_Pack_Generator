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

import streamlit as st

from models.requests import StudyPackRequest


def render_inputs():
    st.subheader("Study Pack Settings")

    subject = st.text_input(
        "Subject",
        placeholder="e.g. Computer Networks",
    )

    topic = st.text_input(
        "Topic",
        placeholder="e.g. TCP/IP",
    )

    academic_level = st.selectbox(
        "Academic Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced",
            "University",
        ],
    )

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Easy",
            "Medium",
            "Hard",
        ],
    )

    study_time = st.text_input(
        "Study Time",
        placeholder="e.g. 2 hours",
    )

    question_count = st.number_input(
        "Number of Questions",
        min_value=1,
        max_value=30,
        value=10,
        step=1,
    )

    additional_instructions = st.text_area(
        "Additional Instructions",
        placeholder="Optional instructions...",
    )

    if not subject.strip():
        st.warning("Please enter a subject.")
        return None

    if not topic.strip():
        st.warning("Please enter a topic.")
        return None

    if not study_time.strip():
        st.warning("Please enter your available study time.")
        return None

    try:
        return StudyPackRequest(
            subject=subject,
            topic=topic,
            academic_level=academic_level,
            difficulty=difficulty,
            study_time=study_time,
            question_count=int(question_count),
            additional_instructions=additional_instructions,
        )

    except Exception as error:
        st.error(f"Invalid study pack settings: {error}")
        return None

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