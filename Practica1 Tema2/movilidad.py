"""El archivo “movilidades.csv”, que contiene los datos de cada una de las movilidades, a saber:
patente, tipo (‘C’-Camión, ‘A’-Camioneta), capacidad de carga, importe mensual patente, marca
(‘Fiat’, ‘Ford’, ‘Peugeot’, etc.), modelo (‘Fiorino’, ‘F100’, etc.)."""
class Movilidad:
    __patente:str
    __tipo:str
    __capacidadCarga:str
    __importeMensualPatente:str
    __marca:str
    __modelo:str

    def __init__(self, patente, tipo, capacidadCarga, importe, marca, modelo):
        self.__patente = patente
        self.__tipo = tipo
        self.__capacidadCarga = capacidadCarga
        self.__importeMensualPatente = importe
        self.__marca = marca
        self.__modelo = modelo

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}'.format(self.__patente, self.__tipo, self.__capacidadCarga, self.__importeMensualPatente, self.__marca, self.__modelo)
    
    def getPatente (self):
        return self.__patente
    
    def getTipo (self):
        return self.__tipo
    
    def getCapacidad (self):
        return self.__capacidadCarga
    def getImporte (self):
        return self.__importeMensualPatente
    
    def getModelo (self):
        return self.__modelo