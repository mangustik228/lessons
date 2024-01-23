from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv


load_dotenv("./.env")


class Database(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="DB_")
    host: str
    port: int
    username: str
    password: str
    db: str = "scrapy_test"

    @property
    def url(self):
        return f"mysql://{self.username}:{self.password}@{self.host}:{self.port}/{self.db}"


db = Database()
