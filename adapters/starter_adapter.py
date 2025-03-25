import httpx
from core.ports.starter_api_port import StarterApiPort
from infrastructure.http_client import HttpClient
from core.entities.shop import Shop
from infrastructure.config_manager import config
from typing import List

class StarterAdapter(StarterApiPort):
    def __init__(self, base_url: str, api_key: str):
        self.http_client = HttpClient(base_url=base_url, headers={"Authorization": f"Bearer {config.starter_api_key}" if config.starter_api_key else "None"})
    """
    По итогам разговора пока шлём на шлюз как есть
    """
    async def update_or_create_shops(self, shops: List[Shop]) -> None:
        endpoint = "/shops"
        data = [shop.to_dict() for shop in shops]
        await self.http_client.post(endpoint, data=data)

    async def create_category(self, categories: list) -> None:
        endpoint = "/categories"
        data = [category.to_dict() for category in categories]
        await self.http_client.post(endpoint, data=data)

    async def create_meal(self, products: list) -> None:
        endpoint = "/meals"
        data = [product.to_dict() for product in products]
        await self.http_client.post(endpoint, data=data)