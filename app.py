from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from flask_cors import CORS
import os
import psycopg2
import psycopg2.extras

load_dotenv()

app = Flask(__name__, template_folder='template')

CORS(app)


def get_conn():
    return psycopg2.connect(os.getenv('DATABASE_URL'))


def init_db():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
    CREATE TABLE IF NOT EXISTS LIVROS(
    id SERIAL PRIMARY KEY,
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
    image_url = dados.get("imagem_url") or dados.get("image_url")
    sinopse = dados.get("sinopse")

    if not titulo or not categoria or not autor or not image_url or not sinopse:
        return jsonify({"error": "Todos os campos são obrigatórios"}), 400

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
    INSERT INTO LIVROS(titulo, ano_lancamento, categoria, autor, image_url, sinopse)
    VALUES (%s, %s, %s, %s, %s, %s)
  """, (titulo, ano_lancamento, categoria, autor, image_url, sinopse))

    return jsonify({"message": "Livro cadastrado com sucesso",
                    "livro": {
                        "titulo": titulo,
                        "categoria": categoria,
                        "autor": autor,
                    }}), 201


@app.route("/livros-doados", methods=["GET"])
def livros_doados():
    with get_conn() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("SELECT * FROM LIVROS")
            livros = cur.fetchall()

    return jsonify([dict(livro) for livro in livros]), 200


@app.route("/livros-doados/<int:id>", methods=["GET"])
def livro_doados(id):
    with get_conn() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("SELECT * FROM LIVROS WHERE id = %s", (id,))
            livro = cur.fetchone()

    if livro is None:
        return jsonify({"error": "Livro não encontrado"}), 404

    return jsonify(dict(livro)), 200


@app.route("/pesquisa", methods=["GET"])
def pesquisa():
    termo = request.args.get("q", "")
    if not termo:
        return jsonify([]), 200

    termo_like = f"%{termo}%"
    with get_conn() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                """
                SELECT * FROM LIVROS 
                WHERE titulo ILIKE %s OR autor ILIKE %s OR categoria ILIKE %s
                """,
                (termo_like, termo_like, termo_like)
            )
            livros = cur.fetchall()

    return jsonify([dict(livro) for livro in livros]), 200


if __name__ == '__main__':
    debug_mode = os.getenv('DEBUG_MODE')
    app.run(debug=debug_mode)
