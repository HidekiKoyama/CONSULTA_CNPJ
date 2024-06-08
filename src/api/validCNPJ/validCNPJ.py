from flask import Blueprint, jsonify
from .utils.validadorCNPJ import ValidarCnpj as vld

validarCNPJ = Blueprint("validarCNPJ", __name__)

@validarCNPJ.route('/validCNPJ/<id>', methods=["GET", "POST"])
def validar(id):

    result = []
    
    data = {
        "valid": vld(id).cnValidar()
    }
    result.append(data)
    return jsonify(result)

