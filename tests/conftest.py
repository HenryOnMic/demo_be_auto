import pytest
import motor.motor_asyncio
import asyncio
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27027")
DB_NAME = os.getenv("MONGO_DB", "test_demo14")

@pytest.fixture(autouse=True, scope="function")
def clear_users_collection():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
    db = client[DB_NAME]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(db["users"].delete_many({}))
    yield
    client.close() 