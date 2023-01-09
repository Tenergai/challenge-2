import sys
from flask import Flask, request, jsonify

sys.path.append('.')
from Forecast import Forecast

app = Flask(__name__)
forecast = Forecast()

@app.route('/', methods=['GET'])
def home():
    return jsonify({'hello':'helloooo world'})

@app.route('/predict', methods=['POST'])
def predict():
    request_json = request.get_json()
    data = request_json['day']
    prediction = forecast.predict(data)
    return jsonify({'result':prediction})

if __name__ == '__main__':
    app.run(port=5002)