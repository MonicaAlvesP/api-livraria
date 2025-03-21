from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
import sqlite3

load_dotenv()

app = Flask(__name__, template_folder='template')


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
        cursor = conn.cursor()
        cursor.execute("""
    SELECT * FROM LIVROS
  """)
        livros = cursor.fetchall()
        return jsonify(livros)


if __name__ == '__main__':
    debug_mode = os.getenv('DEBUG_MODE')
    app.run(debug=debug_mode)
