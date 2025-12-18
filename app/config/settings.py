from pydantic_settings import BaseSettings
from fastapi import FastAPI
from typing import Optional
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import os
from dotenv import load_dotenv

app = FastAPI()

# Get ALLOWED_HOSTS from the environment and split it into a list
allowed_hosts = os.getenv("ALLOWED_HOSTS")


class Settings(BaseSettings):
    MONGO_HOST: str
    MONGO_PORT: int
    MONGO_DATABASE: str
    MONGO_USER: Optional[str] = None
    MONGO_PASSWORD: Optional[str] = None
    LIVEKIT_URL:str
    LIVEKIT_API_KEY:str
    LIVEKIT_API_SECRET:str
    PORT=int
    ENVIRONMENT:str="dev"

    class ConfigDict:
        env_file = ".env"
        extra = "ignore"


app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=allowed_hosts,
)

settings = Settings()