import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_DIR = Path(__file__).resolve().parent
ENV_PATH = ENV_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)

class Settings:
    def __init__(self):
        self.sql_host = "0.0.0.0"
        self.sql_port = int(os.getenv("SQL_PORT", 5432))
        self.sql_base = os.getenv("SQL_BASE")
        self.sql_user = os.getenv("SQL_USER")
        self.sql_pass = os.getenv("SQL_PASS")

    @property
    def db_url(self) -> str:
        return f"postgresql+asyncpg://{self.sql_user}:{self.sql_pass}@{self.sql_host}:{self.sql_port}/{self.sql_base}"

settings = Settings()