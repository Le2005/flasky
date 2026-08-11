from datetime import datetime, timezone

from flask import Flask, render_template, request
from flask_moment import Moment

app = Flask(__name__)
moment = Moment(app)


@app.route("/")
def index():
    # Flask-Moment recebe UTC e converte para o horário local do navegador.
    return render_template(
        "index.html",
        current_time=datetime.now(timezone.utc),
    )


@app.route("/identificacao")
def identificacao():
    # Troque os valores abaixo pelos seus dados.
    aluno = {
        "nome": "SEU NOME",
        "ra": "SEU RA / MATRÍCULA",
        "curso": "SEU CURSO",
    }
    return render_template("identificacao.html", aluno=aluno)


# Mantém compatibilidade com a rota dinâmica usada nas semanas anteriores.
@app.route("/user/<name>")
def user(name):
    aluno = {
        "nome": name,
        "ra": "SEU RA / MATRÍCULA",
        "curso": "SEU CURSO",
    }
    return render_template("identificacao.html", aluno=aluno)


@app.route("/contextorequisicao")
@app.route("/contexto-requisicao")
def contexto_requisicao():
    # Em hospedagens com proxy, X-Forwarded-For pode conter o IP original.
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    dados = {
        "metodo": request.method,
        "url": request.url,
        "host": request.host,
        "user_agent": request.headers.get("User-Agent", "Não informado"),
        "ip": ip or "Não informado",
        "idioma": request.headers.get("Accept-Language", "Não informado"),
    }
    return render_template("contextorequisicao.html", dados=dados)


@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    # No PythonAnywhere este bloco não é executado pelo WSGI.
    # Ele serve somente para testes locais.
    app.run(debug=True)
