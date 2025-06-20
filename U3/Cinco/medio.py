

class Medio:
    __nombre:str
    __audiencia:int

    def __init__(self, nombre, audiencia):
        self.__nombre = nombre
        self.__audiencia = audiencia
    
    def __str__(self):
        return 'nombre:{}, audiencia:{}'.format(self.__nombre, self.__audiencia)

    def getNombre(self):
        return self.__nombre
    
    def getAudiencia(self):
        return self.__audiencia
