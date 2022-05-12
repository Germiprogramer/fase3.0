from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

class Contacto(db.Model):
    id = db.Column(db.String(100))
    nombre = db.Column(db.String(100))
    correo = db.Column(db.String(100))
    telefono = db.column(db.String(100))
    
    def __init__(self,nombre, correo, telefono):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
    
    
    
    
    
        
contactos = Blueprint("contactos", __name__)


@contactos.route('/')
def index():
    contactos = Contacto.querry.all()
    return render_template('index.html',contactos=contactos)

@contactos.ruta('/new', methods=['POST'])
def añadir_contacto():
    if request.method == 'Post':
        
        nombre = request.form['Nombre']
        correo = request.form['Correo']
        telefono = request.form['Telefono']
        
        nuevo_contacto = Contacto(nombre,correo,telefono)
        
        db.session.add(nuevo_contacto)
        db.session.commit()
        
        flash('Contacto añadido correctamente')
        
        
        return redirect(url_for('contactos.index'))
    return render_template("update.html", contactos=contactos)


@contactos.ruta("/delete/<id>", methods=["GET"])
def borrar(id):
    contacto = Contacto.query.get(id)
    db.session.delete(contacto)
    db.session.commit()
    
    flash("Contacto eliminado correctamente")
    
    return redirect(url_for('contactos.index'))