from db import db
from main import app
from models import Customer, Product, Order, ProductOrder
from csv import DictReader
from sqlalchemy.sql import functions as func
import random

def populate_customer_datebase():
    with app.app_context():
        with open('./data/customers.csv', 'r') as file:
            reader = DictReader(file)
            customers = list(reader)
            for i in customers:
                customers = Customer(name = i['name'],phone = i['phone'], balance = int(0.0))
                db.session.add(customers)
            db.session.commit()
            
def populate_product_datebase():
    with app.app_context():
        with open('./data/products.csv', 'r') as file:
            reader = DictReader(file)
            products = list(reader)
            for i in products:
                products = Product(product = i['name'],price = i['price'], available = int(10.0))
                db.session.add(products)
            db.session.commit()
            
            
def rand_order():
    for __ in range(2):
        record = db.select(Customer).order_by(func.random()).limit(1)
        rand_cust = db.session.execute(record).scalar()
        
        order = Order(customer=rand_cust)
        db.session.add(order)
        
        prod_record = db.select(Product).order_by(func.random()).limit(1)
        rand_prod = db.session.execute(prod_record).scalar()
        qty = random.randint(10,20)
        
        new_order = ProductOrder(order=order,product=rand_prod,quantity=qty)
        db.session.add(new_order)
        
        prod_record = db.select(Product).order_by(func.random()).limit(1)
        rand_prod = db.session.execute(prod_record).scalar()
        qty = random.randint(10,20)
        
        new_order2 = ProductOrder(order=order,product=rand_prod,quantity=qty)
        db.session.add(new_order2)
        db.session.commit()
    
if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
        populate_customer_datebase()
        populate_product_datebase()
        rand_order()
        
        