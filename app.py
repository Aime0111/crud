from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/")
def index():
    return "Hola Mundo"

# Definición del modelo de la tabla 'estudiantes'
class Alumno(db.Model):
    __tablename__ = 'alumnos'
    no_control = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    ap_paterno = db.Column(db.String)
    ap_materno = db.Column(db.String)
    semestre = db.Column(db.Integer)

# Endpoint para obtener todos los estudiantes
@app.route('/alumnos', methods=['GET'])
def obtener_alumnos():
    alumnos = Alumno.query.all()
    lista_alumnos = []
    for alumno in alumnos:
        lista_alumnos.append({
            'no control': alumno.no_control,
            'nombre': alumno.nombre,
            'ap paterno': alumno.ap_paterno,
            'ap materno': alumno.ap_materno,
            'semestre': alumno.semestre
        })
    return jsonify(lista_alumnos)