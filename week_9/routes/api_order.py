from flask import Blueprint, request, jsonify
from db import db
from models import Order

api_order = Blueprint('api_order', __name__)

@api_order.route('/', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([order.to_json() for order in orders])

@api_order.route('/<int:id>/process>', methods=['PUT'])
def test_orders(id):
    order = db.session.execute(db.select(Order).where(Order.id == id))
    data = request.get_json()
    if not data:
        return jsonify({'status': 'error'}), 400
    p = []
    
    for i in order.scalars():
        for __ in data:
            if data['process'] == True:
                if 'strategy' in data:
                    if data['strategy'] == "ignore":
                        test = i.process("ignore")
                    elif data['strategy'] == "reject":
                        test = i.process("reject")
                    else:
                        test = i.process()  
                else:
                    test = i.process() 
            else:
                return jsonify({'status': 'error'}), 400      
        x = {
            "response":test
        }
        p.append(x)
    db.session.commit()
    return jsonify(p)
