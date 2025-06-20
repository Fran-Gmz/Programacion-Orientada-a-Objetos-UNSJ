# Gomez Francisco 45213346 E010-300
class Colectivo:
    __pantente:str
    __marca:str
    __modelo:str
    __capacidad:str
    __dniChofer:str
    __consumoPromedio:int


    def __init__(self, patente, marca, modelo, capacidad, dniChofer):
        self.__pantente = patente
        self.__marca = marca
        self.__modelo = modelo
        self.__capacidad = capacidad
        self.__dniChofer = dniChofer
        self.__consumoPromedio = 35

    def __str__(self):
        return 'patenete:{} ,marca:{} ,modelo:{} ,capacidad:{} ,dniChofer:{}'.format(self.__pantente,self.__marca, self.__modelo, self.__capacidad, self.__dniChofer)

    def getPatente (self):
        return self.__pantente
    def getMarca (self):
        return self.__marca
    
    def getModelo (self):
        return self.__modelo
    
    def getCapacidad (self):
        return self.__capacidad
    
    def getDniChofer (self):
        return self.__dniChofer
    
    def getConsumoPromedio (self):
        return self.__consumoPromedio
    
    def gastoTotal (self, kms):
        gasto = int(kms) / 100
        gastoTotal = gasto * int(self.__consumoPromedio)
        return gastoTotal