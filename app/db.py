from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from typing import AsyncGenerator
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27027")
DB_NAME = os.getenv("MONGO_DB", "test_demo14")

async def get_db() -> AsyncGenerator:
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[DB_NAME]
    try:
        yield db
    finally:
        client.close() 