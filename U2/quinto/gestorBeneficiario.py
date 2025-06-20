import numpy as np
import csv
from beneficiario import Beneficiario

class GestorBeneficiario:
    __cantidad:int
    __dimension:int
    __incremento:int
    __beneficiarios:np.ndarray

    def __init__(self, dimesion, incremento=5):
        self.__cantidad = 0
        self.__dimension = dimesion
        self.__incremento = incremento
        self.__beneficiarios = np.empty(self.__dimension, dtype=Beneficiario)

    def __str__(self):
        s = ''
        for i in range(self.__cantidad):
            s += str(self.__beneficiarios[i]) + ' \n '
        return s

    def agregarUnBeneficiario (self, unBeneficiario):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__beneficiarios.resize(self.__dimension)
        self.__beneficiarios[self.__cantidad] = unBeneficiario
        self.__cantidad += 1

    def test(self):
        archivo = open('Archivobeneficiarios.csv')
        reader = csv.reader(archivo, delimiter=";")
        bandera = False
        for fila in reader:
            if bandera == False:
                bandera = True
                """Saltar Primera Fila"""
            else:
                unBeneficiario = Beneficiario(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7])
                self.agregarUnBeneficiario(unBeneficiario)
        archivo.close()

    def beneficiariosPorId(self, id):
        contador = 0
        for indice in range(self.__cantidad):
            if id == self.__beneficiarios[indice].getIdbeca():
                print(self.__beneficiarios[indice])
                contador += 1
        return contador
    
    def masDeUnaBeca(self, dni):
        indice = 0
        encontrado = False
        posicion = None
        while indice < self.__cantidad and encontrado == False:
            if dni == self.__beneficiarios[indice].getDni():
                encontrado = True
                posicion = indice
            else:
                indice += 1
        if encontrado == True:
            contador = 0
            for j in range(self.__cantidad):
                if self.__beneficiarios[posicion].getDni() == self.__beneficiarios[j].getDni():
                    contador += 1
                    if contador > 1:
                        print('{} {} tiene mas de una beca'.format(self.__beneficiarios[posicion].getNombre(), self.__beneficiarios[posicion].getApellido()))
            if contador == 1:
                print('Tiene solo una beca')        
        else:
            print('No se encontró beneficirio con es dni')

    def listarBeneficiarios(self):
        lista = np.sort(self.__beneficiarios)
        print(self.__beneficiarios)
