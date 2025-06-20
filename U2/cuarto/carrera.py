class Carrera:
    __codigo:str
    __nombre:str
    __titulo:str
    __duracion:str
    __nivel:str
    __codigoFacultad:str

    def __init__(self, codigo, nombre, titulo, duracion, nivel, codigoFacultad):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__titulo = titulo
        self.__duracion = duracion
        self.__nivel = nivel
        self.__codigoFacultad = codigoFacultad


    def __str__(self):
        return 'codigo:{}, nombre:{}, titulo:{}, duracion:{}, nivel:{}, facultad:{}'.format(self.__codigo, self.__nombre, self.__titulo, self.__duracion, self.__nivel, self.__codigoFacultad)
    
    def __lt__(self, otra_carrera):
        return self.__nombre < otra_carrera.__nombre
    
    def getCodigo (self):
        return self.__codigo
    
    def getNombre (self):
        return self.__nombre
    
    def getTitulo(self):
        return self.__titulo
    
    def getDuracion (self):
        return self.__duracion
    
    def getNivel(self):
        return self.__nivel
    
    def getCodigoFacultad(self):
        return self.__codigoFacultad
    

    def __lt__ (self,otroCarrera):
        self.__nombre < otroCarrera.__nombre