from groq import Groq


class GroqClient:
    def __init__(self, api_key: str):
        self.client = Groq(api_key=api_key)

    def generate_json(
        self,
        model: str,
        prompt: str,
    ) -> str:

        response = self.client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an AI study-pack generation engine. "
                        "Return valid JSON only. "
                        "Do not include markdown fences or explanations."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.3,
            response_format={"type": "json_object"},
        )

        return response.choices[0].message.content