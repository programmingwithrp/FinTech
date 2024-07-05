from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/payment', methods=['POST'])
def payment():
    phone_num = request.json.get('phone_num')
    otp = request.json.get('otp')
    password = request.json.get('password')

    # Dummy response for payment details
    data = {
        "phone_num": phone_num,
        "otp": otp,
        "password": password,
        "payment_details": {
            "status": "success",
            "amount": "100.00",
            "currency": "USD"
        }
    }
    return jsonify(data)


@app.route('/dummy_weather', methods=['GET'])
def dummy_weather():
    city = request.args.get('city', 'New York')
    data = {
        "city": city,
        "temperature": "22°C",
        "description": "Clear sky"
    }
    return jsonify(data)


@app.route('/dummy_currency', methods=['GET'])
def dummy_currency():
    data = {
        "USD": 1.0,
        "EUR": 0.85,
        "JPY": 110.0
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(port=5001)
