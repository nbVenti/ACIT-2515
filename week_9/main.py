from flask import Flask, render_template, redirect, url_for
from csv import DictReader
from pathlib import Path
from db import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.instance_path = Path("data").resolve()

db.init_app(app)

@app.route('/')
def homepage():
    return render_template("base.html")

@app.route('/customers')
def customer_list():
    print("Customers")
    with open('./data/customers.csv', 'r') as file:
        reader = DictReader(file)
        customers = list(reader)
    return render_template("customers.html", customers=customers)

@app.route('/products')
def product_list():
    print("Products")
    with open('./data/products.csv', 'r') as file:
        reader = DictReader(file)
        products = list(reader)
        for i in products:
            i["price"] = float(i["price"])
            i["name"] = i["name"].capitalize()
    return render_template("products.html", products=products)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
    
