from matricula import Matricula
import csv

class GestorMatricula:
    __matriculas:list

    def __init__(self):
        self.__matriculas = []

    def __str__(self):
        s = ''
        long = len(self.__matriculas)
        for i in range(long):
            s += str(self.__matriculas[i]) + ' \n '
        return s
    
    def agregarMatricula (self, unaMatricula):
        self.__matriculas.append(unaMatricula)
    
    
    def cargarArchivo (self, manejadorEmpleados, manejadorProgramas):
        archivo = open('matriculas.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            fecha = fila[0]
            empleado = manejadorEmpleados.buscarEmpleadoPorNombreYdevuelveObjeto(fila[1])
            programa =  manejadorProgramas.buscarProgramaPorNombreYdevuelveObjeto(fila[2])
            if empleado != None and programa != None:
                unaMatricula = Matricula(fecha, empleado, programa)
                self.agregarMatricula(unaMatricula)
        archivo.close()

    def informeDeLosProgramasMatriculado(self):
        id = int(input('Ingresa id de la persona: '))
        long = len(self.__matriculas)
        s = ''
        for i in range(long):
            if id == self.__matriculas[i].getEmpleado().getId():
                s += self.__matriculas[i].getPrograma().getNombre() + ' '
        print('El empleado de la id {} esta matriculado en:'.format(id))
        print(s)

    def mostrarEmpleadosMatriculadosEnUnPrograma(self):
        nombre = input('Ingresa nombre del programa de capacitacion: ')
        long = len(self.__matriculas)
        s = ''
        for i in range(long):
            if nombre == self.__matriculas[i].getPrograma().getNombre():
                s += self.__matriculas[i].getEmpleado().getNombre()
        print('Los empleados matriculas al programa {} son:'.format(nombre))
        print(s)

    def informarEmpleadosNoMatriculasdos(self):
        long = len(self.__matriculas)
        for i in range(long):
            pass