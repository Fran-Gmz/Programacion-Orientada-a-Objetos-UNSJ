
from medio import Medio

class Prensa(Medio):
    __tipoPublicacion:str
    __periodicidad:str

    def __init__(self, nombre, audiencia, tipoPublicacion, periodicidad):
        super().__init__(nombre, audiencia)
        self.__tipoPublicacion = tipoPublicacion
        self.__periodicidad = periodicidad

    def __str__(self):
        s = super().__str__()
        s += ' tipoPublicacion:{}, periodicidad:{}'.format(self.__tipoPublicacion, self.__periodicidad)
    
    def getTipoPublicacion(self):
        return self.__tipoPublicacion

    def getPeriodicidad (self):
        return self.__periodicidad

    