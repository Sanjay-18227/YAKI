"""
YAKI Microphone Recorder

Records a short voice command from the default microphone.
"""

import wave

import sounddevice as sd


class VoiceRecorder:
    """Records audio from the system's default microphone."""

    def __init__(self, sample_rate: int = 16000, channels: int = 1):
        self.sample_rate = sample_rate
        self.channels = channels

    def record(self, duration: int = 5, output_file: str = "voice_command.wav") -> str:
        """
        Record audio from the default microphone.

        Args:
            duration: Recording duration in seconds.
            output_file: File where the recording will be saved.

        Returns:
            Path to the recorded WAV file.
        """

        print("YAKI is listening...")

        recording = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype="int16",
        )

        sd.wait()

        with wave.open(output_file, "wb") as wav_file:
            wav_file.setnchannels(self.channels)
            wav_file.setsampwidth(2)
            wav_file.setframerate(self.sample_rate)
            wav_file.writeframes(recording.tobytes())

        print("Recording finished.")

        return output_file