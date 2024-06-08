import json
import requests


class Consulta():
    __URL = "https://receitaws.com.br/v1/cnpj/"
    
    def busca(self, cnpj):
        try: 
            int(cnpj)
            if len(cnpj)==14:
                my_request = (self.__URL + cnpj)
                values = requests.request("GET", my_request)
                vl = values.json()
                lista = []
                lista = vl["nome"], vl["uf"], vl["municipio"], vl["logradouro"], vl["numero"], vl["complemento"], vl["cep"], vl["telefone"], vl["email"], vl["situacao"], vl["data_situacao"], vl["abertura"], vl["natureza_juridica"], vl["fantasia"], vl["cnpj"], vl["ultima_atualizacao"], vl["status"], vl["tipo"], vl["efr"], vl["motivo_situacao"], vl["situacao_especial"], vl["data_situacao_especial"], vl["capital_social"]
                return lista
            else:
                return None
            
        except:
            return None

"""

nome = 0 - ok ,
logradouro = 3,
situacao = 9 - ok,
email = 8,
capital_social = 22
abertura = 11,
cnpj = 14,

fantasia = 13,
uf = 1,
municipio = 2,
numero = 4,
complemento = 5,
cep = 6,
telefone = 7,
data_situacao = 10,
natureza_juridica = 12,
ultima_atualizacao = 15,
status = 16,
tipo = 17,
efr = 18,
motivo_situacao = 19,
situacao_especial = 20,
data_situacao_especial = 21,


objeto = Consulta()
dados = objeto.busca("61442737000159")

print(dados)
"""