from fastapi import APIRouter, HTTPException
from models import User
from db import users_collection
# import pdb

router = APIRouter()

async def create_user(user: User):
    user_dict = user.dict()
    existing_user = users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    users_collection.insert_one(user_dict)
    return user

async def get_users():
    # pdb.set_trace()
    users = list(users_collection.find({}, {"_id": 0}))
    return users
