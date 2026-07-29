from flask import Flask, request, make_response, redirect, abort

app = Flask(__name__)

# 1. Rota raiz (Página inicial)
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# 2. Rota dinâmica (Recebe o nome como parâmetro na URL)
@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>'

# 3. Contexto de requisição (Acessa dados do navegador via objeto 'request')
@app.route('/contextorequisicao')
def contexto_requisicao():
    user_agent = request.headers.get('User-Agent')
    return f'<p>Seu navegador é: <b>{user_agent}</b></p>'

# 4. Código de status diferente (Retorna código HTTP 400 Bad Request)
@app.route('/codigostatusdiferente')
def codigo_status_diferente():
    return '<h1>Bad Request / Requisição Inválida</h1>', 400

# 5. Objeto de resposta (Cria um objeto Response e define um Cookie)
@app.route('/objetoresposta')
def objeto_resposta():
    response = make_response('<h1>Este documento carrega um cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

# 6. Redirecionamento (Redireciona o usuário para outro site)
@app.route('/redirecionamento')
def redirecionamento():
    return redirect('https://www.google.com')

# 7. Abortar (Força um erro de requisição, como o HTTP 404 Not Found)
@app.route('/abortar')
def abortar():
    abort(404)

if __name__ == '__main__':
    app.run(debug=True)
