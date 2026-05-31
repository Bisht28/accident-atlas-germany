from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str

    APP_NAME: str
    APP_VERSION: str

    LICENSE_NAME: str
    LICENSE_URL: str

    OLLAMA_BASE_URL: str

    model_config = SettingsConfigDict(
        env_file="backend/.env",
        extra="ignore"
    )


settings = Settings()