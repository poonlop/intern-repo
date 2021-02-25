import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#test data of fruits
fruits = [
    {'type': 'banana',
    'price': 10,
    'quantity': 5},
    {'type': 'apple',
    'price': 30,
    'quantity': 2},
    {'type': 'coconut',
    'price': 50,
    'quantity': 1}
]

@app.route('/', methods=['get'])
def home():
    return "<h1>fruits online shop</h1><p>delivery 24-hr<p>"

@app.route('/all')
def all():
    return jsonify(fruits)

@app.route('/find')
def find():
    if 'type' in request.args:
        t = request.args['type']
    else:
        return "no type provided"
    result = []
    for fruit in fruits:
        if fruit['type'] == t:
            result.append(fruit)
    return jsonify(result)
app.run()