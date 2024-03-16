from sqlalchemy import Float, Numeric, ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column, relationship

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
    customer = relationship("Customer", back_populates="orders")
    products = relationship("ProductOrder", back_populates="order", cascade="all, delete-orphan")

class ProductOrder(db.Model):
    id = mapped_column(Integer, primary_key=True)
    order_id = mapped_column(Integer, ForeignKey(Order.id),nullable=False)
    product_id = mapped_column(Integer, ForeignKey(Product.id),nullable=False)
    product = relationship("Product",back_populates="orders")
    order = relationship("Order", back_populates="products")
    quantity = mapped_column(Integer, nullable=False)