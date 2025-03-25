from typing import List
from core.ports.sbis_api_port import SbisApiPort
from core.ports.starter_api_port import StarterApiPort
from core.use_cases.transform_pos_data import TransformPosData
from core.use_cases.fetch_menu_from_sbis import FetchMenuFromSbis
from core.use_cases.fetch_nomenclature_from_sbis import FetchNomenclatureFromSbis

class SyncPosToStarter:
    def __init__(self, sbis_api: SbisApiPort, starter_api: StarterApiPort):
        self.sbis_api = sbis_api
        self.starter_api = starter_api
        self.transform_use_case = TransformPosData()
        self.fetch_menu_use_case = FetchMenuFromSbis(sbis_api)
        self.fetch_nomenclature_from_sbis = FetchNomenclatureFromSbis(sbis_api)

    async def execute(self):
        # Получаем POS
        sbis_pos_data = await self.sbis_api.get_pos()
        shops = self.transform_use_case.execute(sbis_pos_data)

        # Получаем меню (прайс-листы)
        pos_ids = [pos["id"] for pos in sbis_pos_data]
        menus = await self.fetch_menu_use_case.execute(pos_ids)

        # Собираем со всех POS-ов список категорий и товаров
        for shop in shops:
            price_list_ids = [menu["id"] for menu in menus.get(shop.id, [])]
            nomenclature = await self.fetch_nomenclature_from_sbis.execute(shop.id, price_list_ids)
            shop.categories = nomenclature["categories"]
            shop.products = nomenclature["products"]

        for shop in shops:
            await self._send_categories_to_starter(shop)
            await self._send_meals_to_starter(shop)

    async def _send_categories_to_starter(self, shop):
        for category in shop.categories:
            category_payload = {
                "name": category["name"],
                "description": "",  
                "images": [], 
                "parentCategoryIds": [category["hierarchical_parent"]] if category["hierarchical_parent"] else [],
                "sortIndex": category["index_number"],
                "isActive": True,
                "posId": str(shop.id)  
            }
            await self.starter_api.create_category(category_payload)

    async def _send_meals_to_starter(self, shop):
        for product in shop.products:
            meal_payload = {
                "name": product["name"],
                "description": product["description"] or "",
                "calories": product["attributes"].get("calorie", 0),
                "fats": product["attributes"].get("fat", 0),
                "carbohydrates": product["attributes"].get("carbohydrate", 0),
                "proteins": product["attributes"].get("protein", 0),
                "weight": 0,  
                "images": product["images"] or [],
                "modifierGroups": [], 
                "categoryIds": [product["hierarchical_parent"]] if product["hierarchical_parent"] else [],
                "deliveryRestrictions": [],
                "isActive": True, 
                "sortIndex": product["index_number"],
                "posId": str(shop.id)
            }
            await self.starter_api.create_meal(meal_payload)