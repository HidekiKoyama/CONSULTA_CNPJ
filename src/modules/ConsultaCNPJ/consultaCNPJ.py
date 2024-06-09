from flask import Blueprint, render_template, request
from utils.consulta_api import Consulta
from api import getURLValidar, getURLRemove

consultaCNPJ = Blueprint('cnpj', __name__, static_folder='static',
                    template_folder='templates', url_prefix="/ConsultaCNPJ")


@consultaCNPJ.route('/consultarCnpj', methods=["POST", "GET"])
def consultarCnpj():
    if request.method == "POST":
        buscar = Consulta()
        cnpj = str(request.form.get("cnpj-busca"))
        
        print('sem remover: ',cnpj)
        
        dicio = []

        data = {
            'str': cnpj
        }
    
        dicio.append(data)

        cnpj = getURLRemove(dicio)
        
        print('removendo: ',cnpj)

        
        if (cnpj != None and cnpj):
            dados = buscar.busca(cnpj)
            return render_template('index.html', dados=dados)
        else:
            return render_template('index.html', dados="")

    else:
        return render_template('index.html', dados="")
    