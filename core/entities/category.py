from pydantic import BaseModel

class Category(BaseModel):
    id: int
    name: str
    hierarchical_id: int
    hierarchical_parent: int = None
    index_number: int

    def to_dict(self):
        return self.model_dump()