
from medio import Medio
from programa import Programa

class Television(Medio):
    __cantidadCanales:int
    __programas:list

    def __init__(self, nombre, audiencia, cantidadCanales=0):
        super().__init__(nombre, audiencia)
        self.__cantidadCanales = cantidadCanales
    
    def __str__(self):
        s = super().__str__()
        s += 'cantidadCanales:{}'.format(self.__cantidadCanales)
        long = len(self.__programas)
        for i in range(long):
            s += str(self.__programas[i]) + ' \n '
        return s
    
    def agregarPrograma(self, nombre, inicio , fin):
        unPrograma = Programa(nombre, inicio, fin)
        self.__programas.append(unPrograma)
    
    def getCantidadCanales (self):
        return self.__cantidadCanales
    
    def getProgramas (self):
        return self.__programas