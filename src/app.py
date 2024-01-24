"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Favoritos, Planetas, Usuarios, Personaje
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/usuarios', methods=['GET'])
def handle_hello():
    todoslosusuarios=Usuarios.query.all()
    resultados=list(map(lambda usuario: usuario.serialize(), todoslosusuarios))
    return jsonify(resultados),200

@app.route('/planetas', methods=['GET'])
def getplaneta():
    todoslosplanetas=Planetas.query.all()
    resultados=list(map(lambda planetas: planetas.serialize(), todoslosplanetas))
    return jsonify(resultados),200

@app.route('/personaje', methods=['GET'])
def getpersonaje():
    todoslospersonaje=Personaje.query.all()
    resultados=list(map(lambda personaje: personaje.serialize(), todoslospersonaje))
    return jsonify(resultados),200

@app.route('/favoritos', methods=['GET'])
def getfavoritos():
    todoslosfavoritos=Favoritos.query.all()
    if todoslosfavoritos == []: 
        return jsonify({"msg": "no hay favoritos"}), 404
    resultados=list(map(lambda favoritos: favoritos.serialize(), todoslosfavoritos))
    return jsonify(resultados),200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
