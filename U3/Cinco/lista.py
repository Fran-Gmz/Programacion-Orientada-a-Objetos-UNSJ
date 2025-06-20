
import json
from nodo import Nodo
from medio import Medio
from television import Television
from radio import Radio
from prensa import Prensa
from programa import Programa

class Lista:
    __comienzo:Nodo

    def __init__(self):
        self.__comienzo = None
    
    def agregarMedio (self, medio):
        nodo = Nodo(medio)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
    
    def listarDatosMedios (self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()

    def Cargar_JSON (self):
        