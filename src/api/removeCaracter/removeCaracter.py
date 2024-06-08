from flask import Blueprint, jsonify
from .utils.Remove_Caracter_especial import Dados

remove = Blueprint("remove", __name__)

@remove.route('/remove/<id>', methods=["GET"])
def removeCaracter(id):
    dados = Dados(id)
    dados.removeCaracterEspecial()
    dados.removeLetraEspecial()
    dados.removeLetrasAlfabeto()

    result = []
    data = {
        "str": dados.getDados()
    }
    
    result.append(data)

    return jsonify(result)