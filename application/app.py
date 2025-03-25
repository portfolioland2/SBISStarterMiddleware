from fastapi import FastAPI, Request

from adapters.sbis_adapter import SbisAdapter
from adapters.starter_webhook_adapter import StarterWebhookAdapter
from adapters.starter_adapter import StarterAdapter

from core.use_cases.handle_starter_webhook import HandleStarterWebhook
from core.use_cases.sync_pos_to_starter import SyncPosToStarter

from infrastructure.config_manager import config
from infrastructure.cron_service import CronService
from infrastructure.logger import logger
#from requests import Request
app = FastAPI()


sbis_adapter = SbisAdapter()
starter_adapter = StarterAdapter(
    base_url=config.starter_base_url,
    api_key=config.starter_api_key
)
starter_webhook_adapter = StarterWebhookAdapter()


sync_pos_use_case = SyncPosToStarter(sbis_adapter, starter_adapter)
handle_webhook_use_case = HandleStarterWebhook(starter_webhook_adapter, sbis_adapter)


@app.on_event("startup")
async def startup_event():
    logger.info("Starting application...")
    
    #callback_url = f"{config.base_url}/webhook/orders"
  #  await starter_webhook_adapter.set_webhook(callback_url)
   # logger.info("Webhook set successfully.")

 #   cron_service = CronService()
  #  await cron_service.start()
  #  logger.info("Cron service started.")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down application...")
    cron_service = CronService()
    await cron_service.stop()
    logger.info("Cron service stopped.")

@app.post("/sync-pos")
async def sync_pos():
    await sync_pos_use_case.execute()
    return {"message": "POS data synchronized successfully."}

@app.post("/webhook/orders")
async def handle_webhook(request: Request):
    payload = await request.json()
    await handle_webhook_use_case.execute(payload)
    return {"message": "Webhook received and processed successfully."}