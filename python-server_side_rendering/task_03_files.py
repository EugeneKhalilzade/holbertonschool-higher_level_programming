from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_data():
    """Read data from JSON file"""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def read_csv_data():
    """Read data from CSV file"""
    products = []
    try:
        with open('products.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convert id to integer and price to float for consistency
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
        return products
    except FileNotFoundError:
        return []

@app.route('/products')
def display_products():
    # Get query parameters
    source = request.args.get('source', '')
    product_id = request.args.get('id')
    
    # Initialize variables
    products = []
    error_message = None
    
    # Read data based on source parameter
    if source == 'json':
        products = read_json_data()
    elif source == 'csv':
        products = read_csv_data()
    else:
        error_message = "Wrong source"
    
    # Filter by ID if provided
    if product_id and not error_message:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products if p['id'] == product_id]
            if filtered_products:
                products = filtered_products
            else:
                error_message = "Product not found"
        except ValueError:
            error_message = "Invalid ID format"
    
    # Render template with products and error message
    return render_template('product_display.html', 
                           products=products, 
                           error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)