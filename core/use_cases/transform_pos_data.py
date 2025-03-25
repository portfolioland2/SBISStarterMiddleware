from typing import List
from core.entities.shop import Shop

class TransformPosData:
    def execute(self, sbis_pos_data: List[dict]) -> List[Shop]:
        return [Shop.from_sbis(pos) for pos in sbis_pos_data]