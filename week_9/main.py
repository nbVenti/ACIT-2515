from flask import Flask, render_template, jsonify, request, redirect, url_for
from pathlib import Path
from db import db
from models import Customer, Product, Order

from routes import api_customer, api_product, api_order, endpoint


app = Flask(__name__)
app.register_blueprint(api_customer, url_prefix='/api/customers')
app.register_blueprint(api_product, url_prefix='/api/product')
app.register_blueprint(api_order, url_prefix='/api/order')
app.register_blueprint(endpoint, url_prefix='/')


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.instance_path = Path("data").resolve()

db.init_app(app)

# @app.route('/')
# def homepage():
#     return render_template("base.html")

# @app.route('/customers')
# def customer_list():
#     request = db.session.execute(db.select(Customer).order_by(Customer.id)) 
#     customers = []
#     for i in request.scalars():
#         u = {
#             "id": i.id, 
#             "name": i.name, 
#             "phone": i.phone, 
#             "balance": format(i.balance, '.2f')
#         }
#         customers.append(u)
    
#     return render_template("customers.html", customers=customers)

# @app.route('/products')
# def product_list():
#     request = db.session.execute(db.select(Product).order_by(Product.id)) 
#     products = []
#     for i in request.scalars():
#         u = {
#             "id": i.id, 
#             "product": i.product.capitalize(), 
#             "price": i.price, 
#             "available": i.available, 
#         }
#         products.append(u)
    
#     return render_template("products.html", products=products)

# @app.route('/orders')
# def orders_list():
#     orders = db.session.execute(db.select(Order).order_by(Order.id))
#     total_orders = []
#     for i in orders.scalars():
#         u = {
#             'id' : i.id,
#             'products': [f"{n.product.product} ({n.quantity})" for n in i.products],
#             'processed': None
#         }
#         u['processed'] = i.processed or "Not processed"
        
#         total_orders.append(u)
    
#     return render_template("orders.html", orders = total_orders)

# @app.route('/order/<int:ORDER_ID>')
# def order(ORDER_ID):
#     order = db.session.execute(db.select(Order).where(Order.id == ORDER_ID))
#     orders = []
#     for i in order.scalars():
#         u = {
#             'name': i.customer.name,
#             'balance': int(i.customer.balance),
#             'products': [f"{n.product.product} ({n.quantity} ${format((n.product.price*n.quantity),'.2f')})" for n in i.products],
#             'price':  Order.price(i),
#         }
        
#         orders.append(u)
#         # print(i.customer.name)
#         # print(int(i.customer.balance))
#         # for u in i.products:
#         #     print(u.product.product, u.quantity)
#         #     print(int(u.product.price) * u.quantity)
#         # print([f"{n.product.product} ({u.quantity})" for n, u in zip(i.products, i.products)])
#         # print(sum([int(u.product.price) * u.quantity for u in i.products]))
#     return render_template("detailed_order.html", id = ORDER_ID, orders = orders, customer_id=i.customer.id, processed = i.processed)

# @app.route("/customer/<int:id>")
# def detailed_customer(id):
#     records = db.session.execute(db.select(Customer).where(Customer.id == id))
#     customers = []
#     for i in records.scalars():
#         u = {
#             "id": i.id, 
#             "name": i.name, 
#             "phone": i.phone, 
#             'balance': int(i.balance), 
#             'orders': i.orders
#             }
#         # for j in u['orders']:
#         #     print(j)
#         #     for x in j.products:
#         #         print(x.product.product)
#         customers.append(u)
#         # print(i.orders[0].products[0].product.product)### this will diplay eggs if the id == 1    
#         # print(i.orders[0].products[0].product.price) ### search for customer Id, then search for the first index in the orders list, then searches for the fist index of the ProductOrder list, then searches for the term in the Product class
#         # print(i.orders[0].products[0].quantity) ### how much of each item was ordered
#     return render_template('detailed.html',customer=customers[0]['name'], id = id, customers=customers)
    
# @app.route('/api/customers')
# def customers_json():
#     records = db.session.execute(db.select(Customer).order_by(Customer.id))
#     cust = []
#     for i in records.scalars():
#         u = {
#             'id: ': i.id,
#             'name: ': i.name,
#             'phone: ': i.phone,
#             'balance: ': i.balance
#             }
#         cust.append(u)

#     return jsonify(cust)

# @app.route('/api/customers/<int:id>')
# def customer_json(id):
#     records = db.session.execute(db.select(Customer).where(Customer.id == id))
#     cust = []
#     for i in records.scalars():
#         u = {
#             'id: ': i.id,
#             'name: ': i.name,
#             'phone: ': i.phone,
#             'balance: ': i.balance
#             }
#         cust.append(u)
        
#     return jsonify(cust)

# @app.route('/api/products')
# def products_json():
#     records = db.session.execute(db.select(Product).order_by(Product.id))
#     prod = []
#     for i in records.scalars():
#         u = {
#             'id: ': i.id,
#             'product: ': i.product,
#             'price: ': i.price,
#             'available: ': i.available
#             }
#         prod.append(u)
    
#     return jsonify(prod)

# @app.route('/api/products/<int:id>')
# def product_json(id):
#     records = db.session.execute(db.select(Product).where(Product.id == id))
#     prod = []
#     for i in records.scalars():
#         u = {
#             'id: ': i.id,
#             'product: ': i.product,
#             'price: ': i.price,
#             'available: ': i.available
#             }
#         prod.append(u)
#     return jsonify(prod)

# @app.route('/api/customers', methods=['POST'])
# def add_customer():
#     data = request.get_json()
#     if data['name'] == '' or data['phone'] == '' or not data:
#         return jsonify({'status': 'error'}), 400
    
#     customer = Customer(name = data['name'], phone = data['phone'])
#     db.session.add(customer)
#     db.session.commit()
#     return jsonify({'status': 'success'}), 201

# @app.route('/api/customers/<int:cust_id>', methods=['PUT'])
# def all_bal(cust_id):   
#     data = request.get_json()
    
#     if not data:
#         return jsonify({'status': 'error'}), 400
#     records = Customer.query.get_or_404(cust_id)
#     records.balance = data['balance']
#     db.session.commit()
    
#     return jsonify({'id': records.id}), 201
    
# @app.route('/api/customers/<int:cust_id>', methods=['DELETE'])
# def delete_customer(cust_id):
#     customer = Customer.query.get_or_404(cust_id)
#     db.session.delete(customer)
#     db.session.commit()
#     return jsonify({'status': 'success'}), 201

# @app.route('/api/products', methods=['POST'])
# def add_product():
#     data = request.get_json()
#     if data['product'] == '' or data['price'] < 0 or not data:
#         return jsonify({'status': 'error'}), 400
    
#     product = Product(product = data['product'], price = data['price'])
#     if product:
#         db.session.add(product)
#         db.session.commit()
#         return jsonify({'status': 'success'}), 201
#     else:
#         return jsonify({'status': 'error'}), 400
    
# @app.route('/api/products/<int:prod_id>', methods=['PUT'])
# def update_product(prod_id):        
#     data = request.get_json()
    
#     if not data:
#         return jsonify({'status': 'error'}), 400
#     product = Product.query.get_or_404(prod_id)
#     if data['product'] == '':
#         data['prodcut'] = product.product
#     if data['price'] == '':
#         data['price'] = product.price
#     if data['available'] == '':
#         data['available'] = product.available
#     product.product = data['product']
#     product.price = data['price']
#     product.available = data['available']
#     db.session.commit()
      
#     return jsonify({'status': 'success'}), 201

# @app.route('/api/products/<int:prod_id>', methods=['DELETE'])
# def delete_product(prod_id):
#     product = Product.query.get_or_404(prod_id)
#     db.session.delete(product)
#     db.session.commit()
#     return jsonify({'status': 'success'}), 201

# @app.route('/api/orders', methods=['POST'])
# def add_order():
#     data = request.get_json()
#     if not data or data['customer_id'] == '' or len(data['items']) <= 0:
#         return jsonify({'status': 'error'}), 400
#     test_id = Customer.query.get_or_404(data['customer_id'])
    
#     order = Order(customer=test_id)
#     db.session.add(order)
    
#     for i in data['items']:
#         product = db.session.execute(db.select(Product).where(Product.product == i['name'])).scalar()
#         if not product:
#             return jsonify({'status': "error"}), 400
#         new_order = ProductOrder(order=order, product=product, quantity=i['quantity'])
#         db.session.add(new_order)
#     db.session.commit()   
        
#     return jsonify({'status': 'success'}), 201
    
# @app.route('/orders/<int:ORDER_ID>/delete', methods=['POST'])
# def delete_order(ORDER_ID):
#     order = Order.query.get_or_404(ORDER_ID)
#     if order.processed:
#         return redirect(url_for('orders_list'))
#     db.session.delete(order)
#     db.session.commit()
#     return redirect(url_for('orders_list'))

# @app.route('/api/orders/<int:ORDER_ID>', methods=['PUT'])
# def test_orders(ORDER_ID):
#     order = db.session.execute(db.select(Order).where(Order.id == ORDER_ID))
#     data = request.get_json()
#     if not data:
#         return jsonify({'status': 'error'}), 400
#     p = []
    
#     for i in order.scalars():
#         for __ in data:
#             if data['process'] == True:
#                 if 'strategy' in data:
#                     if data['strategy'] == "ignore":
#                         test = i.process("ignore")
#                     elif data['strategy'] == "reject":
#                         test = i.process("reject")
#                     else:
#                         test = i.process()  
#                 else:
#                     test = i.process() 
#             else:
#                 return jsonify({'status': 'error'}), 400      
#         x = {
#             "response":test
#         }
#         p.append(x)
#     db.session.commit()
#     return jsonify(p)

@app.route('/orders/<int:ORDER_ID>/process', methods=['POST'])
def process_order(ORDER_ID):
    order = Order.query.get_or_404(ORDER_ID)
    if order.processed:
        return redirect(url_for('orders_list'))
    order.process()
    db.session.commit()
    return redirect(url_for('orders_list'))

if __name__ == '__main__':
    app.run(debug=True, port=3000)
    
