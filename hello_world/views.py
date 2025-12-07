from flask import Flask, request

app = Flask(__name__)

moje_imie = "Dawid"
msg = "Hello World!"


def get_formatted(msg, name, output_format):
    if output_format == "upper":
        return f"{msg.upper()} {name.upper()}"
    elif output_format == "lower":
        return f"{msg.lower()} {name.lower()}"
    else:
        return f"{msg} {name}"


SUPPORTED = ["upper", "lower"]


@app.route('/')
def index():
    output = request.args.get('output', 'upper')
    return get_formatted(msg, moje_imie, output.lower())


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)
