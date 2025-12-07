from flask import Flask, request, jsonify


app = Flask(__name__)


moje_imie = "Dawid"
msg = "Hello World!"


SUPPORTED = ["json", "text"]


def get_formatted(message, name, output):
    if output == "json":
        return jsonify({"imie": name, "msg": message})
    return f"{message} {name}"


@app.route('/')
def index():
    output = request.args.get('output', '').lower()
    return get_formatted(msg, moje_imie, output)


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)
