from fastapi import APIRouter
from models import Payment
from services.payments import create_payment, get_all_payments, refund_payment, track_refund_status

router = APIRouter()

@router.post("/payments", response_model=Payment)
async def create_payment_api(payment: Payment):
   # API endpoint to create a new payment
    return create_payment(payment)

@router.get("/payments")
async def get_payments_api():
    # API endpoint to fetch all payments
    return get_all_payments()


@router.put("/payments/{payment_id}/refund")
async def refund_payment_api(payment_id: str):
    return await refund_payment(payment_id)

@router.get("/payments/{payment_id}/status")
async def track_refund_status_api(payment_id: str):
    return await track_refund_status(payment_id)