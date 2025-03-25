from pydantic import BaseModel

class Meal(BaseModel):
    id: int
    terminal_id: int
    name: str
    price: float
    quantity: int
    in_menu: bool

    def to_dict(self):
        return self.model_dump()