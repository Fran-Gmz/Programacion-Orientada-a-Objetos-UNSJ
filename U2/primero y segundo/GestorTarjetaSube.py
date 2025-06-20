from TarjetaSube import TarjetaSube 
class GestorTarjetaSube:
    __lista:list

    def __init__(self):
        self.__lista = []

    def __str__(self):
        s = ''
        for indice in range(len(self.__lista)):
            s += str(self.__lista[indice]) + '\n'
        return s

    def agregarUnaTarjeta(self, Tarjeta):
        if isinstance(Tarjeta, TarjetaSube):
            self.__lista.append(Tarjeta)
        else:
            print('No es objeto de Tarjeta Sube')
            
    def tarjetasNegativas (self):
        contador = 0
        for indice in range(len(self.__lista)):
            if self.__lista[indice].getSaldo() < 0:
                contador += 1
        return contador


    def obtenerNumero (self, numero):
        indice = 0
        encontrado = False
        posicion = None
        long = len(self.__lista)
        while indice < len(self.__lista) and encontrado == False:
            if numero == self.__lista[indice].getNumero():
                encontrado = True
                posicion = indice
            else:
                indice += 1
        if encontrado == True:
            return self.__lista[posicion].getNumero()
        else:
            print('Numero no encontrado')
