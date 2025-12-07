from flask import Flask, request

app = Flask(__name__)

moje_imie = "Dawid"
msg = "Hello World!"

SUPPORTED = ["json", "xml", "yaml"]

def get_formatted(msg, name, output):
    return f"{msg} {name} ({output})"

@app.route('/')
def index():
    output = request.args.get('output')
    return get_formatted(msg, moje_imie, output.lower())

@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)

