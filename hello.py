from datetime import datetime, timezone

from flask import Flask, render_template, request
from flask_moment import Moment

app = Flask(__name__)
moment = Moment(app)


@app.route("/")
def index():
    return render_template(
        "index.html",
        current_time=datetime.now(timezone.utc),
    )


@app.route("/identificacao")
def identificacao():
    aluno = {
        "nome": "Leandro Kauã",
        "ra": "PT3037649",
        "instituicao": "IFSP",
    }
    return render_template("identificacao.html", aluno=aluno)


@app.route("/user/<name>")
def user(name):
    aluno = {
        "nome": name,
        "ra": "PT3037649",
        "instituicao": "IFSP",
    }
    return render_template("identificacao.html", aluno=aluno)


@app.route("/contextorequisicao")
@app.route("/contexto-requisicao")
def contexto_requisicao():
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
    app.run(debug=True)
