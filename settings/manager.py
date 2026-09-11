"""
YAKI Runtime Settings Manager

Handles settings that can be changed while YAKI is running.
"""

from config import (
    DEFAULT_ACCURACY,
    DEFAULT_HUMOR,
    DEFAULT_EMOTION,
)


class YAKISettings:
    """Stores and manages YAKI's runtime settings."""

    def __init__(self):
        self.accuracy = DEFAULT_ACCURACY
        self.humor = DEFAULT_HUMOR
        self.emotion = DEFAULT_EMOTION

    def set_accuracy(self, value: int) -> int:
        """Set YAKI's accuracy level."""
        self.accuracy = self._validate_percentage(value)
        return self.accuracy

    def set_humor(self, value: int) -> int:
        """Set YAKI's humor level."""
        self.humor = self._validate_percentage(value)
        return self.humor

    def set_emotion(self, value: int) -> int:
        """Set YAKI's emotion level."""
        self.emotion = self._validate_percentage(value)
        return self.emotion

    def get_all(self) -> dict:
        """Return all current runtime settings."""
        return {
            "accuracy": self.accuracy,
            "humor": self.humor,
            "emotion": self.emotion,
        }

    @staticmethod
    def _validate_percentage(value: int) -> int:
        """Keep percentage values between 0 and 100."""

        if not isinstance(value, int):
            raise TypeError("Setting value must be an integer.")

        if not 0 <= value <= 100:
            raise ValueError("Setting value must be between 0 and 100.")

        return value