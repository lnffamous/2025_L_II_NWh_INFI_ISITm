from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED
from flask import request

moje_imie = "Dawid"
msg = "Hello World!"


@app.route('/')
def index():
    output = request.args.get('output', '').lower()
    return get_formatted(msg, moje_imie, output)


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)
