from flask import Flask
from src.app.app_main import app_main
from src import remove, validarCNPJ

app = Flask(__name__)

app.register_blueprint(app_main)
app.register_blueprint(remove)
app.register_blueprint(validarCNPJ)

if __name__ == "__main__":
    app.run(debug=True)