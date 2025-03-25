from pydantic import BaseModel

class Terminal(BaseModel):
    id: int
    shop_id: int
    name: str
    pos_id: str

    def to_dict(self):
        return self.model_dump()