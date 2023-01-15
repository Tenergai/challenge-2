import sys
from flask import Flask, request, jsonify

sys.path.append('.')
from Forecast import Forecast

app = Flask(__name__)
forecast = Forecast()

@app.route('/', methods=['GET'])
def home():
    return jsonify({'hello':'helloooo world'})

@app.route('/train_svm', methods=['GET'])
def train_svm():
    return jsonify({'score':str(forecast.train_svm())})

@app.route('/train_rf', methods=['GET'])
def train_rf():
    return jsonify({'score':str(forecast.train_rf())})

@app.route('/train_dt', methods=['GET'])
def train_dt():
    return jsonify({'score':str(forecast.train_dt())})

@app.route('/predict', methods=['POST'])
def predict():
    request_json = request.get_json()
    data = request_json['day']
    prediction = forecast.predict(data)
    return jsonify({'result':prediction})

if __name__ == '__main__':
    app.run(port=5002)