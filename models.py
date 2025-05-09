from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    date = db.Column(db.String(50))
    location = db.Column(db.String(100))

# À lancer une fois pour créer la base
if __name__ == "__main__":
    db.create_all()
    print("Base de données créée avec succès !")
