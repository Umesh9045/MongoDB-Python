from db import payments_collection
from models import Payment
from fastapi import HTTPException
from bson import ObjectId

async def refund_payment(payment_id: str):
    # pdb.set_trace()
    # Update payment and set both `payment_status` and `refund_status`
    payment = payments_collection.find_one_and_update(
        {"_id": ObjectId(payment_id), "payment_status": {"$ne": "Refunded"}},
        {"$set": {"payment_status": "Refunded", "refund_status": "Refund Initiated"}},
        return_document=True  # Returns the updated document after modification
    )

    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found or already refunded")

    return {"message": "Refund initiated successfully", "refund_id": payment_id}

async def track_refund_status(refund_id: str):
    payment = payments_collection.find_one({"_id": ObjectId(refund_id)}, {"_id": 0})
    
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    
    return {"refund_id": refund_id, "status": payment["refund_status"]}
