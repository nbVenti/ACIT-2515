from sqlalchemy import Float, Numeric, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.sql import functions as func
from datetime import datetime

from db import db

class Customer(db.Model):
 id = mapped_column(Integer, primary_key=True)
 name = mapped_column(String(200), nullable=False, unique=True)
 phone = mapped_column(String(20), nullable=False)
 balance = mapped_column(Numeric, nullable=False, default=0.0)
 orders = relationship("Order")
 def to_json(self):
     return {
         'id': self.id,
         'name': self.name,
         'phone': self.phone,
         'balance': self.balance
         }

class Product(db.Model):
 id = mapped_column(Integer, primary_key=True)
 product = mapped_column(String(200), nullable=False, unique=True)
 price = mapped_column(Float(200), nullable=False)
 available = mapped_column(Integer, nullable=False, default=True)
 orders = relationship("ProductOrder")
 def to_json(self):
     return {
         'id': self.id,
         'product': self.product,
         'price': self.price,
         'available': self.available
         }

class Order(db.Model):
    id = mapped_column(Integer, primary_key=True)
    customer_id = mapped_column(Integer, ForeignKey(Customer.id), nullable=False)
    total = mapped_column(Float(200))   
    created = mapped_column(DateTime,nullable=False,default=func.now())
    processed = mapped_column(DateTime, nullable=True)
    customer = relationship("Customer", back_populates="orders")
    products = relationship("ProductOrder", back_populates="order", cascade="all, delete-orphan")
    def process(self,strategy="adjust"):
        if self.processed == 'None':
            return False, "Already processed"
        if (self.customer.balance <= 0 ):
            return False, "Poor lol"
        for u in self.products:
            if u.quantity > u.product.available:
                if strategy == "adjust":
                    u.quantity = u.product.available #adjust
                if strategy == "reject":
                    return False, "Order too big"
                if strategy == "ignore":
                    u.quantity = 0 # ignore
                    
            u.product.available = u.product.available - u.quantity
            self.customer.balance = self.customer.balance - int(u.product.price * u.quantity )
            self.processed = datetime.now()
        return True, self.processed
        
        # if self.products.quantity > self.products.product.available
    def price(self):
        # for u in i.products:
        return format((sum([(u.product.price) * u.quantity for u in self.products])), '.2f')
class ProductOrder(db.Model):
    id = mapped_column(Integer, primary_key=True)
    order_id = mapped_column(Integer, ForeignKey(Order.id),nullable=False)
    product_id = mapped_column(Integer, ForeignKey(Product.id),nullable=False)
    quantity = mapped_column(Integer, nullable=False)
    product = relationship("Product",back_populates="orders")
    order = relationship("Order", back_populates="products")