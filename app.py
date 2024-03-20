from flask import Flask
from generate import Generate
app = Flask(__name__)

gen = Generate()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/prime/')
def prime():
    return {"numbers" : gen.is_prime()}

@app.route('/even/')
def even():
    return {"numbers" : gen.is_even()}

@app.route('/fibo/')
def fibo():
    return {"numbers" : gen.is_fibo()}

@app.route('/rand/')
def rand():
    return {"numbers" : gen.is_random()}


if __name__ == '__main__':

    app.run()
