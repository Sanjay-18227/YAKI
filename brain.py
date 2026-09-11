"""
YAKI AI Brain

Sends the user's internally transcribed speech to
the Groq language model and returns YAKI's response.
"""

from groq import Groq

from config import GROQ_API_KEY, YAKI_NAME, USER_NAME
from settings.manager import YAKISettings


class YAKIBrain:
    """Handles YAKI's AI reasoning."""

    def __init__(self, settings: YAKISettings):
        if not GROQ_API_KEY:
            raise RuntimeError(
                "GROQ_API_KEY is not configured."
            )

        self.client = Groq(api_key=GROQ_API_KEY)
        self.settings = settings

    def think(self, user_text: str) -> str:
        """Generate a response to the user's speech."""

        current = self.settings.get_all()

        system_prompt = f"""
You are {YAKI_NAME}, a personal desktop AI assistant.

The authenticated user's name is {USER_NAME}.

Current runtime settings:
- Accuracy: {current['accuracy']} percent
- Humor: {current['humor']} percent
- Emotion: {current['emotion']} percent

Follow these settings when generating your response.

Important:
- Be helpful and natural.
- Keep responses reasonably concise because the response
  will be spoken aloud.
- Do not mention internal transcription.
- Do not expose API keys, secrets, or private system information.
- Accuracy controls how carefully you reason and verify information.
- Humor controls how playful your response is.
- Emotion controls the emotional warmth of your response.
"""

        response = self.client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_text,
                },
            ],
            temperature=0.7,
        )

        return response.choices[0].message.content.strip()