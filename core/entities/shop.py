from pydantic import BaseModel
from typing import List, Optional

class Shop(BaseModel):
    id: int
    name: str
    address: str
    latitude: float
    longitude: float
    timezone: str = "UTC+3"
    delivery_types: List[str]
    phones: Optional[List[str]] = None
    phone: Optional[str] = None
    products: Optional[List[str]] = None
    categories: Optional[List[dict]] = None
    work_start: str
    work_end: str
    
    @classmethod
    def from_sbis(cls, sbis_data: dict):
        worktime = sbis_data.get("worktime", {})
        schedule = worktime.get("schedule", {})
        start_time = schedule.get("start", "00:00:00")
        stop_time = schedule.get("stop", "23:59:59")

        return cls(
            id=sbis_data["id"],
            name=sbis_data["name"],
            address=sbis_data["address"],
            latitude=float(sbis_data["latitude"]),
            longitude=float(sbis_data["longitude"]),
            delivery_types=sbis_data.get("product", []),
            work_start=start_time,
            work_end=stop_time,
            phones=sbis_data.get("phones", None),
            phone=sbis_data.get("phone", None),
            products=sbis_data.get("products", None),
            categories=sbis_data.get("categories", None),
        )