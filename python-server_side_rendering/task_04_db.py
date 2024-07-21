from flask import Flask, render_template, request
import json
import csv
import sqlite3
app = Flask(__name__)

def read_csv_file(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
    
def read_sqlite_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    products = [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in rows]
    conn.close()
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    products = []
    error = None

    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    elif source == 'sql':
        try:
            products = read_sqlite_db('products.db')
        except Exception as e:
            error = f"Database error: {e}"
            raise 'Database error'
    else:
        error = 'Wrong source. Please specify "json" or "csv".'
        raise 'Wrong source. Please specify "json" or "csv".'
    
    return render_template('product_display.html', products=products, error=error)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get("items", [])
    except FileNotFoundError:
        items_list = []
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)