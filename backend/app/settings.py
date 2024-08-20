from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file = '.env', env_file_encoding='utf-8'
    )

    DATABSE_URL: str = 'sqlite+aiosqlite:///database.db'