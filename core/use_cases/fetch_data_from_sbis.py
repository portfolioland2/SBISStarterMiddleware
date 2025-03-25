from typing import List
from core.ports.sbis_api_port import SbisApiPort
from core.entities.shop import Shop
from core.entities.terminal import Terminal
from core.entities.meal import Meal

class FetchDataFromSbis:
    def __init__(self, sbis_api: SbisApiPort):
        self.sbis_api = sbis_api

    async def execute(self) -> dict:
        shops = await self.sbis_api.get_shops()
        terminals = await self.sbis_api.get_terminals()
        meals = await self.sbis_api.get_meals()

        return {
            "shops": [shop.to_dict() for shop in shops],
            "terminals": [terminal.to_dict() for terminal in terminals],
            "meals": [meal.to_dict() for meal in meals],
        }