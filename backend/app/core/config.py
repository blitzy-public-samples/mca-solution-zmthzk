from os import getenv
from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "MCA Application Processing System"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = getenv("SECRET_KEY", "your-secret-key")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = getenv("DATABASE_URL", "sqlite:///./test.db")
    GOOGLE_CLOUD_PROJECT: str = getenv("GOOGLE_CLOUD_PROJECT")
    GOOGLE_APPLICATION_CREDENTIALS: str = getenv("GOOGLE_APPLICATION_CREDENTIALS")
    STORAGE_BUCKET: str = getenv("STORAGE_BUCKET")
    SENDGRID_API_KEY: str = getenv("SENDGRID_API_KEY")
    EMAIL_FROM: str = getenv("EMAIL_FROM")
    EMAIL_TO: str = getenv("EMAIL_TO")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()