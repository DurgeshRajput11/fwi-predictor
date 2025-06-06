from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

application = Flask(__name__)
app = application

ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['POST'])
def predict_datapoint():
    data = request.json  # AJAX will send JSON
    Temperature = float(data.get('Temperature'))
    RH = float(data.get('RH'))
    Ws = float(data.get('Ws'))
    Rain = float(data.get('Rain'))
    FFMC = float(data.get('FFMC'))
    DMC = float(data.get('DMC'))
    ISI = float(data.get('ISI'))
    Classes = float(data.get('Classes'))
    Region = float(data.get('Region'))

    new_data = [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]
    new_data_scaled = standard_scaler.transform(new_data)
    result = ridge_model.predict(new_data_scaled)
    pred = round(result[0], 2)

    return jsonify({'prediction': pred})

if __name__ == "__main__":
    app.run(debug=True)
