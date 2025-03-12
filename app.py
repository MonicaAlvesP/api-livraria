from flask import Flask  # Importa a classe Flask do módulo flask
from dotenv import load_dotenv  # Importa a função load_dotenv do módulo dotenv
import os  # Importa o módulo os para interagir com variáveis de ambiente

load_dotenv()  # Carrega variáveis de ambiente do arquivo .env

app = Flask(__name__)  # Cria uma instância da aplicação Flask


@app.route('/')  # Define a rota para a URL raiz
def hello_world():
    # Retorna uma mensagem para a URL raiz
    return '<h1>Pagina home</h1>'


@app.route('/blog')  # Define a rota para a URL /blog
def blog():
    # Retorna uma mensagem para a URL /blog
    return '<h1>Pagina blog</h1>'


if __name__ == '__main__':  # Verifica se o script está sendo executado diretamente
    # Obtém o valor da variável de ambiente DEBUG_MODE
    debug_mode = os.getenv('DEBUG_MODE')
    # Executa a aplicação Flask com o modo de depuração definido pela variável de ambiente
    app.run(debug=debug_mode)
