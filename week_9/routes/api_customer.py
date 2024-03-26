from flask import Blueprint, request, jsonify
from db import db
from models import Customer

api_customer = Blueprint('api_customer', __name__)

@api_customer.route('/', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([customer.to_jsonialize() for customer in customers])

@api_customer.route('/', methods=['POST'])
def create_customer():
    data = request.get_json()
    if data['name'] == '' or data['phone'] == '' or not data:
        return jsonify({'status': 'error'}), 400
    
    customer = Customer(name = data['name'], phone = data['phone'])
    db.session.add(customer)
    db.session.commit()
    return jsonify({'status': 'success'}), 201

@api_customer.route('/<int:id>', methods=['GET'])
def get_customer(id):
    customer = Customer.query.get(id)
    if not customer:
        return jsonify({'status': 'error'}), 404
    return jsonify(customer.to_jsonialize())

@api_customer.route('/<int:id>', methods=['DELETE'])
def delete_customer(cust_id):
    customer = Customer.query.get_or_404(cust_id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({'status': 'success'})

@api_customer.route('/<int:id>', methods=['PUT'])
def all_bal(id):
    data = request.get_json()
    if not data:
        return jsonify({'status': 'error'}), 400
    records = Customer.query.get_or_404(id)
    records.balance = data['balance']
    db.session.commit()
    
    return jsonify({'id': records.id}), 201