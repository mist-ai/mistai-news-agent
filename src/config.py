from pydantic_settings import BaseSettings
from pathlib import Path

# use pydantic documentation to refer datatypes
class Settings(BaseSettings):
    aws_access_key_id: str
    db_port: int = 5432

    class Config:
        env_file = str(Path(__file__).parent.parent / ".env")

settings = Settings()