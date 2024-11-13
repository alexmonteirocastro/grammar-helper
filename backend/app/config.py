from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = (
        "postgresql://postgres:postgres@localhost:5432/polish_cases"  # default value
    )
    SECRET_KEY: str = "my-secret-key"

    class Config:
        env_file = ".env"


settings = Settings()
