from Plan import Plan
from Telefonia import Telefonia
from Television import Television
import csv
class GestorPlan:
    __planes : list
    
    def __init__(self):
        self.__planes = []
    
    def retornarLongitudLista(self):
        return len(self.__planes)
    def leerCsv(self):
        archivo = open("planes.csv", "r")
        reader=csv.reader(archivo, delimiter=";")
        
        for fila in reader:
            if(fila[0] == 'M'):
                telefonia = Telefonia(fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
                self.__planes.append(telefonia)
                
            if(fila[0] == 'T'):
                television = Television(fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
                self.__planes.append(television)
    
    def mostrar(self):
        long = len(self.__planes)
        for i in range(long):
            print(self.__planes[i])
    
    def mostrarTipoSegunPosicion(self,posicion):
        if(isinstance(self.__planes[posicion], Telefonia)):
            print(type(self.__planes[posicion]))
            print(self.__planes[posicion].get_nombre())
        else:
            if(isinstance(self.__planes[posicion], Television)):
                print(type(self.__planes[posicion]))
                print(self.__planes[posicion].get_nombre())
    
    def mostrarPorCoberturaGeografica(self,cobertura):
        long = len(self.__planes)
        contador = 0
        for i in range(long):
            if(self.__planes[i].get_cobertura() == cobertura):
                contador+=1
                print("Plan: ",self.__planes[i].get_nombre())
        
        print("La cantidad total de planes que corresponden a la cobertura ",cobertura,"son ",contador)
    
    def mostrarTodosPlanes(self):
        long = len(self.__planes)
        for i in range(long):
            self.__planes[i].mostrar()
            
    