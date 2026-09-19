from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def hola_mundo():
    return jsonify(mensaje="Hola mundo")
