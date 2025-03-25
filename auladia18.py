from flask import Flask 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {
        "mensagem": "ta quase na hora do almoço",
        "horario":"11:30"
    }