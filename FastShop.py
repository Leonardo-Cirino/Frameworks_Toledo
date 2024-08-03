from flask import Flask, make_response
from markupsafe import escape
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/cadastros/user")
def cad_usuarios():
    return render_template("cadastro_user.html", titulocaduser="Cadastrar Usuários")
@app.route("/cadastros/cad_user", methods=['POST'])
def cad_user():
    return request.form 

@app.route("/cadastros/anuncio")
def cad_anuncios():
    return render_template("cadastro_anuncio.html", titulocadanuncio="Cadastrar Anuncios")
@app.route("/cadastros/cad_anu", methods=['POST'])
def cad_anu():
    return request.form




@app.route("/Relat")
def relat_compra():
    return render_template("relatorios.html")



@app.route("/anuncios/fav")
def anuncios_fav():
    return render_template("anuncios_fav.html", titulofav="Anuncios Favoritos")


@app.route("/anuncios/duvidas")
def anuncios_duv():
    return render_template("anuncios_duv.html")

@app.route("/anuncios/categ")
def anuncios_categ():
    return render_template("anuncios_cat.html", titulocateg="Categorias dos Anuncios")