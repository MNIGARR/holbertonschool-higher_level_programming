import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json(filename):
    """Reads a JSON file and returns a list of dictionaries."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv(filename):
    """Reads a CSV file and returns a list of dictionaries."""
    products = []
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert types for consistency with JSON
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except (FileNotFoundError, KeyError, ValueError):
        pass
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    # 1. Handle Invalid Source
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # 2. Load Data
    if source == 'json':
        data = read_json('products.json')
    else:
        data = read_csv('products.csv')

    # 3. Filter by ID if provided
    if product_id:
        data = [p for p in data if p.get('id') == product_id]
        if not data:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
