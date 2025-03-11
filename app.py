from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Olá, esta é uma pagina renderizada pelo Flask!'


@app.route('/blog')
def blog():
    return 'Esta é a página inicial do blog!'


if __name__ == '__main__':
    debug_mode = os.getenv('DEBUG_MODE')
    app.run(debug=debug_mode)
