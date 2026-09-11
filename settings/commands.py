"""
YAKI Voice Command Settings Controller

Processes commands that change YAKI's runtime
accuracy, humor, and emotion settings.
"""

import re

from settings.manager import YAKISettings


class SettingsCommandProcessor:
    """Understands and executes YAKI settings commands."""

    def __init__(self, settings: YAKISettings):
        self.settings = settings

    def process(self, command: str) -> str | None:
        """
        Process a settings command.

        Returns:
            A response message if the command is a settings command.
            None if the command is not a settings command.
        """

        command = command.strip().lower()

        # ----------------------------------------------------
        # ACCURACY
        # ----------------------------------------------------

        match = re.search(
            r"(?:set|change|make|adjust)?\s*"
            r"accuracy\s*(?:to|at|level)?\s*"
            r"(\d{1,3})\s*(?:percent|%)?",
            command,
        )

        if match:
            value = int(match.group(1))

            try:
                new_value = self.settings.set_accuracy(value)
            except (TypeError, ValueError):
                return "Accuracy must be between 0 and 100 percent."

            return f"Accuracy set to {new_value} percent."

        # ----------------------------------------------------
        # HUMOR
        # ----------------------------------------------------

        match = re.search(
            r"(?:set|change|make|adjust)?\s*"
            r"humou?r\s*(?:to|at|level)?\s*"
            r"(\d{1,3})\s*(?:percent|%)?",
            command,
        )

        if match:
            value = int(match.group(1))

            try:
                new_value = self.settings.set_humor(value)
            except (TypeError, ValueError):
                return "Humor must be between 0 and 100 percent."

            return f"Humor set to {new_value} percent."

        # ----------------------------------------------------
        # EMOTION
        # ----------------------------------------------------

        match = re.search(
            r"(?:set|change|make|adjust)?\s*"
            r"emotion\s*(?:to|at|level)?\s*"
            r"(\d{1,3})\s*(?:percent|%)?",
            command,
        )

        if match:
            value = int(match.group(1))

            try:
                new_value = self.settings.set_emotion(value)
            except (TypeError, ValueError):
                return "Emotion must be between 0 and 100 percent."

            return f"Emotion set to {new_value} percent."

        # ----------------------------------------------------
        # CURRENT SETTINGS
        # ----------------------------------------------------

        if (
            "current settings" in command
            or "show settings" in command
            or "what are my settings" in command
            or "what is your accuracy" in command
            or "what is your humor" in command
            or "what is your emotion" in command
        ):
            current = self.settings.get_all()

            return (
                f"Accuracy is {current['accuracy']} percent. "
                f"Humor is {current['humor']} percent. "
                f"Emotion is {current['emotion']} percent."
            )

        return None