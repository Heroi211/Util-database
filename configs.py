from pydantic.v1 import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    DATABASE_USER:str = ""
    DATABASE_PASS:str = ""
    DATABASE_NAME:str = ""
    DATABASE_HOST:str = ""
    DATABASE_PORT:str = ""
    
    DATABASE_URL:str = f"postgresql:asyncpg"
    
    DB_base = declarative_base()
    
    class Config:
        case_sensitive = True
        
settings : Settings = Settings()