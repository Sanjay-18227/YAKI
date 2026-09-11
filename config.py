"""
YAKI Configuration

This file contains the default configuration for YAKI.
Runtime settings such as accuracy, humor, and emotion will
later be controlled by voice commands.
"""

import os
from dotenv import load_dotenv


# ============================================================
# ENVIRONMENT
# ============================================================

load_dotenv()


# ============================================================
# YAKI IDENTITY
# ============================================================

YAKI_NAME = "YAKI"
USER_NAME = "Sanjay"


# ============================================================
# RUNTIME PERSONALITY SETTINGS
# ============================================================

# These are the starting values when YAKI launches.
# They can later be changed by voice commands.

DEFAULT_ACCURACY = 90
DEFAULT_HUMOR = 55
DEFAULT_EMOTION = 70


# ============================================================
# VOICE SETTINGS
# ============================================================

VOICE_ENABLED = True

# Windows female voice that we will use when available.
PREFERRED_VOICE = "Microsoft Zira Desktop - English (United States)"


# ============================================================
# LANGUAGE
# ============================================================

DEFAULT_LANGUAGE = "en"


# ============================================================
# LOCAL SECURITY
# ============================================================

# YAKI's computer-control service should only operate
# locally on this laptop.

LOCAL_HOST = "127.0.0.1"


# ============================================================
# AI PROVIDER
# ============================================================

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")


# ============================================================
# APPLICATION
# ============================================================

APP_NAME = "YAKI"
APP_VERSION = "0.1.0"

DEBUG = True