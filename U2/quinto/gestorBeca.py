import numpy as np
import csv
from beca import Beca

class GestorBeca:
    __cantidad:int
    __dimension:int
    __incremento:int
    __becas:np.ndarray

    def __init__(self, dimension, incremento=5):
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento
        self.__becas = np.empty(dimension, dtype=Beca)

    def __str__(self):
        s = ''
        for i in range(self.__cantidad):
            s += str(self.__becas[i]) + ' \n '
        return s
    
    def agregarUnaBeca (self, unaBeca):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__becas.resize(self.__dimension)
        self.__becas[self.__cantidad] = unaBeca
        self.__cantidad += 1

    def test(self):
        archivo = open('Archivobecas.csv')
        reader = csv.reader(archivo, delimiter=";")
        bandera = False
        for fila in reader:
            if bandera == False:
                bandera = True
                """Saltear Primera Fila"""
            else:
                unaBeca = Beca(fila[0],fila[1], fila[2])
                self.agregarUnaBeca(unaBeca)
        archivo.close()

    
    def beneficiariosYimporteTotal(self, nombreBeca, manejadorBeneficiario):
        indice = 0
        encontrado = False
        posicion = None

        while indice < self.__cantidad and encontrado == False:
            if nombreBeca == self.__becas[indice].getTipo():
                encontrado = True
                posicion = indice
            else:
                indice += 1
    
        if encontrado == True:
           importe = self.__becas[indice].getImporte()
           print('Estudiantes de la beca {}'.format(nombreBeca))
           cantidad = manejadorBeneficiario.beneficiariosPorId(self.__becas[indice].getId())
           importeTotal = float(importe) * int(cantidad)
           print("El importe total que debe disponer la secretaria es de {}".format(str(importeTotal)))
        else:
            print('El nombre no coincide con ninguna beca')