from db import db
from main import app
from models import Customer, Product
from csv import DictReader

def populate_customer_datebase():
    with app.app_context():
        with open('./data/customers.csv', 'r') as file:
            reader = DictReader(file)
            customers = list(reader)
            for i in customers:
                customers = Customer(name = i['name'],phone = i['phone'], balance = int(0))
                db.session.add(customers)
            db.session.commit()
            
    

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
        populate_customer_datebase()
