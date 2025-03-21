# 📚 API livraria

Desenvolvido como parte do curso de Fullstack da Vai na Web, este projeto demonstra a implementação de uma API REST usando Flask com integração a banco de dados SQLite.

## 🌟 Funcionalidades

- **Página Inicial**: Apresenta uma interface de boas-vindas com um poema sobre a jornada de aprendizado em programação
- **Cadastro de Livros**: Endpoint para cadastrar novos livros para doação
- **Listagem de Livros**: Endpoint para visualizar todos os livros cadastrados no sistema

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

### POST /doar

Cadastra um novo livro para doação

```json
{
  "titulo": "Nome do Livro",
  "categoria": "Categoria do Livro",
  "autor": "Nome do Autor",
  "imagem_url": "URL da imagem do livro",
  "sinopse": "Pequeno resumo do livro"
}
```

### GET /livros-doados

Retorna a lista de todos os livros cadastrados

<div align="left">
  Feito com 💜 por <a href="https://github.com/MonicaAlvesP?tab=repositories">MA</a>.
</div>
