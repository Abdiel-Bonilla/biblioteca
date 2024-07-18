import psycopg2
from flask import Flask,request,redirect,render_template,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField,StringField,SubmitField
import db

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.errorhandler(404)
def error404(error):
    return render_template('404.html')

@app.route('/libros')
def libros():
    conn= db.conectar()
    #crear un cursor (objeto para recorrer las tablas)
    cursor= conn.cursor()
    #ejecutar una consulta en postgres
    cursor.execute('''SELECT*FROM libros_view ORDER BY id_libro''')
    #recuperar informacion
    datos= cursor.fetchall()
    #cerrar cursor y conexion de la base de datos
    cursor.close()
    db.desconectar(conn)
    return render_template('libros.html', datos=datos)

@app.route('/autores')
def autores():
    #conectar con la BD
    conn= db.conectar()
    #crear un cursor (objeto para recorrer las tablas)
    cursor= conn.cursor()
    #ejecutar una consulta en postgres
    cursor.execute('''SELECT*FROM autores_view ORDER BY id_autor''')
    #recuperar informacion
    datos= cursor.fetchall()
    #cerrar cursor y conexion de la base de datos
    cursor.close()
    db.desconectar(conn)
    return render_template('autores.html', datos=datos)

@app.route('/paises')
def paises():
    #conectar con la BD
    conn= db.conectar()
    #crear un cursor (objeto para recorrer las tablas)
    cursor= conn.cursor()
    #ejecutar una consulta en postgres
    cursor.execute('''SELECT*FROM país ORDER BY id_pais''')
    #recuperar informacion
    datos= cursor.fetchall()
    #cerrar cursor y conexion de la base de datos
    cursor.close()
    db.desconectar(conn)
    return render_template('paises.html', datos=datos)

@app.route('/delete_pais/<int:id_pais>', methods=['POST'])
def delete_pais(id_pais):
    #conectar con la BD
    conn= db.conectar()
    #crear un cursor (objeto para recorrer las tablas)
    cursor= conn.cursor()
    #Borrar el registro con el id_pais seleccionado
    cursor.execute('''DELETE FROM país WHERE id_pais=%s''',
                    (id_pais,))
    conexion.commit()
    cursor.close()
    conexion.close()
    return redirect(url_for('index'))

@app.route('/delete_autor/<int:id_autor>', methods=['POST'])
def delete_autor(id_autor):
    #conectar con la BD
    conn= db.conectar()
    #crear un cursor (objeto para recorrer las tablas)
    cursor= conn.cursor()
    #Borrar el registro con el id_pais seleccionado
    cursor.execute('''DELETE FROM autores_view WHERE id_autor=%s''',
                    (id_autor,))
    conexion.commit()
    cursor.close()
    db.desconectar(conn)
    return redirect(url_for('index'))

@app.route('/delete_libro/<int:id_libro>', methods=['POST'])
def delete_libro(id_autor):
    #conectar con la BD
    conn= db.conectar()
    #crear un cursor (objeto para recorrer las tablas)
    cursor= conn.cursor()
    #Borrar el registro con el id_pais seleccionado
    cursor.execute('''DELETE FROM libros_view WHERE id_libro=%s''',
                    (id_libro,))
    conexion.commit()
    cursor.close()
    db.desconectar(conn)
    return redirect(url_for('index'))































#PAISES
@app.route('/update1_pais/<int:id_pais>', methods=['POST'])
def update1_pais(id_pais):
    #conectar con la BD
    conn= db.conectar()
    #crear un cursor (objeto para recorrer las tablas)
    cursor= conn.cursor()
    #recuperar el registro del id_pais seleccionado
    cursor.execute( '''SELECT*FROM país WHERE id_pais=%s''' ,
                    (id_pais,))
    datos=cursor.fetchall()
    cursor.close()
    db.desconectar(conn)
    return render_template ('editar_pais.html', datos=datos)
@app.route('/update2_pais/<int:id_pais>', methods=['POST'])
def update2_pais(id_pais):
    nombre=request.form['nombre']
    #conectar con la BD
    conn= db.conectar()
    #crear un cursor (objeto para recorrer las tablas)
    cursor= conn.cursor()
    cursor.execute('''UPDATE país SET nombre=%s WHERE id_pais=%s''',(nombre,id_pais,))
    conn.commit()
    cursor.close()
    db.desconectar(conn)
    return redirect(url_for('index'))

#AUTORES
@app.route('/update1_autores/<int:id_autor>', methods=['POST'])
def update1_autores(id_autor):
    #conectar con la BD
    conn= db.conectar()
    #crear un cursor (objeto para recorrer las tablas)
    cursor= conn.cursor()
    #recuperar el registro del id_pais seleccionado
    cursor.execute( '''SELECT*FROM autores_view WHERE id_autor=%s''' ,
                    (id_autor,))
    datos=cursor.fetchall()
    cursor.close()
    db.desconectar(conn)
    return render_template ('editar_autor.html', datos=datos)

@app.route('/update2_autores/<int:id_autor>', methods=['POST'])
def update2_autores(id_autor):
    nombre=request.form['nombre']
    #conectar con la BD
    conn= db.conectar()
    #crear un cursor (objeto para recorrer las tablas)
    cursor= conn.cursor()
    cursor.execute('''UPDATE autores_view SET "Nombre del autor"=%s WHERE id_autor=%s''',(nombre,id_autor,))
    conn.commit()
    cursor.close()
    db.desconectar(conn)
    return redirect(url_for('index'))