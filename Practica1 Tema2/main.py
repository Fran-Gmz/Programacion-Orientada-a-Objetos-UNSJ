from gestorGastos import gestorGastos
from gestorMovilidades import gestorMovilidad

def test():
    manejadorMovilidad = gestorMovilidad()
    manejadorGastos = gestorGastos()

    manejadorMovilidad.testMovilidades()
    manejadorGastos.testGastos()

    print(manejadorMovilidad)
    print(manejadorGastos)


if __name__ == '__main__':
    test()