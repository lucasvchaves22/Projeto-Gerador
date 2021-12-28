import string
from flask import Flask, render_template, request, redirect
from random import random, choice

from werkzeug.utils import escape

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/criptografar", methods=["POST"])
def criptografar():
    senha = request.form.get('senha')
    valores = '!@#$%&_,:;'
    n_senha = ""
    espaco = " _"
    bot = ''.join(senha)
    bot1 = '12345678'
    bot2 = '87654321'
    bot3 = '1234'
    bot4 = '123'
    bot5 = '123456'

    if len(senha) >= 8:
        for letra in senha:
            if letra in "Aa": n_senha = n_senha + '@' # + choice(valores)
            elif letra in "Ee": n_senha = n_senha + '3'
            elif letra in "Ii": n_senha = n_senha + '1'
            elif letra in "Oo": n_senha = n_senha + '0'
            elif letra in "Uu": n_senha = n_senha + '#'
            else: n_senha = n_senha + letra

    else: return render_template("erro.html")    
    
    if bot == bot1 or bot == bot2 or bot3 in bot or bot4 in bot or bot5 in bot:
        return render_template("error.html")
    else: n_senha += espaco

    n_senha += choice(string.ascii_uppercase)

    return render_template("senha.html", nova=n_senha)

@app.route("/gerar", methods=["POST"])
def gerar():
    valores = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
    tamanho = 8
    senha = ''
    espaco =" _"

    for i in range(tamanho):
        senha += choice(valores)

    senha += espaco

    return render_template("senhagerada.html", nova=senha)

app.run(debug=True)