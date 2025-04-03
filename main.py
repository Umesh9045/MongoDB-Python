from fastapi import FastAPI
from routes.users import router as users_router
from routes.payments import router as payments_router

app = FastAPI(title="Payment Gateway API")

# Register routers
app.include_router(users_router, prefix="/api")
app.include_router(payments_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Payment Gateway API is running!"}
