# 📚 API Livraria

Desenvolvido como parte do curso de Fullstack da Vai na Web, este projeto demonstra a implementação de uma API REST usando Flask com integração a banco de dados SQLite. Com a ajuda do meu professor [João Pedro Belo](https://www.linkedin.com/in/jo%C3%A3o-pedro-belo/), consegui desenvolver e aprimorar as funcionalidades desta aplicação.

## 🌟 Funcionalidades

- **Página Inicial**: Apresenta uma interface de boas-vindas com um poema sobre a jornada de aprendizado em programação
- **Cadastro de Livros**: Endpoint para cadastrar novos livros para doação
- **Listagem de Livros**: Endpoint para visualizar todos os livros cadastrados no sistema
- **Detalhes do Livro**: Endpoint para obter informações detalhadas de um livro específico, incluindo título, autor, categoria, ano de lançamento, sinopse e URL da imagem.

## 🗄️ Estrutura do Banco de Dados

O projeto utiliza SQLite para armazenar informações sobre os livros. Cada livro possui:

- ID (chave primária)
- Título
- Ano de Lançamento
- Categoria
- Autor
- URL da imagem do livro
- Sinopse

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação principal
- **Flask**: Framework web para desenvolvimento da API
- **SQLite**: Banco de dados local para armazenamento
- **python-dotenv**: Para gerenciamento de variáveis de ambiente

## 🚀 Como Executar

1. Clone o repositório
```
git clone https://github.com/MonicaAlvesP/api-livraria.git
```
2. Crie um ambiente virtual:

```
python -m venv venv
```

3. Ative o ambiente virtual:

- No Windows:
  ```
  venv\Scripts\activate
  ```
- No macOS/Linux:
  ```
  source venv/bin/activate
  ```

4. Instale as dependências:

```
pip install -r requirements.txt
```

5. Crie um arquivo .env na raiz do projeto com:

```
DEBUG_MODE=True
```

6. Execute a aplicação:

```
python app.py
```

## 🔗 Endpoints da API

### GET /

Retorna a página inicial em HTML

### GET /livros-doados
Retorna a lista de todos os livros cadastrados no sistema.

**Respostas:**
- 200 OK: Retorna a lista de livros
- 500 Internal Server Error: Quando ocorre algum problema no servidor

### GET /livros-doados/<id>

Retorna os detalhes de um livro específico pelo seu ID

**Respostas:**
- 200 OK: Retorna os dados do livro solicitado
- 404 Not Found: Quando o livro com o ID especificado não existe

### POST /doar

Cadastra um novo livro para doação

```json
{
  "titulo": "Nome do Livro",
  "ano_lancamento": "Ano em que o livro foi lançado",
  "categoria": "Categoria do Livro",
  "autor": "Nome do Autor",
  "image_url": "URL da imagem do livro",
  "sinopse": "Pequeno resumo do livro"
}
```
**Respostas:**
- 201 Created: Livro cadastrado com sucesso
- 400 Bad Request: Erro quando campos obrigatórios não são fornecidos

<div align="left">
  Feito com 💜 por <a href="https://github.com/MonicaAlvesP?tab=repositories">MA</a>.
</div>
