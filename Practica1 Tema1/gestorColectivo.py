# Gomez Francisco 45213346 E010-300
import numpy as np
import csv
from colectivo import Colectivo

class gestorColectivo:
    __dimension:int
    __incremento:int
    __cantidad:str
    __colectivos:np.ndarray

    def __init__(self, dimension=10, incremneto=10):
        self.__dimension = dimension
        self.__incremento = incremneto
        self.__cantidad = 0
        self.__colectivos = np.empty(self.__dimension, dtype=Colectivo)

    def __str__(self):
        s = ''
        for i in range(self.__cantidad):
            s += str(self.__colectivos[i]) + ' \n '
        return s
    
    def agregarColectivo (self, unColectivo):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__colectivos.resize(self.__dimension)
        self.__colectivos[self.__cantidad] = unColectivo
        self.__cantidad += 1

    def testColectivos(self):
        archivo = open('colectivos.csv')
        reader = csv.reader(archivo, delimiter=";")
        bandera = False
        for fila in reader:
            if bandera == False:
                """Saltear primera fila"""
                bandera = True
            else:
                unColectivo = Colectivo(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.agregarColectivo(unColectivo)
        archivo.close()
        
    def informeDelosTramosPorDni(self, dni, manejadorTramo):
        indice = 0
        encontrado = False
        posicion = None

        while indice < self.__cantidad and encontrado == False:
            if dni == self.__colectivos[indice].getDniChofer():
                encontrado = True
                posicion = indice
            else:
                indice += 1

        if encontrado == True:
            patente = self.__colectivos[posicion].getPatente()
            manejadorTramo.informarOrigenDestinoKm(patente)
        else:
            print('No se encontro dni')

    def motrarTotalKmyGastos(self, manejadorTramo):

        for i in range(self.__cantidad):
            patente = self.__colectivos[i].getPatente()
            consumo = self.__colectivos[i].getConsumoPromedio()
            kms = manejadorTramo.obtenerKilometrosPorColectivo(patente)
            gastoTotal = self.__colectivos[i].gastoTotal(kms)

            print('colectivo:{} reccorrio en total {}km y su gasto fue ${}'.format(patente,kms,gastoTotal))