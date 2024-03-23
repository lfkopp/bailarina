
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Site da Renta'


if __name__ == "__main__":
    app.run(host="localhost", port=81)
