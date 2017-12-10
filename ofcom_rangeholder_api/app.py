from flask import Flask, jsonify
from flask_cors import CORS, cross_origin


class FlaskWithDataStore(Flask):
    datastore = None

app = FlaskWithDataStore(__name__)
CORS(app)


@app.route('/')
def index():
    return 'Hello, world'


@app.route('/favicon.ico')
def favicon():
    return ''


@app.route('/<number>')
@cross_origin()
def number(number):
    number_range = app.datastore.find(number)
    if number_range:
        return jsonify(dict(number_range))
    else:
        return ('', 404)


def build_with_datastore(datastore):
    app.datastore = datastore
    return app
