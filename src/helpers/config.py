from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    FILE_ALLOWED_EXTENSIONS:list
    FILE_MAX_SIZE:int
    FILE_DEFAULT_CHUNCK_SIZE:int

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

def get_settings():
    return Settings()