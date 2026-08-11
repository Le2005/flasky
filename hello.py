from datetime import datetime, timezone

from flask import Flask, redirect, render_template, request, url_for
from flask_moment import Moment

app = Flask(__name__)
moment = Moment(app)

# Dados do aluno usados nos links da aplicação.
NOME_ALUNO = "Leandro Kauã"
PRONTUARIO_ALUNO = "PT3037649"
INSTITUICAO_ALUNO = "IFSP"


@app.route("/")
def index():
    return render_template(
        "index.html",
        current_time=datetime.now(timezone.utc),
    )


@app.route("/identificacao")
def identificacao():
    # Mantém a rota simples, mas redireciona para o mesmo formato usado
    # na aplicação de referência do professor.
    return redirect(
        url_for(
            "user",
            name=NOME_ALUNO,
            prontuario=PRONTUARIO_ALUNO,
            instituicao=INSTITUICAO_ALUNO,
        )
    )


@app.route("/user/<name>/<prontuario>/<instituicao>")
def user(name, prontuario, instituicao):
    return render_template(
        "identificacao.html",
        nome=name,
        prontuario=prontuario,
        instituicao=instituicao,
    )


# Compatibilidade com a rota utilizada em etapas anteriores.
@app.route("/user/<name>")
def user_legado(name):
    return redirect(
        url_for(
            "user",
            name=name,
            prontuario=PRONTUARIO_ALUNO,
            instituicao=INSTITUICAO_ALUNO,
        )
    )


@app.route("/contextorequisicao")
@app.route("/contexto-requisicao")
def contexto_requisicao_sem_nome():
    return redirect(url_for("contexto_requisicao", name=NOME_ALUNO))


@app.route("/contextorequisicao/<name>")
def contexto_requisicao(name):
    return render_template(
        "contextorequisicao.html",
        nome=name,
        navegador=request.headers.get("User-Agent", "Não informado"),
        ip=request.remote_addr or "Não informado",
        host=request.host,
    )


@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
