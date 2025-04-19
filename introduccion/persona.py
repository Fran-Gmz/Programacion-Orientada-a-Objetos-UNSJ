class Persona (object):
    __dni:int
    __nombre:str
    __apellido:str
    __sueldo:float

    def __init__(self, dni, nombre, apellido, sueldo):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__sueldo = sueldo

    def __str__(self):
        return 'dni:{}, nombre:{}, apellido:{}, sueldo:{}'.format(str(self.__dni), self.__nombre, self.__apellido , str(self.__sueldo))
    
    def getDni (self):
        return self.__dni
    
    def getNombre (self):
        return self.__nombre
    
    def getApellido (self):
        return self.__apellido
    
    def getSueldo (self):
        return self.__sueldo
