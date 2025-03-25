import httpx
from infrastructure.http_client import HttpClient
from infrastructure.config_manager import config

class SbisAdapter:
    def __init__(self):
        self.auth_client = HttpClient(base_url=config.sbis_auth_url)
        self.api_client = HttpClient(base_url=config.sbis_base_url)
        self.token = None

    async def authenticate(self):
        auth_data = {
            "app_client_id": config.sbis_app_client_id,
            "app_secret": config.sbis_app_secret,
            "secret_key": config.sbis_secret_key
        }
        response = await self.auth_client.post("", data=auth_data)
        self.token = response.get("token")
        self.api_client.headers["X-SBISAccessToken"] = self.token

    async def get_pos(self) -> list:
        if not self.token:
            await self.authenticate()
        endpoint = "/point/list"
        response = await self.api_client.get(endpoint)
        return response.get("salesPoints", [])

    async def get_menu(self, point_id: int, actual_date: str) -> list:
        if not self.token:
            await self.authenticate()
        endpoint = "/nomenclature/price-list"
        params = {
            "pointId": point_id,
            "actualDate": actual_date
        }
        response = await self.api_client.get(endpoint, params=params)
        return response.get("priceLists", [])
    
    async def get_nomenclature_list(self, point_id: int, price_list_id: int) -> list:
        if not self.token:
            await self.authenticate()
        endpoint = "/nomenclature/list"
        params = {
            "pointId": point_id,
            "priceListId": price_list_id
        }
        response = await self.api_client.get(endpoint, params=params)
        return response

    async def create_order(self, order_data: dict) -> None:
        if not self.token:
            await self.authenticate()
        endpoint = "/order/create"
        await self.http_client.post(endpoint, data=order_data)