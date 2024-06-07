from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DataEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Define your database fields here

