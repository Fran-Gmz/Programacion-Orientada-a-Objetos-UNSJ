# Gomez Francisco 45213346 E010-300
import csv
from tramo import Tramo

class gestorTramo:
    __tramos:list

    def __init__(self):
        self.__tramos = []
    
    def __str__(self):
        long = len(self.__tramos)
        s = ''
        for i in range(long):
            s += str(self.__tramos[i]) + ' \n '
        return s
    
    def agregarTramo (self, unTramo):
        self.__tramos.append(unTramo)

    def testTramos (self):
        archivo = open('tramos.csv')
        reader = csv.reader(archivo,delimiter=";")
        bandera = False
        for fila in reader:
            if bandera == False:
                """Saltear Primera fila"""
                bandera = True
            else:
                unTramo = Tramo(fila[0],fila[1],fila[2],fila[3])
                self.agregarTramo(unTramo)
        archivo.close()

    def informarOrigenDestinoKm(self,patente):
        recorrido = 0
        long = len(self.__tramos)
        for i in range(long):
            if patente == self.__tramos[i].getPatente():
                recorrido += int(self.__tramos[i].getDistancia())
                origen = self.__tramos[i].getOrigen()
                destino = self.__tramos[i].getDestino()
                km = self.__tramos[i].getDistancia()
                print('origen:{}, destino:{} ,distancia km:{}'.format(origen,destino,km))
        print('total km recorridos {}'.format(recorrido))

    def obtenerKilometrosPorColectivo(self, patente):
        recorrido = 0
        long = len(self.__tramos)
        for i in range(long):
            if patente == self.__tramos[i].getPatente():
                recorrido += int(self.__tramos[i].getDistancia())
        return recorrido

    def listarDatosPorDistancia(self, distancia):
        self.__tramos.sort(distancia)

        long = len(self.__tramos)
        for i in range(long):
            origen = self.__tramos[i].getOrigen()
            destino = self.__tramos[i].getDestino()
            patente = self.__tramos[i].getPatente()
            print('origen:{},destino:{},patente:{}'.format(origen,destino,patente))




        