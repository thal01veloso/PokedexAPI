from flask import Flask, render_template
from flask.globals import request
import requests
import json
from model.pokemon import Pokemon

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/buscar", methods=['GET',"POST"])
def buscar():
    pokemon = Pokemon(request.form['nome'].lower(),"")
    try:
        res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.nome}").text
        res = json.loads(res)['sprites']
        res = res['front_default']
        pokemon.foto=res
    except:
        return "Nome incorreto"
    return render_template("index.html", foto=pokemon.foto, nome=pokemon.nome.upper())

app.run(debug=True)

