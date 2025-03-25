from typing import List
from core.ports.sbis_api_port import SbisApiPort
from core.entities.menu import PriceList
from datetime import datetime

class FetchMenuFromSbis:
    def __init__(self, sbis_api: SbisApiPort):
        self.sbis_api = sbis_api

    async def execute(self, pos_ids: List[int]) -> dict:
        menus = {}
        actual_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for pos_id in pos_ids:
            raw_menu = await self.sbis_api.get_menu(pos_id, actual_date)
            menus[pos_id] = [PriceList(**item).to_dict() for item in raw_menu]

        return menus