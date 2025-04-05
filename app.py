from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://aime:5mKbuTUEhCjqXXcmijUtvD4DfzKrGvHC@dpg-cv7oreij1k6c739gn5s0-a.oregon-postgres.render.com/biblioteca_7xwc'
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

# Crear un nuevo estudiante (formulario)
@app.route('/alumnos/new', methods=['GET', 'POST'])
def create_alumno():
    if request.method == 'POST':
        no_control = request.form['no_control']
        nombre = request.form['nombre']
        ap_paterno = request.form['ap_paterno']
        ap_materno = request.form['ap_materno']
        semestre = request.form['semestre']

        nuevo_alumno = Alumno(no_control=no_control, nombre=nombre, ap_paterno=ap_paterno, ap_materno=ap_materno, semestre=semestre)
        db.session.add(nuevo_alumno)
        db.session.commit()

        return redirect(url_for('listar_alumnos'))
    return render_template('create_alumno.html')

# Actualizar un alumno (formulario)
@app.route('/alumnos/update/<string:no_control>', methods=['GET', 'POST'])
def update_alumno(no_control):
    alumno = Alumno.query.get(no_control)
    if request.method == 'POST':
        alumno.nombre = request.form['nombre']
        alumno.ap_paterno = request.form['ap_paterno']
        alumno.ap_materno = request.form['ap_materno']
        alumno.semestre = request.form['semestre']
        
        db.session.commit()
        return redirect(url_for('listar_alumnos'))
    return render_template('update_alumno.html', alumno=alumno)

# Eliminar un alumno
@app.route('/alumnos/delete/<string:no_control>')
def delete_alumno(no_control):
    alumno = Alumno.query.get(no_control)
    if Alumno:
        db.session.delete(alumno)
        db.session.commit()
    return redirect(url_for('listar_alumnos'))

if __name__ == '__main__':
    app.run(debug=True)
