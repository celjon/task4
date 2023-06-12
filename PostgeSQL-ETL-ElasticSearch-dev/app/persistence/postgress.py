from datetime import datetime
from typing import List
from sqlmodel import Session, select
from core.elastic import ELASTIC_CLIENT
from db.models.shop import ShopModel
from domain.shop.shop import Shop
from persistence.common import ShopPersistence

class PostgresShopPersistence(ShopPersistence):
    def __init__(self, session: Session):
        self.__session = session

    def save(self, name: str, description: str, count_left: int, create_time: str, update_time: str) -> Shop:
        shop_model = ShopModel(name=name, description=description, count_left=count_left,
                               create_time=create_time, update_time=update_time)
        self.__session.add(shop_model)
        self.__session.commit()
        return Shop(
            id=shop_model.id,
            name=shop_model.name,
            description=shop_model.description,
            count_left=shop_model.count_left,
            create_time=shop_model.create_time,
            update_time=shop_model.update_time,
        )

    def delete(self, name: str) -> Shop:
        query = select(ShopModel).where(ShopModel.name == name)
        shop_model = self.__session.exec(query).first()
        self.__session.delete(shop_model)
        self.__session.commit()
        return None

    def get_product_by_id(self, product_id: int) -> Shop:
        query = select(ShopModel).where(ShopModel.id == product_id)
        shop_model = self.__session.exec(query).first()
        return Shop(
            id=shop_model.id,
            name=shop_model.name,
            description=shop_model.description,
            count_left=shop_model.count_left,
            create_time=shop_model.create_time,
            update_time=shop_model.update_time,
        )

    def list_product(self) -> List[Shop]:
        query = select(ShopModel)
        shop_models = self.__session.exec(query).all()
        return [
            Shop(
                id=shop_model.id,
                name=shop_model.name,
                description=shop_model.description,
                count_left=shop_model.count_left,
                create_time=shop_model.create_time,
                update_time=shop_model.update_time,
            )
            for shop_model in shop_models
        ]

    def buy(self, product_id: int, amount: int) -> Shop:
        query = select(ShopModel).where(ShopModel.id == product_id)
        shop_model = self.__session.exec(query).first()
        self.__session.delete(shop_model)
        if shop_model.count_left > 0:
            shop_model.count_left -= amount
            shop_model.update_time = str(datetime.now())
        self.__session.add(shop_model)
        self.__session.commit()
        return Shop(
            id=shop_model.id,
            name=shop_model.name,
            description=shop_model.description,
            count_left=shop_model.count_left,
            create_time=shop_model.create_time,
            update_time=shop_model.update_time,
        )

    def get_product_by_name(self, product_name: str) -> Shop:
        query_body = {
            "query": {
                "bool": {
                    "must": {"match": {"name": product_name}}
                }
            }
        }
        shop_model = ELASTIC_CLIENT.search(index="schemas", body=query_body)
        if shop_model["hits"]["max_score"]:
            return Shop(
                id=shop_model["hits"]["hits"][0]["_source"]["id"],
                name=shop_model["hits"]["hits"][0]["_source"]["name"],
                description=shop_model["hits"]["hits"][0]["_source"]["description"],
                count_left=shop_model["hits"]["hits"][0]["_source"]["count_left"],
                create_time=shop_model["hits"]["hits"][0]["_source"]["create_time"],
                update_time=shop_model["hits"]["hits"][0]["_source"]["create_time"],
            )
        else:
            return Shop(
                id=0,
                name=0,
                description=0,
                count_left=0,
                create_time=0,
                update_time=0,
            )
