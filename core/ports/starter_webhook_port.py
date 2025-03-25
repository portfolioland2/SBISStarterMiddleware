from abc import ABC, abstractmethod

class StarterWebhookPort(ABC):
    @abstractmethod
    async def set_webhook(self, callback_url: str) -> None:
        pass

    @abstractmethod
    async def handle_order_webhook(self, payload: dict) -> None:
        pass