from fastapi import APIRouter
from models import User
from services.users import create_user, get_users


router = APIRouter()

@router.post("/users", response_model=User)
async def create_user_api(user: User):
    return  await create_user(user)

@router.get("/users")
async def get_users_api():
    return await get_users()
