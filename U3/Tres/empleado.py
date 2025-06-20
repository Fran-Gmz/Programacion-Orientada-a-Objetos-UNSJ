
class Empleado:
    __nombre:str
    __id:int
    __puseto:str

    def __init__(self, nombre, id, puesto):
        self.__nombre = nombre
        self.__id = id
        self.__puseto = puesto

    def __str__(self):
        return '{}, {}, {}'.format(self.__nombre, self.__id, self.__puseto)
    
    def getNombre (self):
        return self.__nombre
    
    def getId (self):
        return self.__id
    
    def getPuesto (self):
        return self.__puseto