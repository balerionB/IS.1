from datetime import timedelta

SESSION_COOKIE_HTTPONLY = True

SESSION_COOKIE_SECURE = True

SESSION_COOKIE_SAMESITE = "Lax"

PERMANENT_SESSION_LIFETIME = timedelta(

    minutes=30

)
import os

class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")