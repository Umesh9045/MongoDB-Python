from db import payments_collection
from models import Payment
from fastapi import HTTPException
from bson import ObjectId

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

async def track_refund_status(refund_id: str):
    payment = payments_collection.find_one({"_id": ObjectId(refund_id)}, {"_id": 0})
    
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    
    return {"refund_id": refund_id, "status": payment["payment_status"]}
