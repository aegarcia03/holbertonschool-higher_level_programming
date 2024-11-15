from flask import Flask, render_template, request
import json, csv

app = Flask(__name__)

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
    with open('items.json') as json_file:
        data = json.load(json_file)
        items_list = data.get("items", [])

    return render_template('items.html', items = items_list)

def read_json():
    with open('products.json', 'r') as file:
        data = json.load(file)
        return file

def read_csv():
    with open('products.csv', newline='') as file:
        product_list = []
        csv_file = csv.DictReader(file)
        for row in csv_file:
            product_list.append(row)

    return product_list

@app.route('/products')
def products():
    source = request.args.get('source').lower()
    p_id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error='Wrong source')
    if source == 'json':
        products = read_json()  
    elif source == 'csv':
        products = read_csv()
    
    if p_id:
        try:
            p_id = int(p_id)
            filtered_p = [product for product in products if product['id'] == p_id]

            if not filtered_p:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.hmtl', error="Invalid product id")
    else:
        filtered_p = products
    

    return render_template('product_display.html', products=filtered_p)

if __name__ == '__main__':
    app.run(debug=True, port=5000)