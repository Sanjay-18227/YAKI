"""
YAKI Speech-to-Text

Converts recorded audio into text using Groq Whisper.
The text is an internal representation only.
"""

import os

from dotenv import load_dotenv
from groq import Groq


# Load variables from the YAKI .env file.
load_dotenv()


class SpeechToText:
    """Handles speech recognition for YAKI."""

    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise RuntimeError(
                "GROQ_API_KEY is not set. "
                "Add it to the YAKI .env file."
            )

        self.client = Groq(api_key=api_key)

    def transcribe(self, audio_file: str) -> str:
        """
        Convert an audio file into text.

        Args:
            audio_file: Path to the recorded audio file.

        Returns:
            Transcribed text.
        """

        with open(audio_file, "rb") as file:
            transcription = self.client.audio.transcriptions.create(
                file=file,
                model="whisper-large-v3-turbo",
            )

        return transcription.text.strip()