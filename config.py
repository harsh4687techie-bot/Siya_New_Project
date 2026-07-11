import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    if os.environ.get("VERCEL"):
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:////tmp/app.db")
        UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER", "/tmp/uploads")
    else:
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", f"sqlite:///{BASE_DIR / 'app.db'}")
        UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER", str(BASE_DIR / "app" / "uploads"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    MAIL_SERVER = os.environ.get("MAIL_SERVER", "localhost")
    MAIL_PORT = int(os.environ.get("MAIL_PORT", "1025"))
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS", "False").lower() in {"1", "true", "yes"}
    MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL", "False").lower() in {"1", "true", "yes"}
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER", "noreply@vitalledger.local")
    WTF_CSRF_ENABLED = True


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
