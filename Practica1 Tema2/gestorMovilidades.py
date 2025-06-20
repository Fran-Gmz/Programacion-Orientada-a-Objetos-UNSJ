import csv
import numpy as np
from movilidad import Movilidad
class gestorMovilidad:
    __cantidad:int
    __dimension:int
    __incremento:int
    __movilidades: np.ndarray

    def __init__(self,dimension=10, incremnto=10):
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremnto
        self.__movilidades = np.empty(self.__dimension, dtype=Movilidad)

    def __str__(self):
        s = ''
        for i in range(self.__cantidad):
            s += str(self.__movilidades[i]) + ' \n '
        return s
    def agregarMovilidad (self,unaMovilidad):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__movilidades.resize(self.__incremento)
        self.__movilidades[self.__cantidad] = unaMovilidad
        self.__cantidad += 1
    
    def testMovilidades (self):
        archivo = open('movilidades.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = False
        for fila in reader:
            if bandera == False:
                """Saltear primera fila"""
                bandera = True
            else:
                unaMovilidad = Movilidad(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
                self.agregarMovilidad(unaMovilidad)
        archivo.close()
        