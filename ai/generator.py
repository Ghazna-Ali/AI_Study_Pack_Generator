import json
import time

from ai.client import GroqClient

from config.settings import (
    GROQ_MODEL,
    MAX_API_RETRIES,
    RETRY_BASE_DELAY,
)

from utils.errors import AIServiceError


class AIGenerator:
    def __init__(self, api_key: str):
        self.client = GroqClient(api_key)

    def generate_json(
        self,
        prompt: str,
        stage_name: str = "AI Generation",
    ) -> dict:
        """
        Generate a JSON response using Groq.

        Args:
            prompt: Prompt sent to the AI model.
            stage_name: Name of the workflow stage. Used to
                        make errors easier to understand.

        Returns:
            Parsed JSON response as a Python dictionary.

        Raises:
            AIServiceError: If the Groq request fails after
                            all retry attempts.
        """

        last_error = None

        for attempt in range(
            1,
            MAX_API_RETRIES + 1,
        ):
            try:

                raw_response = self.client.generate_json(
                    model=GROQ_MODEL,
                    prompt=prompt,
                )

                return json.loads(
                    raw_response
                )

            except json.JSONDecodeError as error:

                last_error = error

            except Exception as error:

                last_error = error

            if attempt < MAX_API_RETRIES:

                time.sleep(
                    RETRY_BASE_DELAY * attempt
                )

        raise AIServiceError(
            f"{stage_name} failed after "
            f"{MAX_API_RETRIES} attempts: "
            f"{type(last_error).__name__}: "
            f"{last_error}"
        )