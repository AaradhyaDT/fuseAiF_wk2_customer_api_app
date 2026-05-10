# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session
from app import models, schemas
from app.logger import logger

def get_customers(db: Session, skip: int = 0, limit: int = 100):
    logger.info(f"Fetching customers — skip = {skip}, limit = {limit}")
    return db.query(models.Customer).offset(skip).limit(limit).all()

def get_customer(db: Session, customer_id: int):
    logger.info(f"Fetching customer {customer_id}")
    return db.query(models.Customer).filter(models.Customer.customerNumber == customer_id).first()

def create_customer(db: Session, customer: schemas.CustomerCreate) -> models.Customer:
    logger.info(f"Creating customer with name {customer.customerName}")
    db_customer = models.Customer(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def update_customer(db, customer_id, customer: schemas.CustomerUpdate) -> models.Customer:
    logger.info(f"Updating customer {customer_id}")
    db_customer = get_customer(db, customer_id)
    for key, value in customer.model_dump(exclude_unset = True).items():
        setattr(db_customer,key,value)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def delete_customer(db, customer_id):
    logger.info(f"Deleting customer {customer_id}")
    db_customer = get_customer(db,customer_id)
    db.delete(db_customer)
    db.commit()
    return db_customer

def get_customer_orders(db: Session, customer_id: int, skip: int = 0, limit: int = 100):
    logger.info(f"Fetching orders for customer {customer_id} — skip = {skip}, limit = {limit}")
    return db.query(models.Order).filter(models.Order.customerNumber == customer_id).offset(skip).limit(limit).all()

def get_customer_payments(db: Session, customer_id: int, skip: int = 0, limit: int = 100):
    logger.info(f"Fetching payments for customer {customer_id} — skip = {skip}, limit = {limit}")
    return db.query(models.Payment).filter(models.Payment.customerNumber == customer_id).offset(skip).limit(limit).all()
