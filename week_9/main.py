from flask import Flask
from pathlib import Path
from db import db
from manage import create
from demo import demo

from routes import api_customer, api_product, api_order, endpoint


app = Flask(__name__)
app.register_blueprint(api_customer, url_prefix='/api/customers')
app.register_blueprint(api_product, url_prefix='/api/product')
app.register_blueprint(api_order, url_prefix='/api/order')
app.register_blueprint(endpoint, url_prefix='/')


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.instance_path = Path("data").resolve()

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
    create()
    demo()
    
    
