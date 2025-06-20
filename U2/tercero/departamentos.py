class Departamento:
    __numero:int
    __nombre:str

    def __init__(self, numero, nombre):
        self.__numero = numero
        self.__nombre = nombre

    def __str__(self):
        return 'numero:{}, nombre:{}'.format(str(self.__numero),self.__nombre)
    
    def getNumero (self):
        return self.__numero
    
    def getNombre (self):
        return self.__nombre