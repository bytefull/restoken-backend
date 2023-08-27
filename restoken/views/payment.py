from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import restoken.schemas.payment as payment_schema
import restoken.schemas.order as order_schema
from restoken.database import get_db
import restoken.models.user as customer_model
import restoken.models.restaurant as restaurant_model
import restoken.models.order as order_model
import restoken.crud.order as order_crud

payment_router = APIRouter()


def create_order_from_payment(db: Session, payment: payment_schema.PaymentCreate):
    db_order = order_model.Order(
        amount=payment.amount,
        customer_id=payment.customer_id,
        restaurant_id=payment.restaurant_id,
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


@payment_router.post("", response_model=payment_schema.PaymentResult)
def execute_payment(
    payment: payment_schema.PaymentCreate, db: Session = Depends(get_db)
):
    # Client request:
    # {
    #   "customer_id": "fc631ceb-4a84-4cfc-b5fe-526c1009d142",
    #   "restaurant_id": 2,
    #   "amount": 15,
    #   "timestamp": 1693152741
    # }

    # 1. Receive JSON message(customer id, restaurant id, amount, timestamp)
    # 2. Verify that the customer with the customer id exists
    db_user = (
        db.query(customer_model.User)
        .filter(customer_model.User.id == payment.customer_id)
        .first()
    )
    if not db_user:
        return {"status": "customer not found"}

    # 3. Verify that the restaurant with the restaurant id exists
    db_restaurant = (
        db.query(restaurant_model.Restaurant)
        .filter(restaurant_model.Restaurant.id == payment.restaurant_id)
        .first()
    )
    if not db_restaurant:
        return {"status": "restaurant not found"}

    # 4. Verify that the customer has enough money ((balance - amount) > 0)
    print("db_user.balance = {}".format(db_user.balance))
    print("payment.amount = {}".format(payment.amount))
    if (db_user.balance - payment.amount) < 0:
        return {"status": "doesn't have enough money"}

    # 5. Create an Order(customer id, restaurant id, amount, timestamp)
    db_order = create_order_from_payment(db, payment)
    if db_order is None:
        return {"status": "failed to create order in database"}

    # 6. Execute payment (balance = balance - amount) by updating user balance
    db_user.balance = db_user.balance - payment.amount
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # 7. Return response to client
    return {"status": "payment success"}
