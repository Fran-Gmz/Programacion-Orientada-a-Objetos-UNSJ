
from programa import Programa
import csv
class GestorPrograma:
    __programas:list

    def __init__(self):
        self.__programas = []

    def __str__(self):
        s = ''
        long = len(self.__programas)
        for i in range(long):
            s += str(self.__programas) + ' \n '
        return s
    
    def agregarPrograma (self, unPrograma):
        self.__programas.append(unPrograma)
    
    def cargarArchivo(self):
        archivo = open('programas.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            unPrograma = Programa(fila[0],fila[1],int(fila[2]))
            self.agregarPrograma(unPrograma)
        archivo.close()
    
    def buscarProgramaPorNombreYdevuelveObjeto (self, nombre):
        i = 0
        long = len(self.__programas)
        encontrado = False
        objeto = None
        while i < long and encontrado == False:
            if nombre == self.__programas[i].getNombre():
                encontrado = True
                objeto = self.__programas[i]
            else:
                i += 1
        if encontrado == True:
            return  objeto
        else:
            print ('No se encontro progrma')