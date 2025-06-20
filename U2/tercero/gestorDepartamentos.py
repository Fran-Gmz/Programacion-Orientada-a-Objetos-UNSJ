from departamentos import Departamento
import csv

class GestorDepartamentos:
    __departamentos:list

    def __init__(self):
        self.__lista = []

    def cargar (self):
        archivo = open("Departamentos.csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            id = str(fila[0])
            nom = str(fila[1]) 
            self.__lista.append(Departamento(id, nom))
        archivo.close()

    def __str__(self):
        s = ''
        for i in range(len(self.__lista)):
            s += str(self.__lista) + '\n'
        return s