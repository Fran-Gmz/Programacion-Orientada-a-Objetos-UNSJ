class TarjetaSube:
    __saldo:int
    __numero:int

    def __init__(self, saldo=0, numero=0):
        self.__saldo = saldo
        self.__numero = numero

    def __str__(self):
        return 'numero:{}, saldo:{}'.format(str(self.__numero), str(self.__saldo))
  
    def cargarSaldo (self, importe:int):
        if  importe > 0:
            self.__saldo += importe
        else:
            print("Error al cargar saldo")

    def pagarPasaje (self, importe:int):
        if importe > -200:
            if self.__saldo >= importe:
                self.__saldo = self.__saldo - importe
                print('Nuevo Saldo:{}'.format(self.__saldo))
            else:
                print('Saldo insuficiente {}'.format(self.__saldo - importe))

    def getNumero (self):
        return self.__numero
    
    def getSaldo (self):
        return self.__saldo
        