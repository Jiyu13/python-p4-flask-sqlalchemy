# 1. import SQLALchemy class from Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# 2. connect your application with SQLAlchemy???
db = SQLAlchemy()


# use db object's Model class
class Owner(db.Model):
    # set db tanle name
    __tablename__ = 'owners'

    # set columns for the table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    # 1-m relationship: point to 'Pet' class, 
    # backref to owner to get the owner at that pet => pets.owner
    pets = db.relationship('Pet', backref='owner')

    def __repr__(self):
        return f'<Pet Owner {self.name}>'


class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    # define 1-m relationship between Owner and Pet model
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))

    def __repr__(self):
        return f"<Pet {self.name}, {self.species}>"
