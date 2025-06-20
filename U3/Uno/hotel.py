from habitacion import Habitacion
class Hotel:
    __nombre:str
    __direcion:str
    __telefono:str
    __habitaciones:list

    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direcion = direccion
        self.__telefono = telefono
        self.__habitaciones = []
    
    def __str__(self):
        s = '{}, {}, {} \n '.format(self.__nombre, self.__direcion, self.__telefono)
        long = len(self.__habitaciones)
        for i in range(long):
            s += str(self.__habitaciones[i]) + ' \n '
        return s
    

    def agregarHabitacion (self, num, piso, tipo, precio, dispo):
        unaHabitacion = Habitacion(num, piso, tipo, precio, dispo)
        self.__habitaciones.append(unaHabitacion)

    def getNombre(self):
        return self.__nombre
    
    def getDireciion(self):
        return self.__direcion
    
    def getTelefono(self):
        return self.__telefono
    
    def getHabitaciones(self):
        return self.__habitaciones
    
    def buscarHabitacionPorNumero(self, numero):
        i = 0
        long = len(self.__habitaciones)
        encontrado = False
        posicion = None
        while i < long and encontrado == False:
            if numero == self.__habitaciones[i].getNumero():
                encontrado = True
                posicion = i
            else:
                i += 1
        if encontrado == True:
            return posicion
        else:
            print('Habitacion no encontrada')
         
    def reservarHabitacionDisponible(self, i):
        disponible = self.__habitaciones[i].getDisponibilidad()
        if disponible == True:
            self.__habitaciones[i].setDisponibilidad(False)
            print('Habitacion reservada')
        else:
            print('La habitacion no esta disponible')


    def informeDeDisponibilidad(self, i):
        disponible = self.__habitaciones[i].getDisponibilidad()
        if disponible == True:
            print('La habitacion estba libre')
        else:
            self.__habitaciones[i].setDisponibilidad(False)
            print('Habitacion Reservada')
    
    def mostrarNumeroYpisoDeLasHabitacionesDelTipo(self, tipo):
        long = len(self.__habitaciones)
        print('Habitaciones del tipo {}'.format(tipo))
        for i in range(long):
            if tipo == self.__habitaciones[i].getTipoHabitacion():
                numero = self.__habitaciones[i].getNumero()
                piso = self.__habitaciones[i].getPiso()
                print('numero: {}, piso:{}'.format(numero, piso))

    def mostrarHabitacionesLibresPorPiso(self):
        piso = 1
        cantidad = 0
        long = len(self.__habitaciones)
        for i in range (long):
            if piso == self.__habitaciones[i].getPiso():
                if self.__habitaciones[i].getDisponibilidad() == True:
                    cantidad += 1
            else:
                print('En el piso {}, hay {} habitaciones libres'.format(piso, cantidad))
                piso += 1 
                cantidad = 1
        print('En el piso {}, hay {} habitaciones libres'.format(piso, cantidad))

    def MostrarDatosParaCadaTipoHabitación(self):
        long = len(self.__habitaciones)
        for i in range(long):
            tipo = self.__habitaciones[i].getTipoHabitacion()
            numero = self.__habitaciones[i].getNumero()
            piso =  self.__habitaciones[i].getPiso()
            precio = self.__habitaciones[i].getPrecioNoche()
            dispo = self.__habitaciones[i].getDisponibilidad()
            print('Tipo de habitacion: {}'.format(tipo))
            print('Numero             Piso                Precio            Disponibilida')
            print('{}                 {}                  {}                {}'.format(numero,piso,precio,dispo))