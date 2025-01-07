import os

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openai_api_key: str

    class Config:
        env_file = ".env"

    model_config = SettingsConfigDict()
settings = Settings()

print("env file :"+ settings.openai_api_key)
