"""
YAKI Voice Conversation

Connects microphone recording, speech-to-text,
YAKI's AI brain, and text-to-speech.

The transcription is internal and is not shown
as the user-facing interface.
"""

from voice.recorder import VoiceRecorder
from voice.stt import SpeechToText
from voice.tts import TextToSpeech

from brain import YAKIBrain
from settings.manager import YAKISettings


class VoiceConversation:
    """Handles YAKI's complete voice conversation pipeline."""

    def __init__(self):
        self.settings = YAKISettings()

        self.recorder = VoiceRecorder()
        self.stt = SpeechToText()
        self.tts = TextToSpeech()

        self.brain = YAKIBrain(self.settings)

    def run_once(self):
        """Listen, think, and speak one response."""

        audio_file = self.recorder.record(
            duration=5,
            output_file="voice_command.wav",
        )

        text = self.stt.transcribe(audio_file)

        if not text:
            self.tts.speak("I didn't hear anything.")
            return

        print("Internal transcription:", text)

        response = self.brain.think(text)

        print("YAKI response:", response)

        self.tts.speak(response)