import psycopg2
from flask import Flask,redirect,render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField,StringField,SubmitField

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/libros')
def libros():
    #conectar con la BD
    conexion= psycopg2.connect(
        database= "Biblioteca3a",
        user="postgres",
        password="cris20",
        host="localhost",
        port="5432"
    )

    #crear un cursor (objeto para recorrer las tablas)
    cursor= conexion.cursor()
    #ejecutar una consulta en postgres
    cursor.execute('''SELECT*FROM libros_view''')
    #recuperar informacion
    datos= cursor.fetchall()
    #cerrar cursor y conexion de la base de datos
    cursor.close()
    conexion.close()
    return render_template('libros.html', datos=datos)

@app.route('/autores')
def autores():
     #conectar con la BD
    conexion= psycopg2.connect(
        database= "Biblioteca3a",
        user="postgres",
        password="cris20",
        host="localhost",
        port="5432"
    )

    #crear un cursor (objeto para recorrer las tablas)
    cursor= conexion.cursor()
    #ejecutar una consulta en postgres
    cursor.execute('''SELECT*FROM autores_view''')
    #recuperar informacion
    datos= cursor.fetchall()
    #cerrar cursor y conexion de la base de datos
    cursor.close()
    conexion.close()
    return render_template('autores.html', datos=datos)