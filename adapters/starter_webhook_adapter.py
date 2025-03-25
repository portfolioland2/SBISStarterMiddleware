from infrastructure.http_client import HttpClient
from core.ports.starter_webhook_port import StarterWebhookPort
from infrastructure.config_manager import config

class StarterWebhookAdapter(StarterWebhookPort):
    def __init__(self):
        self.http_client = HttpClient(
            base_url=config.starter_base_url,
            headers={"Authorization": f"Bearer {config.starter_api_key}" if config.starter_api_key else "None"},
        )

    async def set_webhook(self, callback_url: str) -> None:
        endpoint = "/set_webhook"
        payload = {"callbackUrl": callback_url}
        await self.http_client.post(endpoint, data=payload)

    async def handle_order_webhook(self, payload: dict) -> None:
        # тут валидация/обработка данных из стартера
        return payload