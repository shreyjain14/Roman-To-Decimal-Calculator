from calculator import convert
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', decimal=None)


@app.route('/', methods=['POST'])
def read_form():
    data = request.form.get
    decimal = convert(data('roman'))

    return render_template('index.html', decimal=decimal)


app.run()
