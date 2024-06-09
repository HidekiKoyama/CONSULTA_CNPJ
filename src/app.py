from flask import Flask, redirect, url_for
from api.removeCaracter.removeCaracter import remove
from api.validCNPJ.validCNPJ import validarCNPJ
from modules import *

app = Flask(__name__, template_folder='templates',static_folder='static')

app.register_blueprint(consultaCNPJ)
app.register_blueprint(remove)
app.register_blueprint(validarCNPJ)


@app.route('/')
def redirecting():

    return redirect(url_for('cnpj.consultarCnpj'))

if __name__ == "__main__":
    app.run(debug=True)