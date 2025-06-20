from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Trabajador(db.Model):
    __tablename__= 'trabajador'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), nullable = False)
    apellido = db.Column(db.String(50), nullable = False)
    dni = db.Column(db.String(10), nullable = False)
    correo = db.Column(db.String(100), unique = True, nullable = False)
    legajo = db.Column(db.Integer, nullable = False)
    horas = db.Column(db.Integer, nullable = False)
    funcion = db.Column(db.String(2), nullable = False)
    registro = db.relationship('RegistroHorario', backref = 'registrosh')


class RegistroHorario(db.Model):
    __tablename__= 'registrohorario'
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.String(30), nullable = False)
    horaEntrada = db.Column(db.String(20), nullable = False)
    horaSalida = db.Column(db.String(20), nullable = False)
    dependencia = db.Column(db.String(20), nullable = False)
    idTrabajador = db.Column(db.Integer, db.ForeignKey('trabajador.id'))        