from flask import Blueprint, render_template
from
contacts = Blueprint ("contact", __name__)

@contacts.route("/")
def home():
  return render_template("index.html")

@contacts.route("/new" , methods=["POST"])
def add_contacto():
  print(request.form["Nombre"])
  print(request.form["Apellidos"])
  print(request.form["Correo electrónico"])
  print(request.form["Contraseña"])
  print(request.form["Teléfono"])
  return "saving a contact"

@contacts.route("/update")
def update():
  return "update a contact"


@contact.route("/delete")
def delete():
  return "delete a contact"

@contacts.route("/about")
def about():
  return render_template("index.html")
  