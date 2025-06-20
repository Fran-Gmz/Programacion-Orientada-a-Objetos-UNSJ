# Gomez Francisco 45213346 E010-300
class Tramo:
    __ciudadOrigen:str
    __ciudadDestino:str
    __distancia:str
    __patenteColectivo:str
    

    def __init__(self, origen, destino, distancia , patente):
        self.__ciudadOrigen = origen
        self.__ciudadDestino = destino
        self.__distancia = distancia
        self.__patenteColectivo = patente

    def __str__(self):
        return 'origen:{}, destino:{}, distancia:{}, patente:{}'.format(self.__ciudadOrigen, self.__ciudadDestino, self.__distancia, self.__patenteColectivo)
    
    def getOrigen (self):
        return self.__ciudadOrigen
    
    def getDestino (self):
       return self.__ciudadDestino
    
    def getDistancia (self):
       return self.__distancia
    
    def getPatente (self):
       return self.__patenteColectivo
    
    def __gt__ (self, distancia):
        if self.__distancia > distancia:
            return self.__distancia