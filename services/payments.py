from db import payments_collection
from models import Payment
from fastapi import HTTPException
from bson import ObjectId

# import pdb

def create_payment(payment: Payment):
    """Handles payment processing and inserts into MongoDB"""
    payment_dict = payment.dict()

    # Insert payment into DB
    result = payments_collection.insert_one(payment_dict)
    
    # Error Handling
    if not result.inserted_id:
        raise HTTPException(status_code=500, detail="Payment processing failed")
    
    return payment

def get_all_payments():
    """Retrieves all payment records from MongoDB"""
    payments = list(payments_collection.find({}))  
    for payment in payments:
        payment["_id"] = str(payment["_id"])
    return payments
