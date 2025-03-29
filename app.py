from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from flask_cors import CORS
import os
import sqlite3

load_dotenv()

app = Flask(__name__, template_folder='template')

CORS(app)


def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute(
            """
    CREATE TABLE IF NOT EXISTS LIVROS(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    ano_lancamento INTEGER NOT NULL,
    categoria TEXT NOT NULL,
    autor TEXT NOT NULL,
    image_url TEXT NOT NULL,
    sinopse TEXT NOT NULL
    )
    """
        )


init_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/doar", methods=["POST"])
def doar():
    dados = request.get_json()

    titulo = dados.get("titulo")
    ano_lancamento = dados.get("ano_lancamento")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    image_url = dados.get("imagem_url")
    sinopse = dados.get("sinopse")

    if not titulo or not categoria or not autor or not image_url or not sinopse:
        return jsonify({"error": "Todos os campos são obrigatórios"}), 400

    with sqlite3.connect('database.db') as conn:
        conn.execute(f"""
    INSERT INTO LIVROS(titulo, ano_lancamento, categoria, autor, image_url, sinopse)
    VALUES (?, ?, ?, ?, ?, ?)
  """, (titulo, ano_lancamento, categoria, autor, image_url, sinopse))
        return jsonify({"message": "Livro cadastrado com sucesso",
                        "livro": {
                            "titulo": titulo,
                            "categoria": categoria,
                            "autor": autor,
                        }}), 201
        conn.commit()

        return jsonify({"message": "Livro cadastrado com sucesso"}, 201)


@app.route("/livros-doados", methods=["GET"])
def livros_doados():
    with sqlite3.connect('database.db') as conn:
        livros = conn.execute("SELECT * FROM LIVROS").fetchall()

        livros_formatados = []

        for livro in livros:
            dicionario_livros = {
                "id": livro[0],
                "titulo": livro[1],
                "ano_lancamento": livro[2],
                "categoria": livro[3],
                "autor": livro[4],
                "image_url": livro[5],
                "sinopse": livro[6]
            }
            livros_formatados.append(dicionario_livros)
    return jsonify(livros_formatados), 200


@app.route("/livros-doados/<int:id>", methods=["GET"])
def livro_doados(id):
    with sqlite3.connect('database.db') as conn:
        livro = conn.execute(
            "SELECT * FROM LIVROS WHERE id = ?", (id,)).fetchone()

        if livro is None:
            return jsonify({"error": "Livro não encontrado"}), 404

        dicionario_livro = {
            "id": livro[0],
            "titulo": livro[1],
            "ano_lancamento": livro[2],
            "categoria": livro[3],
            "autor": livro[4],
            "image_url": livro[5],
            "sinopse": livro[6]
        }

    return jsonify(dicionario_livro), 200


if __name__ == '__main__':
    debug_mode = os.getenv('DEBUG_MODE')
    app.run(debug=debug_mode)
