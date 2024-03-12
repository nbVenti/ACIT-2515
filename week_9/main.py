from flask import Flask, render_template, redirect, url_for, jsonify, request
from pathlib import Path
from db import db
from models import Customer, Product
from csv import DictReader



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.instance_path = Path("data").resolve()

db.init_app(app)

@app.route('/')
def homepage():
    return render_template("base.html")

@app.route('/customers')
def customer_list():
    request = db.session.execute(db.select(Customer).order_by(Customer.id)) 
    customers = []
    for i in request.scalars():
        u = {
            "id": i.id, 
            "name": i.name, 
            "phone": i.phone, 
            "balance": i.balance, 
        }
        customers.append(u)
    
    return render_template("customers.html", customers=customers)

@app.route('/products')
def product_list():
    request = db.session.execute(db.select(Product).order_by(Product.id)) 
    products = []
    for i in request.scalars():
        u = {
            "id": i.id, 
            "product": i.product.capitalize(), 
            "price": i.price, 
            "available": i.available, 
        }
        products.append(u)
    
    return render_template("products.html", products=products)

@app.route('/api/customers')
def customers_json():
    records = db.session.execute(db.select(Customer).order_by(Customer.id))
    cust = []
    for i in records.scalars():
        u = {
            'id: ': i.id,
            'name: ': i.name,
            'phone: ': i.phone,
            'balance: ': i.balance
            }
        cust.append(u)
    # return(cust)
    return jsonify(cust)

@app.route('/api/customers/<int:id>')
def customer_json(id):
    records = db.session.execute(db.select(Customer).where(Customer.id == id))
    cust = []
    for i in records.scalars():
        u = {
            'id: ': i.id,
            'name: ': i.name,
            'phone: ': i.phone,
            'balance: ': i.balance
            }
        cust.append(u)
        
    return jsonify(cust)

@app.route('/api/products')
def products_json():
    records = db.session.execute(db.select(Product).order_by(Product.id))
    prod = []
    for i in records.scalars():
        u = {
            'id: ': i.id,
            'product: ': i.product,
            'price: ': i.price,
            'available: ': i.available
            }
        prod.append(u)
    
    return jsonify(prod)

@app.route('/api/products/<int:id>')
def product_json(id):
    records = db.session.execute(db.select(Product).where(Product.id == id))
    prod = []
    for i in records.scalars():
        u = {
            'id: ': i.id,
            'product: ': i.product,
            'price: ': i.price,
            'available: ': i.available
            }
        prod.append(u)
        
    return jsonify(prod)

@app.route('/api/customers', methods=['POST'])
def add_customer():
    data = request.get_json()
    if data['name'] == '' or data['phone'] == '' or not data:
        return jsonify({'status': 'error'}), 400
    
    customer = Customer(name = data['name'], phone = data['phone'])
    db.session.add(customer)
    db.session.commit()
    return jsonify({'status': 'success'}), 201

@app.route('/api/customers/<int:cust_id>', methods=['PUT'])
def all_bal(cust_id):   
    data = request.get_json()
    
    if not data:
        return jsonify({'status': 'error'}), 400
    records = Customer.query.get_or_404(cust_id)
    records.balance = data['balance']
    db.session.commit()
    
    return jsonify({'id': records.id}), 201
    
@app.route('/api/customers/<int:cust_id>', methods=['DELETE'])
def delete_customer(cust_id):
    customer = Customer.query.get_or_404(cust_id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({'status': 'success'}), 201

@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if data['product'] == '' or data['price'] < 0 or not data:
        return jsonify({'status': 'error'}), 400
    
    product = Product(product = data['product'], price = data['price'])
    if product:
        db.session.add(product)
        db.session.commit()
        return jsonify({'status': 'success'}), 201
    else:
        return jsonify({'status': 'error'}), 400
    
@app.route('/api/products/<int:prod_id>', methods=['PUT'])
def update_product(prod_id):        
    data = request.get_json()
    
    if not data:
        return jsonify({'status': 'error'}), 400
    product = Product.query.get_or_404(prod_id)
    product.product = data['product']
    product.price = data['price']
    product.available = data['available']
    db.session.commit()
      
    return jsonify({'status': 'success'}), 201

@app.route('/api/products/<int:prod_id>', methods=['DELETE'])
def delete_product(prod_id):
    product = Product.query.get_or_404(prod_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'status': 'success'}), 201



if __name__ == '__main__':
    app.run(debug=True, port=3000)
    
