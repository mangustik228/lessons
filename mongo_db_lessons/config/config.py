from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class _Settings(BaseSettings):
    dsn: str

    class Config:
        env_prefix = "MONGO_"
        case_sensitive = False


settings = _Settings()
