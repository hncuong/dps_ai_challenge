#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
from inference import AccidentsInferer

# Model filename
MODEL_FILE = 'arma_model_2020_12_p6_q24.pickle'
inferer = AccidentsInferer(model_file=MODEL_FILE)

app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return jsonify({'name': 'alice',
                       'email': 'alice@outlook.com'})

@app.route('/', methods=['POST'])
def update_record():
    data = json.loads(request.data)
    # Validity check
    if "year" not in data or "month" not in data:
        return jsonify({'err': "invalid request. Request must contains year and month from 1-2021."})
    
    # Load data
    try:
        year = int(data["year"])
        month = int(data["month"])

        # Load model
        pred_val = inferer.predict(year=year, month=month)
        return jsonify({'prediction': pred_val})
    except:
        return jsonify({'err': "invalid request. Request must contains year and month from 1-2021."})

if __name__ == "__main__":
    app.run(debug=True)