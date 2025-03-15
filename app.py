from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import sqlite3

load_dotenv()

app = Flask(__name__)


def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute(
            """
      CREATE TABLE IF NOT EXISTS LIVROS(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      titulo TEXT NOT NULL,
      categoria TEXT NOT NULL,
      autor TEXT NOT NULL,
      imagem_url TEXT NOT NULL,
      condicao TEXT NOT NULL
      )
    """
        )


init_db()


@app.route("/doar", methods=["POST"])
def doar():
    dados = request.get_json()

    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    imagem_url = dados.get("imagem_url")
    condicao = dados.get("condicao")

    with sqlite3.connect('database.db') as conn:
        conn.execute(f"""
                   
        INSERT INTO LIVROS(titulo, categoria, autor, imagem_url, condicao)
        VALUES ("{titulo}", "{categoria}", "{autor}", "{imagem_url}", "{condicao}")
                   """)
        return jsonify({"message": "Livro cadastrado com sucesso"}), 201


if __name__ == '__main__':
    debug_mode = os.getenv('DEBUG_MODE')
    app.run(debug=debug_mode)
