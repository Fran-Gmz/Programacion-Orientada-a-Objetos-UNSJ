class Beca:
    __id:str
    __tipo:str
    __importe:float

    def __init__(self, id, tipo, importe):
        self.__id = id
        self.__tipo = tipo 
        self.__importe = importe

    def __str__(self):
        return 'id:{},tipo:{},importe:{}'.format(self.__id, self.__tipo, str(self.__importe))
    
    def getId (self):
        return self.__id
    
    def getTipo (self):
        return self.__tipo
    
    def getImporte (self):
        return self.__importe