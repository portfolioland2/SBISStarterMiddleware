import httpx
from typing import Any, Dict
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class HttpClient:
    def __init__(self, base_url: str, headers: Dict[str, str] = None):
        self.base_url = base_url
        self.headers = headers or {}

    async def get(self, endpoint: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET {url} with params: {params}")
        async with httpx.AsyncClient(base_url=self.base_url, headers=self.headers) as client:
            response = await client.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()

    async def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST {url} with payload: {data}")
        async with httpx.AsyncClient(base_url=self.base_url, headers=self.headers) as client:
            response = await client.post(endpoint, json=data)
            response.raise_for_status()
            return response.json()

    def _log_response(self, response: httpx.Response):
        logger.info(f"Response status: {response.status_code}")
        try:
            logger.debug(f"Response body: {response.json()}")
        except Exception:
            logger.debug("Response body: Unable to parse JSON")