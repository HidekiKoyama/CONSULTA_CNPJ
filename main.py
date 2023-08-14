from flask import Flask
from src.app.app_main import app_main

app = Flask(__name__)

app.register_blueprint(app_main)

if __name__ == "__main__":
    app.run(debug=True)