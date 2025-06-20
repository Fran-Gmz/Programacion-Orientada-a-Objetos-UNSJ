from TarjetaSube import TarjetaSube
from GestorTarjetaSube import GestorTarjetaSube
def Test():
    TarjetaUno = TarjetaSube(20,101)
    TarjetaDos = TarjetaSube(-100,102)

    ManejadorTarjeta = GestorTarjetaSube()
    ManejadorTarjeta.agregarUnaTarjeta(TarjetaUno)
    ManejadorTarjeta.agregarUnaTarjeta(TarjetaDos)

    cantidad = ManejadorTarjeta.tarjetasNegativas()
    numero = ManejadorTarjeta.obtenerNumero(101)
    print (numero)
    

if __name__ == '__main__':
   Test()
