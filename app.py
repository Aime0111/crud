from flask import Flask, jsonify, render_template
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

    def to_dict(self):
        return {
            'no_control': self.no_control,
            'nombre': self.nombre,
            'ap_paterno': self.ap_paterno,
            'ap_materno': self.ap_materno,
            'semestre': self.semestre,
        }

# Endpoint para obtener todos los estudiantes
@app.route('/alumnos', methods=['GET'])
def listar_alumnos():
    alumnos = Alumno.query.all()
    return render_template('index.html', alumnos=alumnos)