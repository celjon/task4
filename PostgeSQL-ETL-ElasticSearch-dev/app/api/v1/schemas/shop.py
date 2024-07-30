from pydantic import BaseModel


class ShopCreateRequestSchema(BaseModel):
    name: str
    description: str
    count_left: int


class ShopCreateResponseSchema(BaseModel):
    id: int


class ShopDeleteRequestSchema(BaseModel):
    name: str


class ShopDeleteResponseSchema(BaseModel):
    result: None


class ShopPurchaseRequestSchema(BaseModel):
    id: int
    amount: int


class ShopPurchaseResponseSchema(BaseModel):
    id: int
    name: str
    description: str
    count_left: int
    create_time: str
    update_time: str


class ShopGetByNameRequestSchema(BaseModel):
    name: str


class ShopGetByNameResponseSchema(BaseModel):
    id: int
    name: str
    description: str
    count_left: int
    create_time: str
    update_time: str


class ShopSchema(BaseModel):
    id: int
    name: str
    description: str
    count_left: int
    create_time: str
    update_time: str
