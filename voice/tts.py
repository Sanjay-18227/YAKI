"""
YAKI Text-to-Speech

Converts YAKI's internal response text into spoken audio
using the selected Windows female voice.
"""

import pyttsx3

from config import PREFERRED_VOICE


class TextToSpeech:
    """Handles YAKI's voice output."""

    def __init__(self):
        self.engine = pyttsx3.init()
        self._select_voice()

    def _select_voice(self):
        """Select the preferred Windows voice."""

        voices = self.engine.getProperty("voices")

        for voice in voices:
            if voice.name == PREFERRED_VOICE:
                self.engine.setProperty("voice", voice.id)
                return

        raise RuntimeError(
            f"Preferred voice not found: {PREFERRED_VOICE}"
        )

    def speak(self, text: str):
        """Speak the supplied text."""

        if not text:
            return

        self.engine.say(text)
        self.engine.runAndWait()