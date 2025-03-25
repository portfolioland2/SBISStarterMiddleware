from apscheduler.schedulers.asyncio import AsyncIOScheduler
from core.use_cases.fetch_data_from_sbis import FetchDataFromSbis
from adapters.sbis_adapter import SbisAdapter
from infrastructure.config_manager import config

class CronService:
    def __init__(self):
        self.scheduler = AsyncIOScheduler()

    async def start(self):
        
        sbis_adapter = SbisAdapter(
            base_url=config.sbis_base_url,
            api_key=config.sbis_api_key
        )
        fetch_data_use_case = FetchDataFromSbis(sbis_adapter)

        
        self.scheduler.add_job(
            fetch_data_use_case.execute,
            "cron",
            hour="*", 
            minute="0"
        )
        self.scheduler.start()

    async def stop(self):
        self.scheduler.shutdown()