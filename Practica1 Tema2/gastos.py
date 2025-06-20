"""El archivo “gastosAbril2025.csv”, que contiene los datos de los gastos realizados para las
movilidades de la empresa, registra: patente, fecha, importe del gasto, descripción.
"""
class Gasto:
    __patente:str
    __fecha:str
    __importe:str
    __descripcion:str

    def __init__(self, patente, fecha, importe, descripcion):
        self.__patente = patente
        self.__fecha = fecha
        self.__importe = importe
        self.__descripcion = descripcion

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.__patente, self.__fecha, self.__importe, self.__descripcion)
    
    def getPatente (self):
        return self.__patente
    
    def getFecha (self):
       return self.__fecha
    
    def getImporte (self):
       return self.__importe
    
    def getDescripcion (self):
       return self.__descripcion
    