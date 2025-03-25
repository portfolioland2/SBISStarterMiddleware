from pydantic import BaseModel
from typing import List, Optional

class Product(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    unit: str
    images: List[str]
    attributes: dict
    hierarchical_id: int
    hierarchical_parent: int = None
    index_number: int

    def to_dict(self):
        return self.model_dump()