from flask import Blueprint, jsonify
from .utils.validadorCNPJ import ValidarCnpj as vld

validarCNPJ = Blueprint("validarCNPJ", __name__)

__URL_VALIDAR = 'http://localhost:5000/validCNPJ/'

@validarCNPJ.route('/validCNPJ/<id>', methods=["GET", "POST"])
def validar(id):

    result = []
    
    data = {
        "valid": vld(id).cnValidar()
    }
    result.append(data)
    return jsonify(result)

def getURLValidar(value : str) -> str:
    return __URL_VALIDAR + value