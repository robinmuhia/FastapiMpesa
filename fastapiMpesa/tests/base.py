from fastapi import FastAPI
from fastapiMpesa import MpesaAPI
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MPESA_API_ENVIRONMENT: str
    MPESA_API_KEY: str
    MPESA_API_SECRET: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

mp = MpesaAPI(settings=settings)
