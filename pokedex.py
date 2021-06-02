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
    pokemon = Pokemon(request.form['nome'].lower(),"","","")
    try:
        res = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.nome}").text)
        result = res['sprites']
        result = result['front_default']
        pokemon.foto=result
        if len(res['types'])==2:
            pokemon.type1=res['types'][0]['type']['name']
            pokemon.type2=res['types'][1]['type']['name']
        else:
            pokemon.type1=res['types'][0]['type']['name']
    except:
        return "Nome incorreto"
    return render_template("index.html",
    foto=pokemon.foto,
    nome=pokemon.nome.upper(),
    tipo1=pokemon.type1.upper(),
    tipo2=pokemon.type2.upper())

app.run(debug=True)

