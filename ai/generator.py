import json
import time

from ai.client import GeminiClient
from config.settings import (
    GEMINI_MODEL,
    MAX_API_RETRIES,
    RETRY_BASE_DELAY,
)
from utils.errors import AIServiceError


class AIGenerator:
    """
    Handles reliable execution of Gemini requests.
    """

    def __init__(
        self,
        api_key: str,
    ):
        self.client = GeminiClient(
            api_key
        )

    def generate_json(
        self,
        prompt: str,
        stage_name: str,
    ) -> dict:

        last_error = None

        for attempt in range(
            1,
            MAX_API_RETRIES + 1,
        ):

            try:

                raw_response = (
                    self.client.generate_json(
                        model=GEMINI_MODEL,
                        prompt=prompt,
                    )
                )

                result = json.loads(
                    raw_response
                )

                if not isinstance(
                    result,
                    dict,
                ):
                    raise ValueError(
                        "Expected a JSON object."
                    )

                return result

            except Exception as error:

                last_error = error

                if attempt < MAX_API_RETRIES:

                    time.sleep(
                        RETRY_BASE_DELAY
                        * attempt
                    )

        raise AIServiceError(
            f"{stage_name} failed after "
            f"{MAX_API_RETRIES} attempts. "
            f"Last error: {last_error}"
        )