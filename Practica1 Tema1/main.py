# Gomez Francisco 45213346 E010-300
from gestorColectivo import gestorColectivo
from gestorTramo import gestorTramo

def test():
    num = 10
    manejadorColectivo = gestorColectivo(num)
    manejadorTramo = gestorTramo()

    manejadorColectivo.testColectivos()
    manejadorTramo.testTramos()
    print("1. informe De los Tramos Por Dni")
    print("2. mostrar Total Km y Gasto")
    print("3. listar Datos Por Distancia")
    menu = int(int(input("Ingresa Opcion: ")))
    while menu > 0 and menu < 4:
        if menu == 1:
            #inciso a
            dni = input("IngresaDni de chofer: ")
            manejadorColectivo.informeDelosTramosPorDni(dni, manejadorTramo)
        elif menu == 2:
            #inciso b
            manejadorColectivo.motrarTotalKmyGastos(manejadorTramo)

        elif menu == 3:
            #inciso c
            distancia=int(input('ingresar distancia: '))
            manejadorTramo.listarDatosPorDistancia(distancia)
        print("1. informe De los Tramos Por Dni")
        print("2. mostrar Total Km y Gasto")
        print("3. listar Datos Por Distancia")
        menu = int(int(input("Ingresa Opcion ")))

if __name__ == '__main__':
    test()

 #c. Dada una distancia recorrida, listar los datos (ciudad origen, ciudad des no y
    #patente del colec vo) de los tramos en los que los km recorridos superan la
    #distancia dada. Regla de negocio: para resolver este úl mo punto, el analista le
    #solicita que sobrecargue el operador relacional correspondiente.