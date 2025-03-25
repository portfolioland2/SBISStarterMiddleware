from abc import ABC, abstractmethod
from typing import List, Dict

class SbisApiPort(ABC):
    # Получить торговую точку
    @abstractmethod
    async def get_pos(self) -> List[Dict]:
        pass
    # Получить меню торговой точки
    @abstractmethod
    async def get_menu(self, point_id: int, actual_date: str) -> List[Dict]:
        pass
    # Получить список блюд
    @abstractmethod
    async def get_nomenclature_list(self, point_id: int, price_list_id: int) -> List[Dict]:
        pass
    @abstractmethod
    async def create_order(self, order_data: Dict) -> None:
        pass