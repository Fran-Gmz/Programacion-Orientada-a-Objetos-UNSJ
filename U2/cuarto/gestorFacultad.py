import numpy as np
import csv
from facultad import Facultad


class GestorFacultad:
    __cantidad:int
    __dimension:int
    __incremento:int
    __facultades:np.ndarray

    def __init__(self, dimension:int, incremnto:int=5):
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremnto
        self.__facultades = np.empty(dimension, dtype=Facultad)

    def __str__(self):
       s = ''
       for indice in range(self.__cantidad):
           s +=  str(self.__facultades[indice]) + ' \n '
       return s

    def agregarUnaFacultad(self, facultad):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__facultades.resize(self.__dimension)
        self.__facultades[self.__cantidad] = facultad
        self.__cantidad += 1

    def test(self):
        archivo = open('archivoFacultades.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = False
        for fila in reader:
            if bandera == False:
                """"Saltear Primera Fila"""
                bandera = True
            else:
                unaFacultad = Facultad(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.agregarUnaFacultad(unaFacultad)
        archivo.close()

    def buscarFacultadPorCodigo(self, codigoFacultad):
        indice = 0
        encontrado = False
        posicion = None
        while indice< self.__cantidad and encontrado == False:
            if codigoFacultad == self.__facultades[indice].getCodigo():
                encontrado = True
                posicion = indice
            else:
                indice += 1
        
        if encontrado == True:
            return self.__facultades[posicion].getNombre()
        else:
            print("No se encuentra en una facultad")

    def mostrarCantidadCarreras(self, listaCarreras):
        for i in range(self.__cantidad):
           codigo = self.__facultades[i].getCodigo()
           nombre = self.__facultades[i].getNombre()
           listaCarreras.cantidadDeCarrerasPorFacultad(codigo, nombre)
    
    def buscarFacultadPorNombre(self, nombre):
        indice = 0
        encontrado = False
        posicion = None
        while indice < self.__cantidad and encontrado == False:
            if nombre == self.__facultades[indice].getNombre():
                encontrado = True
                posicion = indice
            else:
                indice += 1

        if encontrado == True:
            return self.__facultades[posicion].getCodigo()
        else:
            print("No se encontró facultad")