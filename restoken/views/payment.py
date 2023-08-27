from fastapi import APIRouter

payment_router = APIRouter()


@payment_router.post("")
def execute_payment():
    # Client request:
    # {
    #   "customer_id": "fc631ceb-4a84-4cfc-b5fe-526c1009d142",
    #   "restaurant_id": 2,
    #   "amount": 15,
    #   "timestamp": 1693152741
    # }

    # 1. Receive JSON message(user id, restaurant id, amount, timestamp)
    # 2. Verify that the user with the user id exists
    # 3. Verify that the restaurant with the restaurant id exists
    # 4. Verify that the user has enough money ((balance - amount) > 0)
    # 5. Create an Order(user id, restaurant id, amount, timestamp)
    # 6. Execute payment (balance = balance - amount)
    # 7. Build response (status + error message if any)
    # 8. Return response to client
    return {"message": "payment API in progress..."}
