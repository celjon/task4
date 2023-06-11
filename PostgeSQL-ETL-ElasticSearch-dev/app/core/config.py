from pathlib import Path
from pydantic import BaseSettings

class Settings(BaseSettings):

    DB_NAME: str
    DB_USER:str
    DB_PASSWORD: str
    DB_HOSTNAME:str
    DB_PORT:int

    ELASTIC_HOST:str
    ELASTIC_PORT:int
    class Config:
        env_file = ".env"
    
    ROOT_DIR = Path(__file__).parent.parent

SETTINGS = Settings()