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
    contactos = 
