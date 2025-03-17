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
    categoria TEXT NOT NULL,
    autor TEXT NOT NULL,
    imagem_url TEXT NOT NULL,
    condicao TEXT NOT NULL
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
  categoria = dados.get("categoria")
  autor = dados.get("autor")
  image_url = dados.get("imagem_url")
  condicao = dados.get("condicao")

  if not titulo or not categoria or not autor or not image_url or not condicao:
    return jsonify({"error": "Todos os campos são obrigatórios"}), 400

  with sqlite3.connect('database.db') as conn:
    conn.execute("""
    INSERT INTO LIVROS(titulo, categoria, autor, imagem_url, condicao)
    VALUES (?, ?, ?, ?, ?)
  """, (titulo, categoria, autor, image_url, condicao))
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
    cursor = conn.execute("""
    SELECT * FROM LIVROS
  """)
    livros = cursor.fetchall()
    return jsonify(livros)

if __name__ == '__main__':
  debug_mode = os.getenv('DEBUG_MODE')
  app.run(debug=debug_mode)
