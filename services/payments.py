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

async def refund_payment(payment_id: str):
    # pdb.set_trace()
    payment = payments_collection.find_one({"_id": ObjectId(payment_id)})
    
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    
    if payment.get("payment_status") == "Refunded":
        raise HTTPException(status_code=400, detail="Payment is already refunded")
    
    payments_collection.update_one(
        {"_id": ObjectId(payment_id)},
        {"$set": {"payment_status": "Refunded"}}
    )
    
    return {"message": "Payment refunded successfully"}

async def track_refund_status(payment_id: str):
    payment = payments_collection.find_one({"_id": ObjectId(payment_id)}, {"_id": 0})
    
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    
    return {"payment_id": payment_id, "status": payment["payment_status"]}
