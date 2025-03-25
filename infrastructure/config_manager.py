from pydantic_settings import BaseSettings
from pydantic import Field

class ConfigManager(BaseSettings):
    
    base_url: str = Field(..., env="BASE_URL")
    sbis_auth_url: str = Field(..., env="SBIS_AUTH_URL")
    sbis_app_client_id: str = Field(..., env="SBIS_APP_CLIENT_ID")
    sbis_app_secret: str = Field(..., env="SBIS_APP_SECRET")
    sbis_secret_key: str = Field(..., env="SBIS_SECRET_KEY")
    sbis_base_url: str = Field(..., env="SBIS_BASE_URL")
    starter_base_url: str = Field(..., env="STARTER_BASE_URL")
    starter_api_key: str = Field(..., env="STARTER_API_KEY")
    #cron_schedule: str = Field("0 0 * * *", env="CRON_SCHEDULE")

    
  #TODO:  cron_schedule: str = "0 0 * * *"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

config = ConfigManager()
print("Loaded config:", config.model_dump())