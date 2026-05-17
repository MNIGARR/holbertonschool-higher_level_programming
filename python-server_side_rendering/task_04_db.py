import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv(filename):
    products = []
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except (FileNotFoundError, KeyError, ValueError):
        pass
    return products

def read_sql(product_id=None):
    products = []
    try:
        conn = sqlite3.connect('products.db')
        # This makes rows behave like dictionaries: row['name'] instead of row[1]
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        if product_id:
            cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
            row = cursor.fetchone()
            if row:
                products.append(dict(row))
        else:
            cursor.execute('SELECT * FROM Products')
            products = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    # Validate Source
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # Load Data based on source
    if source == 'json':
        data = read_json('products.json')
        if product_id:
            data = [p for p in data if p.get('id') == product_id]
    elif source == 'csv':
        data = read_csv('products.csv')
        if product_id:
            data = [p for p in data if p.get('id') == product_id]
    elif source == 'sql':
        data = read_sql(product_id)

    # Handle "Product not found"
    if product_id and not data:
        return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
