from flask import Flask, request, jsonify, render_template
import json
import pickle
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

# Load model and column data
model = pickle.load(open(os.path.join("artifacts", "banglore_home_prices_model.pickle"), "rb"))
columns = json.load(open(os.path.join("artifacts", "columns.json"), "r"))['data_columns']
locations = columns[3:]  # first 3 columns are sqft, bath, bhk

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_price')
def predict_price_page():
    return render_template('index.html')

@app.route('/get_location_names')
def get_location_names():
    return jsonify({'locations': locations})
@app.route('/compare')
def compare_page():
    return render_template('compare.html')

@app.route('/analyze')
def analyze_page():
    return render_template('analyze.html')


@app.route('/compare_bhk_prices', methods=['POST'])
def compare_bhk_prices():
    data = request.get_json()
    location = data.get('location')

    bhk_prices = []
    for bhk in range(1, 6):  # 1 to 5 BHK
        x = np.zeros(len(columns))
        x[0] = 1000  # assuming fixed sqft for comparison
        x[1] = 2     # fixed bath
        x[2] = bhk
        if location in columns:
            loc_index = columns.index(location)
            x[loc_index] = 1
        price = model.predict([x])[0] * 100000
        bhk_prices.append({'bhk': bhk, 'price': round(price)})

    return jsonify({'data': bhk_prices})


@app.route('/compare_bath_prices', methods=['POST'])
def compare_bath_prices():
    data = request.get_json()
    location = data.get('location')

    bath_prices = []
    for bath in range(1, 6):  # 1 to 5 bathrooms
        x = np.zeros(len(columns))
        x[0] = 1000  # fixed sqft
        x[1] = bath
        x[2] = 2     # fixed bhk
        if location in columns:
            loc_index = columns.index(location)
            x[loc_index] = 1
        price = model.predict([x])[0] * 100000
        bath_prices.append({'bath': bath, 'price': round(price)})

    return jsonify({'data': bath_prices})





@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    data = request.get_json()

    location = data.get('location')
    sqft = float(data.get('sqft', 0))
    bath = int(data.get('bath', 0))
    bhk = int(data.get('bhk', 0))


    # Then your normal code continues...
    x = np.zeros(len(columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if location in columns:
        loc_index = columns.index(location)
        x[loc_index] = 1

    estimated_price = round(model.predict([x])[0] * 100000)
    return jsonify({'estimated_price': estimated_price})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
