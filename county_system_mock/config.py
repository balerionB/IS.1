# ==========================================
# config.py
#
# Loads configuration from environment
# variables.
# ==========================================

import os

from dotenv import load_dotenv

# Load values from .env
load_dotenv()


class Config:
    """
    Central application configuration.
    """

    # Flask secret key
    SECRET_KEY = os.getenv("SECRET_KEY")

    # PostgreSQL connection string
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    # Disable unnecessary tracking
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT configuration
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")