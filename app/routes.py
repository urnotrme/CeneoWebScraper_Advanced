from app import app
from flask import render_template, request

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/extraction', methods=["POST", "GET"])
def extraction():
    if request.method == "POST":
        # coś
        a=0
    else:
        return render_template("extraction.html")

@app.route('/product/<product_id>')
def product():
    return render_template("product.html")

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/about')
def about():
    return render_template("about.html")