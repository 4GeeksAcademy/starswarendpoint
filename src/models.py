from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }
class Personaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    color_de_cabello = db.Column(db.String(250), nullable=False)
    color_de_ojos = db.Column(db.String(250), nullable=False)
    personaje_id = db.relationship("Favoritos")

    def __repr__(self):
        return '<Personaje %r>' % self.nombre
    
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "color_de_cabello": self.color_de_cabello,
            "color_de_ojos": self.color_de_ojos
            # do not serialize the password, its a security breach
        }
   
class Planetas(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    clima = db.Column(db.String(250), nullable=False)
    gravedad = db.Column(db.String(250), nullable=False)
    planeta_id = db.relationship("Favoritos")

    def __repr__(self):
        return '<Planetas %r>' % self.nombre
    
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "clima": self.clima,
            "gravedad": self.gravedad
            # do not serialize the password, its a security breach
        }
    
class Usuarios(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    user_id_fav = db.relationship("Favoritos")

    def __repr__(self):
        return '<Usuarios %r>' % self.nombre
    
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email
            # do not serialize the password, its a security breach
        }
    
class Favoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id=  db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    personaje_id= db.Column(db.Integer, db.ForeignKey('personaje.id'))
    planeta_id = db.Column(db.Integer, db.ForeignKey('planetas.id'))

    def __repr__(self):
        return '<Favoritos %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "personaje_id": self.personaje_id,
            "planeta_id": self.planeta_id,
            # do not serialize the password, its a security breach
        }