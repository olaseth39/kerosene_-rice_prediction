from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('app.html')

# to get all the the month

@app.route("/month_names")
def get_month_names():
    response = jsonify({
        "months": util.get_month_names()
    })

    # allow request from any origin of flask endpoint
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route('/predict_kero_price', methods=['post'])
def predict_kero_price():
    # create a form
    year = int(request.form['year'])
    month = request.form['month']

    response = jsonify({
        'estimated_price': util.get_estimated_price(month, year)
    })

    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction")
    util.get_load_saved_artifacts()   # from util.py
    app.run(debug=True)
