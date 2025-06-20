#El archivo atenciones registra: Dni, fecha de atención, importe de atención.
class Atencion:
    __dni:str
    __fecha:str
    __importe:float

    def __init__(self, dni, fecha, importe):
        self.__dni = dni
        self.__fecha = fecha
        self.__importe = importe
    
    def __str__(self):
        return 'dni:{}, fecha:{}, importe:{}'.format(self.__dni, self.__fecha, str(self.__importe))
    
    def getDni (self):
        return self.__dni
    
    def getFecha (self):
        return self.__fecha
    
    def getImporte (self):
        return self.__importe