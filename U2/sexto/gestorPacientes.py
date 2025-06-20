import csv
from paciente import Paciente

class gestorPaciente:
    __pacientes:list

    def __init__(self):
        self.__pacientes = []

    def __str__(self):
        s = ''
        long = len(self.__pacientes)
        for i in range(long):
            s += str(self.__pacientes[i]) + ' \n '
        return s
    
    def agregarPaciente (self, paciente):
        self.__pacientes.append(paciente)

    def testPacientes (self):
        archivo = open('pacientes.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = False
        for fila in reader:
            if bandera == False:
                """Saltear primera fila"""
                bandera = True
            else:
                unPaciente = Paciente(fila[0], fila[1], fila[2])
                self.agregarPaciente(unPaciente)
        archivo.close()

    def BuscarNombreApellido(self, dni, manejadorAtencion):
        indice = 0
        encontrado = False
        posicion = None
        long = len(self.__pacientes)
       
        while indice < long and encontrado == False:  
            if dni == self.__pacientes[indice].getDni():
                encontrado = True
                posicion = indice
            else:
                indice += 1
        if encontrado == True:
            nombreYapellido  = self.__pacientes[posicion].getNombre()
            cantidad = manejadorAtencion.CantidadDeAtenciones(dni)
            print('nombre y apellido: {}, atenciones que tuvo: {}'.format(nombreYapellido,cantidad))
        else:
            print('No se encontro dni')

    def listarPacientesSinAtencion(self, manejadorAtencion):
        long = len(self.__pacientes)
        enontrado = False
        for i in range(long):
            dni = self.__pacientes[i].getDni()
            bandera = manejadorAtencion.verificarAtencion(dni)
            if bandera != None:
                encontrado = True
                nombre = self.__pacientes[i].getNombre()
                print('{}, no tuvo atenciones'.format(nombre))

        if encontrado == False:
            print('No se encontraron pacientes sin atenciones ')

    def listarPacientesPorApellido(self):
        self.__pacientes.sort()
        long = len(self.__pacientes)
        s = ''
        for i in range(long):
            s += str(self.__pacientes[i]) + ' \n '
        print (s)
