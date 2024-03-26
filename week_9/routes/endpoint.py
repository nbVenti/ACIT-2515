from flask import Blueprint, render_template, redirect, url_for, request
from db import db
from models import Customer, Order, Product

endpoint = Blueprint('pages', __name__)

@endpoint.route('/')
def homepage():
    return render_template("base.html")

@endpoint.route('/customers', methods=['GET'])
def get_customers():
    request = db.session.execute(db.select(Customer).order_by(Customer.id)) 
    customers = []
    for i in request.scalars():
        u = {
            "id": i.id, 
            "name": i.name, 
            "phone": i.phone, 
            "balance": format(i.balance, '.2f')
        }
        customers.append(u)
    
    return render_template("customers.html", customers=customers)

@endpoint.route('/products', methods=['GET'])
def get_products():
    request = db.session.execute(db.select(Product).order_by(Product.id)) 
    products = []
    for i in request.scalars():
        u = {
            "id": i.id, 
            "product": i.product.capitalize(), 
            "price": format(i.price, '.2f'), 
            "available": i.available
        }
        products.append(u)
    
    return render_template("products.html", products=products)

@endpoint.route('/orders', methods=['GET'])
def get_orders():
    request = db.session.execute(db.select(Order).order_by(Order.id)) 
    orders = []
    for i in request.scalars():
        u = {
            "id": i.id, 
            "customer_id": i.customer_id, 
            "products": [f"{n.product.product} ({n.quantity})" for n in i.products], 
            "processed": None
        }
        u['processed'] = i.processed or "Not processed"
        
        orders.append(u)
    
    return render_template("./orders.html", orders=orders)

@endpoint.route('/order/<int:id>', methods=['GET'])
def get_order(id):
    order = db.session.execute(db.select(Order).where(Order.id == id)).scalars().first()
    if not order:
        return redirect(url_for('pages.get_orders'))
    orders = []
    u = {
        'name': order.customer.name,
        'balance': int(order.customer.balance),
        'orders': [f"{n.product.product} ({n.quantity} ${format((n.product.price*n.quantity),'.2f')})" for n in order.products],
        'price':  Order.price(order),
    }
    orders.append(u)
    print(orders)
    return render_template("detailed_order.html",id = id, orders = orders, customer_id=order.customer.id, processed = order.processed)

@endpoint.route('/customer/<int:id>', methods=['GET'])
def get_customer(id):
    customer = db.session.execute(db.select(Customer).where(Customer.id == id)).scalars().first()
    if not customer:
        return redirect(url_for('html.get_customers'))
    
    customers = []
    
    u = {
        "id": customer.id, 
        "name": customer.name, 
        "phone": customer.phone, 
        'balance': int(customer.balance), 
        'orders': customer.orders
    }
    customers.append(u)
    
    return render_template("detailed.html",id = id, customer = customer.name, customers = customers)

@endpoint.route('/orders/<int:id>/delete', methods=['POST'])
def delete_order(id):
    order = Order.query.get_or_404(id)
    if order.processed:
        return redirect(url_for('pages.get_orders'))
    db.session.delete(order)
    db.session.commit()
    return redirect(url_for('pages.get_orders'))

@endpoint.route('/orders/<int:id>/process', methods=['POST'])
def process_order(id):
    order = Order.query.get_or_404(id)
    if order.processed:
        return redirect(url_for('pages.get_orders'))
    order.process()
    db.session.commit()
    return redirect(url_for('pages.get_orders'))
