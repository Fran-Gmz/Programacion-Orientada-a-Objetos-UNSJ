#El archivo de pacientes registra: dni, Nombre, edad, y la unidad en la que presta servicio
class Paciente:
    __dni:set
    __nombre:str
    __unidad:str

    def __init__(self, dni, nombre, unidad):
        self.__dni = dni
        self.__nombre = nombre
        self.__unidad = unidad

    def __str__(self):
        return 'dni:{}, nombre:{}, unidad{}'.format(self.__dni, self.__nombre, self.__unidad)
    
    def __lt__ (self, otroPaciente):
        return self.__unidad < otroPaciente.__unidad
        
    def getDni(self):
        return self.__dni
    
    def getNombre (self):
        return self.__nombre  
    
    def getUnidad (self):
        return self.__unidad
    
    