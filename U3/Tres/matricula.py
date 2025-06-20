
from programa import Programa
from empleado import Empleado
class Matricula:
    __fecha:str
    __empleado:Empleado
    __programa:Programa

    def __init__(self, fecha, empleado, programa):
        self.__fecha = fecha
        self.__empleado = empleado
        self.__programa = programa
    
    def __str__(self):
        return 'fecha:{} \n ----Empleado---- \n {} \n ----Programa----: \n{}'.format(self.__fecha, self.__empleado, self.__programa)

    def getFecha (self):
        return self.__fecha
    
    def getPrograma (self):
        return self.__programa
    
    def getEmpleado (self):
        return self.__empleado