from hotel import Hotel
import csv 

class GestorHotel:
    __hoteles:list

    def __init__(self):
       self.__hoteles = []

    def __str__(self):
        s = ''
        long = len(self.__hoteles)
        for i in range(long):
            s += str(self.__hoteles[i]) + ' \n '
        return s
    
    def agregarHotel (self, hotel):
       self.__hoteles.append(hotel)

    def testArchivo (self):
        i = 0
        archivo = open('Hoteles.csv')
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            if len(fila) == 3:
                unHotel = Hotel(fila[0], fila[1], fila[2])
                self.agregarHotel(unHotel)
                i += 1
            else:
                numero = int(fila[0])
                piso = int(fila[1])
                tipoHabitacion = fila[2]
                precioNoche = float(fila[3])
                disponibilidad = bool(fila[4])
                self.__hoteles[i - 1].agregarHabitacion(numero,piso,tipoHabitacion, precioNoche, disponibilidad)
        archivo.close()

    def buscarHotelPorNombre (self, nombre):
        i = 0
        long = len(self.__hoteles)
        encontrado = False
        posicion = None
        while i < long and encontrado == False:
            if nombre == self.__hoteles[i].getNombre():
                encontrado = True
                posicion = i
            else:
                i += 1
        if encontrado == True:
            return posicion
        else:
            print('No se encontro hotel')
    
    def agregarHabitaciones(self, posicion):
        i = 0
        cantidad = int(input('Cuantas habitaciones desea agregar: '))
        while i < cantidad:
            numero = int(input('Ingrese numero: '))
            piso = int(input('Ingrese el piso: '))
            tipo = input('Ingrese el tipo: ')
            precioNoche = float(input('Ingrese Precio x noche: '))
            disponibilidad = True
            self.__hoteles[posicion].agregarHabitacion(numero, piso, tipo, precioNoche, disponibilidad)
            i += 1

    def reservarHabitacion(self, posicion):
        numero = int(input('Ingresa numero de habitacion: '))
        i = self.__hoteles[posicion].buscarHabitacionPorNumero(numero)
        if i != None:
            self.__hoteles[posicion].reservarHabitacionDisponible(i)
        
    def liberarHabitacion(self, posicion):
        numero = int(input('Ingresa numero de habitacion: '))
        i = self.__hoteles[posicion].buscarHabitacionPorNumero(numero)
        if i!= None:
            ocupada = self.__hoteles[posicion].informeDeDisponibilidad(i)
    
    def mostrarNumeroYpisoDeLasHabitaciones(self, posicion):
        tipo = input('Ingresa tipo de habitacion: ')
        self.__hoteles[posicion].mostrarNumeroYpisoDeLasHabitacionesDelTipo(tipo)

    def cantidadDeHabitacionesLibresPorPiso(self, posicion):
        self.__hoteles[posicion].mostrarHabitacionesLibresPorPiso()
    
    def ParaCadaTipoHabitaciónMostrarDatos(self, posicion):
        self.__hoteles[posicion].MostrarDatosParaCadaTipoHabitación()