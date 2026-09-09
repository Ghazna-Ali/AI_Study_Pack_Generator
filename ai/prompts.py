import json


# ============================================================
# COMMON INSTRUCTION
# ============================================================

JSON_ONLY = """
Return ONLY valid JSON.

Do not use Markdown fences.
Do not include explanations outside the JSON.
Do not include introductory text.
"""


# ============================================================
# PLANNING PROMPT
# ============================================================

def planning_prompt(
    user_request: dict,
) -> str:

    return f"""
You are an expert instructional designer.

Create a personalized learning plan.

USER REQUEST
============
{json.dumps(user_request, indent=2)}

The plan must consider:

- academic level
- difficulty
- available study time
- learning goals
- requested number of questions
- additional instructions

Create:

1. A study pack title
2. Learning objectives
3. Core concepts
4. Concept sequence
5. Difficulty progression
6. Time allocation
7. Areas requiring emphasis
8. Assessment strategy

Return this JSON structure:

{{
    "title": "...",
    "learning_objectives": [],
    "core_concepts": [],
    "study_sequence": [],
    "difficulty_progression": [],
    "time_allocation": [],
    "emphasis": [],
    "assessment_strategy": []
}}

{JSON_ONLY}
"""


# ============================================================
# CONTENT PROMPT
# ============================================================

def content_prompt(
    user_request: dict,
    plan: dict,
) -> str:

    return f"""
You are an expert educational content creator.

Create personalized study material.

USER REQUEST
============
{json.dumps(user_request, indent=2)}

LEARNING PLAN
=============
{json.dumps(plan, indent=2)}

Generate:

- topic overview
- learning objectives
- key concepts
- definitions
- detailed study notes
- practical examples
- common mistakes
- flashcards
- quick revision material

The material must:

- match the learner's level
- match the selected difficulty
- follow the learning sequence
- fit the available study time
- prioritize understanding
- avoid unnecessary repetition

Do NOT create assessment questions.

Return:

{{
    "overview": "...",
    "learning_objectives": [],
    "key_concepts": [],
    "definitions": [],
    "detailed_notes": [],
    "examples": [],
    "common_mistakes": [],
    "flashcards": [],
    "quick_revision": []
}}

{JSON_ONLY}
"""


# ============================================================
# ASSESSMENT PROMPT
# ============================================================

def assessment_prompt(
    user_request: dict,
    plan: dict,
    content: dict,
) -> str:

    return f"""
You are an expert educational assessment designer.

Create an assessment from the approved study material.

USER REQUEST
============
{json.dumps(user_request, indent=2)}

LEARNING PLAN
=============
{json.dumps(plan, indent=2)}

STUDY CONTENT
=============
{json.dumps(content, indent=2)}

Create exactly the requested number of MCQs.

Also create:

- short-answer questions
- long-answer/exam questions
- answer key
- explanations

Rules:

- Questions must test material actually covered.
- Do not introduce unsupported facts.
- Difficulty must match the learner.
- Avoid duplicate questions.
- MCQ options must be unambiguous.
- Correct answers must be valid.
- Questions should test understanding, not only memorization.

Return:

{{
    "mcqs": [],
    "short_answer_questions": [],
    "long_answer_questions": [],
    "answer_key": []
}}

{JSON_ONLY}
"""


# ============================================================
# REVIEW PROMPT
# ============================================================

def review_prompt(
    user_request: dict,
    plan: dict,
    content: dict,
    assessment: dict,
) -> str:

    return f"""
You are a strict educational quality reviewer.

Review this generated study pack.

USER REQUEST
============
{json.dumps(user_request, indent=2)}

PLAN
====
{json.dumps(plan, indent=2)}

CONTENT
=======
{json.dumps(content, indent=2)}

ASSESSMENT
==========
{json.dumps(assessment, indent=2)}

Check for:

1. Factual inconsistencies
2. Missing important concepts
3. Incorrect explanations
4. Inappropriate difficulty
5. Poor progression
6. Repetition
7. Weak flashcards
8. Duplicate questions
9. Incorrect answers
10. Ambiguous MCQs
11. Questions unrelated to the content
12. Mismatch with academic level
13. Mismatch with study time

Return:

{{
    "approved": true,
    "quality_score": 0,
    "issues": [],
    "required_changes": [],
    "assessment_issues": []
}}

Set approved to false if meaningful corrections are required.

{JSON_ONLY}
"""


# ============================================================
# REFINEMENT PROMPT
# ============================================================

def refinement_prompt(
    user_request: dict,
    plan: dict,
    content: dict,
    assessment: dict,
    review: dict,
) -> str:

    return f"""
You are an expert educational editor.

Improve the study pack according to the review findings.

USER REQUEST
============
{json.dumps(user_request, indent=2)}

PLAN
====
{json.dumps(plan, indent=2)}

CURRENT CONTENT
===============
{json.dumps(content, indent=2)}

CURRENT ASSESSMENT
==================
{json.dumps(assessment, indent=2)}

REVIEW FINDINGS
===============
{json.dumps(review, indent=2)}

Apply the required corrections.

Important:

- Preserve good material.
- Fix identified problems.
- Do not introduce unrelated changes.
- Keep the learner's level and difficulty.
- Maintain consistency between content and assessment.

Return the COMPLETE corrected study pack:

{{
    "overview": "...",
    "learning_objectives": [],
    "key_concepts": [],
    "definitions": [],
    "detailed_notes": [],
    "examples": [],
    "common_mistakes": [],
    "flashcards": [],
    "quick_revision": [],
    "mcqs": [],
    "short_answer_questions": [],
    "long_answer_questions": [],
    "answer_key": [],
    "study_plan": []
}}

{JSON_ONLY}
"""