from empleado import Empleado
import csv
class GestorEmpleado:
    __empleados:list

    def __init__(self):
        self.__empleados = []
    
    def __str__(self):
        s = ''
        long = len(self.__empleados)
        for i in range(long):
            s += str(self.__empleados[i]) + ' \n '
        return s
    
    def agregarEmpleado (self, unEmpleado):
        self.__empleados.append(unEmpleado)

    def cargarArchivo (self):
        archivo = open('empleados.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            unEmpleado = Empleado(fila[0],int(fila[1]),fila[2])
            self.agregarEmpleado(unEmpleado)
        archivo.close()

    def buscarEmpleadoPorNombreYdevuelveObjeto (self, nombre):
        i = 0
        long = len(self.__empleados)
        encontrado = False
        objeto = None
        while i < long and encontrado == False:
            if nombre == self.__empleados[i].getNombre():
                encontrado = True
                objeto = self.__empleados[i]
            else:
                i += 1
        if encontrado == True:
            return  objeto
        else:
            print ('No se encontro Empleado')