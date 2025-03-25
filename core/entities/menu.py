from pydantic import BaseModel

class PriceList(BaseModel):
    id: int
    name: str

    def to_dict(self):
        return self.model_dump()