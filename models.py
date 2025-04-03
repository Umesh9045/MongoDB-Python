from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    name: str
    email: str
    created_at: Optional[datetime] = datetime.utcnow()

class Payment(BaseModel):
    user_id: str
    amount: float
    currency: str
    status: str = "pending"  # default status
    created_at: Optional[datetime] = datetime.utcnow()
    