from fastapi import APIRouter

payment_router = APIRouter()


@payment_router.post("")
def execute_payment():
    # 1. Verify that the card id is associated with an existing user
    # 2. Verify that the user has enough money to pass the order
    # 3. Subtract the order amount from user balance
    # 4. Create a new order for the user
    # 5. Return response to client
    return {"message": "payment API in progress..."}
