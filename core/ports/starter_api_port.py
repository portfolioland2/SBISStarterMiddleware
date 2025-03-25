from abc import ABC, abstractmethod
from typing import List
from core.entities.shop import Shop
from typing import Dict

class StarterApiPort(ABC):
    @abstractmethod
    async def update_or_create_shops(self, shops: List[Shop]) -> None:
        pass
    @abstractmethod
    async def create_category(self, category_data: Dict) -> None:
        pass
    @abstractmethod
    async def create_meal(self, meals_data: Dict) -> None:
        pass