from flask import Flask
import random
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello Harry Wang"


@app.route('/hello')
def hello():
    greeting_list = ['Ciao', 'Hei', 'Salut', 'Hola', 'Nihao']
    return random.choice(greeting_list)


if __name__ == '__main__':
    app.run()
