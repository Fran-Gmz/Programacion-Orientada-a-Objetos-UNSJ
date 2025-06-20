class accidentes:
    __lista:list
    def __init__(self):
        self.__lista = [[0]*3 for i in range(4) ]

    def cargar(self, mes, departamento, cantidad):
        self.__lista[mes -1][departamento -1] = cantidad