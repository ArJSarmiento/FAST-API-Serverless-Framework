from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_AUTH_BASE_URL: str 
    APP_HUB_BASE_URL: str
    APP_ID: str 
    APP_SECRET: str 
    APP_USERNAME: str 
    APP_PASSWORD: str
    class Config:
        env_file = '.env' 

settings = Settings()