from typing import Generator

from fastapi import Depends
from sqlmodel import Session

from core.db_config import DB_ENGINE
from persistence.common import ShopPersistence
from persistence.postgress import PostgresShopPersistence


def session_dependecy() -> Generator[Session, None, None]:
    with Session(DB_ENGINE) as session:
        yield session

def shop_persistence_dependency(session: Session = Depends(session_dependecy)) -> ShopPersistence:
    return PostgresShopPersistence(session=session)

