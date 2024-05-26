from sqlalchemy.ext.asyncio import create_async_engine,AsyncEngine,AsyncSession
from sqlalchemy.orm import sessionmaker
from configs import settings

engine:AsyncEngine = create_async_engine(settings.DATABASE_URL)

Session:AsyncSession = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)