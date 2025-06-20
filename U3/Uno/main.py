from gestorHotel import GestorHotel

def test():
    manejadorHotel = GestorHotel()
    manejadorHotel.testArchivo()
    print(manejadorHotel)
    print('___________Menu_____________')
    print('1.Agrgar Habitaciones a un hotel')
    print('2.Reservar Habitacion')
    print('3.Liberar una habitacion')
    print('4.Dado un tipo de habitación  mostrar número y piso de las habitacionesde ese tipo.')
    print('5.Mostrar la cantidad de habitaciones libres por piso.')
    print('6.Para cada tipo de habitación mostrar sus datos')
    opcion = int(input('Ingresa Opcion: '))
    menu = True
    if opcion>0 and opcion<7:
        nombre = 'Hotel Paraíso Tropical'
        posicion = manejadorHotel.buscarHotelPorNombre(nombre)
    while opcion>0 and opcion<8:
        if opcion == 1:
            manejadorHotel.agregarHabitaciones(posicion)
        elif opcion == 2:
            manejadorHotel.reservarHabitacion(posicion)
        elif opcion == 3:
            manejadorHotel.liberarHabitacion(posicion)
        elif opcion == 4:
           manejadorHotel.mostrarNumeroYpisoDeLasHabitaciones(posicion)
        elif opcion == 5:
           manejadorHotel.cantidadDeHabitacionesLibresPorPiso(posicion)
        elif opcion == 6:
           manejadorHotel.ParaCadaTipoHabitaciónMostrarDatos(posicion)
        elif opcion == 7:
            nombre =  input('Ingresa nombre del hotel: ')
            posicion = manejadorHotel.buscarHotelPorNombre(nombre)
        else:
            menu = False
            print('Saliste')
        if menu == True:
            print('___________Menu_____________')
            print('1.Agrgar Habitaciones a un hotel')
            print('2.Reservar Habitacion')
            print('3.Liberar una habitacion')
            print('4.Dado un tipo de habitación  mostrar número y piso de las habitacionesde ese tipo.')
            print('5.Mostrar la cantidad de habitaciones libres por piso.')
            print('6.Para cada tipo de habitación mostrar sus datos')
            print('7.Cambiar de Hotel')
            print('8.Salir')
            opcion = int(input('Ingresa Opcion: '))
            

if __name__ == '__main__':
    test()
