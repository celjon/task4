from typing import List, Union

from fastapi import APIRouter, Depends

from api.v1.schemas.shop import (
    ShopSchema,
    ShopPurchaseRequestSchema,
    ShopPurchaseResponseSchema,
    ShopGetByNameRequestSchema,
    ShopGetByNameResponseSchema,
)
from core.dependencies.persistance import shop_persistence_dependency

from persistence.common import ShopPersistence

router = APIRouter()


@router.get("/", summary="List of products", description="Get list of all products", response_model=List[ShopSchema])
async def list_product(shop_persistence: ShopPersistence = Depends(shop_persistence_dependency)) -> List[ShopSchema]:
    products = shop_persistence.list_product()
    return [
        ShopSchema(
            id=product.id,
            name=product.name,
            description=product.description,
            count_left=product.count_left,
            create_time=product.create_time,
            update_time=product.update_time,
        )
        for product in products
    ]


@router.get("/{product_id}", summary="Get product", description="Get product by id", response_model=Union[ShopSchema, None])
async def get_product_by_id(
    product_id: int, shop_persistence: ShopPersistence = Depends(shop_persistence_dependency)
) -> Union[ShopSchema, None]:
    product = shop_persistence.get_product_by_id(product_id)
    if product:
        return ShopSchema(
            id=product.id,
            name=product.name,
            description=product.description,
            count_left=product.count_left,
            create_time=product.create_time,
            update_time=product.update_time,
        )
    else:
        return None


@router.post("/buy", summary="Buy product", description="Buy product in needed amount", response_model=ShopPurchaseResponseSchema)
async def buy_product(
    buy_request: ShopPurchaseRequestSchema, shop_persistence: ShopPersistence = Depends(shop_persistence_dependency)
) -> ShopPurchaseResponseSchema:
    product = shop_persistence.buy(product_id=buy_request.id, amount=buy_request.amount)
    return ShopPurchaseResponseSchema(
        id=product.id,
        name=product.name,
        description=product.description,
        count_left=product.count_left,
        create_time=product.create_time,
        update_time=product.update_time,
    )


@router.post("/get_by_name", summary="Get product", description="Get product by name", response_model=ShopGetByNameResponseSchema)
async def get_product_by_name(
    search_request: ShopGetByNameRequestSchema, shop_persistence: ShopPersistence = Depends(shop_persistence_dependency)
) -> ShopGetByNameResponseSchema:
    product = shop_persistence.get_product_by_name(search_request.product_name)
    if product:
        return ShopGetByNameResponseSchema(
            id=product.id,
            name=product.name,
            description=product.description,
            count_left=product.count_left,
            create_time=product.create_time,
            update_time=product.update_time,
        )
    else:
        return ShopGetByNameResponseSchema(
            id=None,
            name=None,
            description=None,
            count_left=None,
            create_time=None,
            update_time=None,
        )
