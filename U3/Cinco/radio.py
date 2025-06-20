
from medio import Medio
from programa import Programa

class Radio(Medio):
    __emisora:str
    __frecuencia:str
    __programas:list

    def __init__(self, nombre, audiencia, emisora, frecuencia):
        super().__init__(nombre, audiencia)
        self.__emisora = emisora
        self.__frecuencia = frecuencia
        
    def __str__(self):
        s = super().__str__()
        s += ' emisora:{}, frecuencia:{} '.format(self.__emisora, self.__frecuencia)
        long = len(self.__programas)
        for i in range(long):
            s += str(self.__programas[i]) + ' \n '
        return s
    
    def agregarPrograma(self, nombre, inicio , fin):
        unPrograma = Programa(nombre, inicio, fin)
        self.__programas.append(unPrograma)

    def getEmisora (self):
        return self.__emisora
    
    def getFrecuencia (self):
        return self.__frecuencia
    
    def getProgramas (self):
        return self.__programas