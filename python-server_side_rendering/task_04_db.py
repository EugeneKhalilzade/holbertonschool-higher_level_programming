import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to read products from a JSON file
def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

# Function to read products from a CSV file
def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products

# Function to read products from an SQLite database
def read_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        products = [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in rows]
        conn.close()
        return products
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

# Route to handle displaying products
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql()
    else:
        return render_template('product_display.html', error="Wrong source. Please use 'json', 'csv', or 'sql'.")

    # If ID is provided, filter by ID
    if product_id:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found.")
    
    return render_template('product_display.html', products=products)

if __name__ == "__main__":
    app.run(debug=True)
