from pydantic import PostgresDsn
from sqlmodel import create_engine, Session

from core.config import SETTINGS


DB_URI = PostgresDsn.build(
    scheme="postgresql",
    user=SETTINGS.DB_USER,
    password=SETTINGS.DB_PASSWORD,
    host=f"{SETTINGS.DB_HOSTNAME}:{SETTINGS.DB_PORT}",
    path= f"/{SETTINGS.DB_NAME}"
)

DB_ENGINE = create_engine(DB_URI)

SESSION = Session(DB_ENGINE)