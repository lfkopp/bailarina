from os import getenv
from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/movimentacao')
def movimentacao():
    return render_template('movimentacao.html')

@app.route('/referencia')
def referencia():
    return render_template('referencia.html')


if __name__ == "__main__":
    app.run(host=getenv("HOST", "0.0.0.0"), port=getenv("PORT", 5000), debug=str(getenv("DEBUG", 0))==1)
