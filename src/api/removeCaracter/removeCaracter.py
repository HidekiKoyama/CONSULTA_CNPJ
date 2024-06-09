from flask import Blueprint, jsonify, request
from .utils.Remove_Caracter_especial import Dados
import requests, json

remove = Blueprint("remove", __name__)

__URL_REMOVE = 'http://localhost:5000/remove/'

@remove.route('/remove/', methods=["GET"])
def removeCaracter():
    id = request.args.get('str', '')

    print('eu to recebendo isso no id: ', id)

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


def getURLRemove(value : dict) -> str:

    response = requests.request("GET", url=__URL_REMOVE, params={'str': json.dumps(value)}).text

    response = json.loads(response)[0]['str']

    return response


