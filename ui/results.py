import json

import streamlit as st


def render_results(
    result: dict,
):

    plan = result.get(
        "study_plan_data",
        {},
    )

    final_pack = result.get(
        "final_pack",
        {},
    )

    st.divider()

    st.header(
        plan.get(
            "title",
            "Study Pack",
        )
    )

    tabs = st.tabs(
        [
            "📖 Overview",
            "📝 Notes",
            "🧠 Flashcards",
            "❓ MCQs",
            "✍️ Questions",
            "🔑 Answers",
            "📅 Study Plan",
            "🔍 Review",
        ]
    )


    # ======================================================
    # OVERVIEW
    # ======================================================

    with tabs[0]:

        st.subheader(
            "Overview"
        )

        st.write(
            final_pack.get(
                "overview",
                "",
            )
        )

        st.subheader(
            "Learning Objectives"
        )

        for item in final_pack.get(
            "learning_objectives",
            [],
        ):

            st.markdown(
                f"- {item}"
            )

        st.subheader(
            "Key Concepts"
        )

        for item in final_pack.get(
            "key_concepts",
            [],
        ):

            st.markdown(
                f"- {item}"
            )


    # ======================================================
    # NOTES
    # ======================================================

    with tabs[1]:

        st.subheader(
            "Detailed Notes"
        )

        for note in final_pack.get(
            "detailed_notes",
            [],
        ):

            if isinstance(
                note,
                dict,
            ):

                title = note.get(
                    "title",
                    "Concept",
                )

                explanation = note.get(
                    "explanation",
                    "",
                )

                st.markdown(
                    f"### {title}"
                )

                st.write(
                    explanation
                )

            else:

                st.write(note)


        st.subheader(
            "Definitions"
        )

        for definition in final_pack.get(
            "definitions",
            [],
        ):

            st.markdown(
                f"- {definition}"
            )


    # ======================================================
    # FLASHCARDS
    # ======================================================

    with tabs[2]:

        cards = final_pack.get(
            "flashcards",
            [],
        )

        for index, card in enumerate(
            cards,
            1,
        ):

            with st.expander(
                f"Flashcard {index}"
            ):

                if isinstance(
                    card,
                    dict,
                ):

                    st.markdown(
                        "**Question:** "
                        + str(
                            card.get(
                                "question",
                                "",
                            )
                        )
                    )

                    st.markdown(
                        "**Answer:** "
                        + str(
                            card.get(
                                "answer",
                                "",
                            )
                        )
                    )

                else:

                    st.write(card)


    # ======================================================
    # MCQS
    # ======================================================

    with tabs[3]:

        for index, question in enumerate(
            final_pack.get(
                "mcqs",
                [],
            ),
            1,
        ):

            st.markdown(
                f"### Question {index}"
            )

            if isinstance(
                question,
                dict,
            ):

                st.write(
                    question.get(
                        "question",
                        "",
                    )
                )

                for option in question.get(
                    "options",
                    [],
                ):

                    st.markdown(
                        f"- {option}"
                    )

                with st.expander(
                    "Show answer"
                ):

                    st.write(
                        question.get(
                            "answer",
                            "",
                        )
                    )

                    st.write(
                        question.get(
                            "explanation",
                            "",
                        )
                    )

            else:

                st.write(question)


    # ======================================================
    # QUESTIONS
    # ======================================================

    with tabs[4]:

        st.subheader(
            "Short Answer"
        )

        for question in final_pack.get(
            "short_answer_questions",
            [],
        ):

            st.markdown(
                f"- {question}"
            )

        st.subheader(
            "Long Answer / Exam"
        )

        for question in final_pack.get(
            "long_answer_questions",
            [],
        ):

            st.markdown(
                f"- {question}"
            )


    # ======================================================
    # ANSWERS
    # ======================================================

    with tabs[5]:

        for answer in final_pack.get(
            "answer_key",
            [],
        ):

            if isinstance(
                answer,
                dict,
            ):

                st.markdown(
                    f"**{answer.get('question', '')}**"
                )

                st.write(
                    answer.get(
                        "answer",
                        "",
                    )
                )

            else:

                st.write(answer)


    # ======================================================
    # STUDY PLAN
    # ======================================================

    with tabs[6]:

        for item in plan.get(
            "time_allocation",
            [],
        ):

            if isinstance(
                item,
                dict,
            ):

                st.markdown(
                    f"### {item.get('activity', 'Study')}"
                )

                st.write(
                    item.get(
                        "time",
                        "",
                    )
                )

                if item.get(
                    "description"
                ):

                    st.write(
                        item["description"]
                    )

            else:

                st.write(item)


    # ======================================================
    # REVIEW
    # ======================================================

    with tabs[7]:

        review = result.get(
            "review",
            {},
        )

        st.metric(
            "Quality Score",
            review.get(
                "quality_score",
                "N/A",
            ),
        )

        if review.get(
            "approved"
        ):

            st.success(
                "Study pack passed AI quality review."
            )

        else:

            st.warning(
                "Study pack reached the refinement limit."
            )

        for issue in review.get(
            "issues",
            [],
        ):

            st.markdown(
                f"- {issue}"
            )


    # ======================================================
    # DOWNLOAD
    # ======================================================

    st.divider()

    download_data = json.dumps(
        final_pack,
        indent=2,
        ensure_ascii=False,
    )

    st.download_button(
        "📥 Download Study Pack",
        data=download_data,
        file_name="study_pack.json",
        mime="application/json",
        use_container_width=True,
    )