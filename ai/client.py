from google import genai


class GeminiClient:
    """
    Thin wrapper around the Gemini API client.
    """

    def __init__(
        self,
        api_key: str,
    ):
        if not api_key:
            raise ValueError(
                "Gemini API key is required."
            )

        self.client = genai.Client(
            api_key=api_key
        )

    def generate_json(
        self,
        model: str,
        prompt: str,
    ) -> str:

        response = self.client.models.generate_content(
            model=model,
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "temperature": 0.3,
            },
        )

        if not response.text:
            raise ValueError(
                "Gemini returned an empty response."
            )

        return response.text