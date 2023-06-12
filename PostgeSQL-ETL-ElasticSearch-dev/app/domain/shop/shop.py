from pydantic import BaseModel


class Shop(BaseModel):
    id: int
    name: str
    description: str
    count_left:int
    create_time:str
    update_time:str