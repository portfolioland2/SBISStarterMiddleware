from typing import List, Dict
from core.entities.category import Category
from core.entities.product import Product
from core.ports.sbis_api_port import SbisApiPort

class FetchNomenclatureFromSbis:
    def __init__(self, sbis_api: SbisApiPort):
        self.sbis_api = sbis_api

    async def execute(self, pos_id: int, price_list_ids: List[int]) -> Dict[str, List[Dict]]:
        categories = []
        products = []

        for price_list_id in price_list_ids:
            raw_data = await self.sbis_api.get_nomenclature_list(pos_id, price_list_id)

            for item in raw_data:
                if not isinstance(item, dict):
                    continue

                if item.get("isParent", False):
                    categories.append(Category(
                        id=item["indexNumber"],
                        name=item["name"],
                        hierarchical_id=item["hierarchicalId"],
                        hierarchical_parent=item.get("hierarchicalParent"),
                        index_number=item["indexNumber"]
                    ).to_dict())
                elif item.get("id") is not None:
                    products.append(Product(
                        id=item["id"],
                        name=item["name"],
                        description=item.get("description_simple"),
                        price=item["cost"] / 100,  
                        unit=item["unit"],
                        images=item.get("images", []),
                        attributes=item.get("attributes", {}),
                        hierarchical_id=item["hierarchicalId"],
                        hierarchical_parent=item.get("hierarchicalParent"),
                        index_number=item["indexNumber"]
                    ).to_dict())

        return {"categories": categories, "products": products}