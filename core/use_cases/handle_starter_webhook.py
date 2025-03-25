from typing import Dict
from core.ports.starter_webhook_port import StarterWebhookPort
from adapters.sbis_adapter import SbisAdapter

class HandleStarterWebhook:
    def __init__(self, starter_webhook: StarterWebhookPort, sbis_adapter: SbisAdapter):
        self.starter_webhook = starter_webhook
        self.sbis_adapter = sbis_adapter

    async def execute(self, webhook_payload: Dict) -> None:
        # Обработка вебхука от Стартера
        processed_order = await self.starter_webhook.handle_order_webhook(webhook_payload)
        sbis_order_data = self._transform_to_sbis_format(processed_order)
        await self.sbis_adapter.create_order(sbis_order_data)

    def _transform_to_sbis_format(self, starter_order: Dict) -> Dict:
        delivery_address = starter_order["address"]
        nomenclatures = [
            {
                "externalId": item["mealId"],
                "priceListId": 101,  # ????
                "count": item["quantity"],
                "cost": item["totalPrice"]
            }
            for item in starter_order["orderItems"]
        ]

        return {
            "product": "delivery",
            "pointId": starter_order["shopId"],
            "comment": starter_order.get("comment", ""),
            "customer": {
                "externalId": None,
                "name": starter_order["username"],
                "lastname": "",
                "patronymic": "",
                "email": "",
                "phone": starter_order["userPhone"]
            },
            "datetime": starter_order["submittedDatetime"],
            "nomenclatures": nomenclatures,
            "delivery": {
                "addressFull": delivery_address["street"] + ", " + delivery_address["house"],
                "addressJSON": json.dumps({
                    "City": delivery_address["city"],
                    "Street": delivery_address["street"],
                    "HouseNum": delivery_address["house"]
                }),
                "paymentType": starter_order["paymentType"],
                "persons": 1,
                "isPickup": False
            }
        }