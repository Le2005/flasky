# Semana 04 — Templates (Flask + PythonAnywhere)

Projeto preparado para a branch:

`Semana-04.-Templates`

## Estrutura

```text
flasky/
├── hello.py
├── requirements.txt
├── static/
│   └── css/
│       └── style.css
└── templates/
    ├── base.html
    ├── index.html
    ├── identificacao.html
    ├── contextorequisicao.html
    └── 404.html
```

## Antes de enviar

Edite `hello.py` e substitua:

- `SEU NOME`
- `SEU RA / MATRÍCULA`
- `SEU CURSO`

## Teste local

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
python hello.py
```

Acesse `http://127.0.0.1:5000`.

## Git

```bash
git clone https://github.com/Le2005/flasky.git
cd flasky
git fetch origin
git switch Semana-04.-Templates

# copie os arquivos deste pacote para a pasta do repositório

git add .
git commit -m "Semana 04 - templates Flask e Flask-Moment"
git push origin Semana-04.-Templates
```

## PythonAnywhere

No Bash do PythonAnywhere:

```bash
cd ~
git clone -b Semana-04.-Templates https://github.com/Le2005/flasky.git
cd flasky

mkvirtualenv --python=/usr/bin/python3.13 flasky-venv
pip install -r requirements.txt
```

Se o repositório já estiver clonado:

```bash
cd ~/flasky
git fetch origin
git switch Semana-04.-Templates
git pull origin Semana-04.-Templates
workon flasky-venv
pip install -r requirements.txt
```

Na aba **Web**:

1. Crie/edite o Web App usando **Manual Configuration**.
2. Use a mesma versão do Python escolhida para a virtualenv.
3. Em **Virtualenv**, informe `flasky-venv`.
4. No arquivo WSGI use:

```python
import sys

path = '/home/SEU_USUARIO/flasky'
if path not in sys.path:
    sys.path.insert(0, path)

from hello import app as application
```

5. Troque `SEU_USUARIO` pelo seu usuário do PythonAnywhere.
6. Clique em **Reload**.

Para atualizar depois de novos commits:

```bash
cd ~/flasky
git pull origin Semana-04.-Templates
workon flasky-venv
pip install -r requirements.txt
```

Depois clique em **Reload** na aba Web.
