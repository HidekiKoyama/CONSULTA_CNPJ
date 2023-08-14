from flask import Blueprint, render_template, request
from src.app.utils.consulta_api import Consulta

app_main = Blueprint("app_main", __name__, static_folder="./view/", template_folder="./view/")

@app_main.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        b = Consulta()
        cnpj = str(request.form.get("cnpj-busca"))
        dados = b.busca(cnpj)
        return render_template('index.html', dados=dados)
    else:
        return render_template('index.html', dados="")