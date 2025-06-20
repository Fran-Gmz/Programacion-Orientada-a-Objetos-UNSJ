
class Programa:
    __nombre:str
    __horaInicio:str
    __horaFin:str

    def __init__(self, nombre, inicio, fin):
       self.__nombre = nombre
       self.__horaInicio = inicio
       self.__horaFin = fin
    
    def __str__(self):
       return ' ----programa---- \n nombre:{}, horaInicio:{}, horaFin:{}'.format(self.__nombre, self.__horaInicio, self.__horaFin)
    
    def getNombre (self):
       return self.__nombre
    
    def getHoraInicio (self):
       return self.__horaInicio
    
    def getFin (self):
       return self.__horaFin