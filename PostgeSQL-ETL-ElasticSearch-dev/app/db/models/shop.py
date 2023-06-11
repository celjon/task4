from typing import Optional
from sqlmodel import SQLModel, Field


class ShopModel(SQLModel, table=True):
    __tablename__ = "shop"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, unique=True)
    description: str = Field(max_length=1000, unique=True)
    count_left: int
    create_time: str = Field(max_length=100)
    update_time: str = Field(max_length=100)
