import csv
import numpy as np
from atencion import Atencion

class gestorAtencion:
    __cantidad:str
    __dimension:str
    __incremento:str
    __atenciones:np.ndarray

    def __init__(self, dimension, incremento=10):
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento
        self.__atenciones = np.empty(self.__dimension, dtype=Atencion)

    def __str__(self):
        s = ''
        for i in range(self.__cantidad):
            s += str(self.__atenciones[i]) + ' \n '
        return s
    
    def agregarAtencion (self, unaAtencion):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__atenciones.resize(self.__dimension)
        self.__atenciones[self.__cantidad] = unaAtencion
        self.__cantidad += 1

    
    def testAtenciones(self):
        archivo = open('atenciones.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = False
        for fila in reader:
            if bandera == False:
                """Saltear primera fila"""
                bandera = True
            else:
                unaAtencion = Atencion(fila[0],fila[1],fila[2])
                self.agregarAtencion(unaAtencion)
        archivo.close()

    def informeDeFecha(self, fecha):
        contador = 0
        sumador = 0
        for i in range(self.__cantidad):
            if fecha == self.__atenciones[i].getFecha():
                contador += 1
                sumador += float(self.__atenciones[i].getImporte())
        
        print('atenciones realizadas: {}, importe total que debe disponer la UNSJ: {} '.format(contador, sumador))

    def CantidadDeAtenciones(self, dni):
        cantidad = 0
        for i in range(self.__cantidad):
            if dni == self.__atenciones[i].getDni():
                cantidad += 1
        return cantidad

    def verificarAtencion(self, dni):
        indice = 0
        encontrado = False
        while indice < self.__cantidad and encontrado == False:
            if dni == self.__atenciones[indice].getDni():
                encontrado = True
            else:
                indice += 1
        if encontrado == False:
            return True

