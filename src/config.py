from pydantic_settings import BaseSettings

# use pydantic documentation to refer datatypes
class Settings(BaseSettings):
    aws_access_key_id: str
    db_port: int = 5432

    class Config:
        env_file = "../.env"

settings = Settings()
