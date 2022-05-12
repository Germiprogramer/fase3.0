from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@server/db'


app.register_blueprint(contacts)