import csv
from gastos import Gasto
class gestorGastos:
    __gastos:list

    def __init__(self):
        self.__gastos = []

    def __str__(self):
        s = ''
        long = len(self.__gastos)
        for i in range(long):
            s += str(self.__gastos[i]) + ' \n '
        return s
    
    def agregarGasto (self, unGasto):
        self.__gastos.append(unGasto)
    
    def testGastos(self):
        archivo = open('gastosAbril2025.csv')
        reader = csv.reader(archivo, delimiter=";")
        bandera = False
        for fila in reader:
            if bandera == False:
                """saltear primera fila"""
                bandera = True
            else:
                unGasto = Gasto(fila[0], fila[1], fila[2], fila[3])
                self.agregarGasto(unGasto)
        archivo.close()