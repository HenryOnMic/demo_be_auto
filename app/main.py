from fastapi import FastAPI, status, HTTPException, Response, Depends
from pydantic import BaseModel, EmailStr
from typing import List
from uuid import uuid4
from app.db import get_db
from motor.motor_asyncio import AsyncIOMotorDatabase

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int

class User(UserCreate):
    id: str

def clean_user(user):
    if user is None:
        return None
    user = dict(user)
    user.pop('_id', None)
    # Ensure all required fields are present and are strings where needed
    return {
        'id': str(user.get('id', '')),
        'name': str(user.get('name', '')),
        'email': str(user.get('email', '')),
        'age': int(user.get('age', 0)),
    }

@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: AsyncIOMotorDatabase = Depends(get_db)):
    user_dict = user.dict()
    user_dict["id"] = str(uuid4())
    await db["users"].insert_one(user_dict)
    return User(**clean_user(user_dict))

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: str, db: AsyncIOMotorDatabase = Depends(get_db)):
    user = await db["users"].find_one({"id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return User(**clean_user(user))

@app.get("/users/", response_model=List[User])
async def list_users(db: AsyncIOMotorDatabase = Depends(get_db)):
    users = []
    async for user in db["users"].find():
        users.append(User(**clean_user(user)))
    return users

@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: str, user: UserCreate, db: AsyncIOMotorDatabase = Depends(get_db)):
    result = await db["users"].update_one({"id": user_id}, {"$set": user.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    updated = await db["users"].find_one({"id": user_id})
    return User(**clean_user(updated))

@app.delete("/users/{user_id}", status_code=204)
async def delete_user(user_id: str, db: AsyncIOMotorDatabase = Depends(get_db)):
    result = await db["users"].delete_one({"id": user_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return Response(status_code=204) 