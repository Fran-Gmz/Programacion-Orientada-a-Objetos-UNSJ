from flask import Flask, render_template, request, session
from datetime import datetime

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Trabajador, RegistroHorario

@app.route('/')
def home():
    return render_template('home.html')

#----------------------Funcionalidad 1----------------------------------
@app.route('/registroDeEntrada')
def registrarEntrada():
    return render_template ('registroDeEntrada.html')

@app.route('/entrada', methods = ['GET','POST'])
def resultadoRegistroEntrada():
    if request.method == 'POST':
        if request.form['legajo'] and request.form['dni'] and request.form['dependencia']:
            unTrabajador = Trabajador.query.filter_by(legajo = request.form['legajo']).first()
            if unTrabajador != None:
                dni = unTrabajador.dni
                cuatroUltimas = dni[-4:]
                if cuatroUltimas == request.form['dni']:
                    id = unTrabajador.id
                    fechaHoy = datetime.now().date()
                    unRegistroHorario = RegistroHorario.query.filter_by(idTrabajador = id,fecha = fechaHoy).first()
                    if unRegistroHorario == None:
                        hora = datetime.now().strftime("%H:%M:%S.%f")
                        nuevoRegistroHorario = RegistroHorario(fecha = fechaHoy,  horaEntrada = hora, horaSalida = "0", dependencia = request.form['dependencia'], idTrabajador = id )
                        db.session.add(nuevoRegistroHorario)
                        db.session.commit()
                        return render_template('home.html')
                    else:
                        return render_template('respuesta.html', afirmacion = False, mensaje = 'Error, ya se registró la entrada el dia de hoy.')
                else:
                    return render_template('respuesta.html', afirmacion = False, mensaje = 'Error, no se encontró las cuatro ultimas del dni.')
            else:
                return render_template('respuesta.html', afirmacion = False, mensaje = 'Error, legajo no encontrado.')
        else:
            return render_template('respuesta.html', afirmacion = False, mensaje = 'Error, mal ingreso de datos.')
        
#----------------------- Funcionalidad 2 -----------------------------
@app.route('/registroDeSalida')
def registrarSalida():
    return render_template('registroDeSalida.html')
        
@app.route('/salida', methods = ['GET','POST'])
def resultadoRegistroSalida():
    if request.method == 'POST':
        if request.form['legajo'] and request.form['dni']:
            unTrabajador = Trabajador.query.filter_by(legajo = request.form['legajo']).first()
            if unTrabajador != None:
                dni = unTrabajador.dni
                cuatroUltimas = dni[-4:]
                if cuatroUltimas == request.form['dni']:
                    fechaHoy = datetime.now().date()
                    registro = RegistroHorario.query.filter_by(idTrabajador = unTrabajador.id, fecha = fechaHoy).first()
                    if registro != None:
                        hora = registro.horaSalida
                        if str(hora) == "0":
                            id = unTrabajador.id
                            return render_template('confirmar.html', afirmacion = True, dependencia = registro.dependencia, idTrabajador = id)
                        else:
                            return render_template('respuesta.html', mensaje = 'Error, la salida ya se registró el día de hoy. {}'.format(hora))
                    else:
                        return render_template('respuesta.html', mensaje = 'Error, no se encontró  registro de entrada de hoy.')
                else:
                    return render_template('respuesta.html', mensaje = 'Error, no se encontró las cuatro ultimas del dni.')
            else:
                return render_template('respuesta.html', mensaje = 'Error, legajo no encontrado.')
        else:
            return render_template('respuesta.html', mensaje = 'Error, mal ingreso de datos.')

@app.route('/confirmarSalida')
def confirmarSalida():
    return render_template('confirmar.html')

@app.route('/home/<idT>')
def salidaConfirmada(idT):
    unTrabajador = Trabajador.query.filter_by(id = idT).first()
    fechaHoy = datetime.now().date()
    registro = RegistroHorario.query.filter_by(idTrabajador = unTrabajador.id, fecha = fechaHoy).first()
    hora = datetime.now().strftime("%H:%M:%S.%f")
    registro.horaSalida = hora
    db.session.commit()
    return render_template('home.html')

#-------------------------Funcionalidad Tres-------------------------------

@app.route('/consultarRegistros')
def consultarRegistros ():
    return render_template('consultar.html')

@app.route('/consultar', methods = ['GET','POST'])
def consultar():
    if request.method == 'POST':
        if request.form['legajo'] and request.form['dni'] and request.form['fechaInicio'] and request.form['fechaFinal']:
            unTrabajador = Trabajador.query.filter_by(legajo = request.form['legajo']).first()
            if unTrabajador != None:
                dni = unTrabajador.dni
                cuatroUltimas = dni[-4:]
                if cuatroUltimas == request.form['dni']:
                    fechaInicio = request.form['fechaInicio']
                    fechaFinal = request.form['fechaFinal']
                    registros = RegistroHorario.query.filter(RegistroHorario.idTrabajador == unTrabajador.id, RegistroHorario.fecha >= fechaInicio,RegistroHorario.fecha <= fechaFinal).order_by(RegistroHorario.fecha).all()
                    if registros != None:
                        return render_template('mostrarRegistros.html', registrosPorFecha = registros)
                    else:
                        render_template('respuesta.html', mensaje = 'Error, no se encontraron registros.')
                else:
                    return render_template('respuesta.html', mensaje = 'Error, no se encontró las cuatro ultimas del dni.')
            else:
                return render_template('respuesta.html', mensaje = 'Error, legajo no encontrado.')
        else:
            return render_template('respuesta.html', mensaje = 'Error, mal ingreso de datos.')


@app.route('/mostrarRegistros:')
def mostrarRegistros():
    return render_template('mostrarRegistros.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5002)
