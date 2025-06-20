import numpy as np
import csv
from carrera import Carrera
from gestorFacultad import GestorFacultad

class GestorCarrera ():
    __cantidad:int
    __dimension:int
    __incremetnto:int
    __carreras: np.ndarray

    def __init__(self, dimension, incremento = 5):
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremetnto = incremento
        self.__carreras = np.empty(dimension, dtype=Carrera)

    def __str__(self):
        s = ''
        for indice in range(self.__cantidad):
            s += str(self.__carreras[indice]) + ' \n '
        return s

    def agregarCarrera(self,unaCarrera):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremetnto
            self.__carreras.resize(self.__dimension)
        self.__carreras[self.__cantidad] = unaCarrera
        self.__cantidad += 1



    def test(self):
        archivo = open('archivoCarreras.csv','r', encoding='latin-1')
        reader = csv.reader(archivo, delimiter=';')
        bandera = False
        for fila in reader:
            if bandera == False:
                """"Saltear Primera Fila"""
                bandera = True
            else:
                unaCarrera = Carrera(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
                self.agregarCarrera(unaCarrera)
        archivo.close()

    def buscarFacultadPorCarrera (self, nombre:str):
        indice = 0
        encontrado = False
        posicion = None
        while indice< self.__cantidad and encontrado == False:
            if nombre.lower() == self.__carreras[indice].getNombre().lower(): #lower 
                encontrado = True
                posicion = indice
            else:
                indice += 1
        
        if encontrado == True:
            return self.__carreras[posicion].getCodigoFacultad()
        else:
            print("No se existe esa carrera")

    def cantidadDeCarrerasPorFacultad(self, codigo, nombre):
        cantidad = 0
        for i in range(self.__cantidad):
            if self.__carreras[i].getCodigoFacultad() == codigo:
                cantidad += 1
                #print('{}'.format(self.__carreras[i].getNombre()))
        print('total {} carreras en {}'.format(cantidad,nombre))
       
    def mostrarDatosCarreras(self, codigo):
        lista = []
        contador = 0
        for i in range (self.__cantidad):
            if codigo == self.__carreras[i].getCodigoFacultad():
                lista.append(self.__carreras[i])
                contador += 1
        lista.sort()

        for j in range(contador):
            print('{}, {}'.format(lista[j].getNombre(), lista[j].getDuracion()))