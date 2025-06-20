class Habitacion:
    __numero:int
    __piso:int
    __tipoHabitacion:str
    __precioNoche:float
    __diponibilidad:bool

    def __init__(self, numero, piso, tipoHabitacion, precioNoche, disponibilidad):
        self.__numero = numero
        self.__piso = piso
        self.__tipoHabitacion = tipoHabitacion
        self.__precioNoche = precioNoche
        self.__diponibilidad = disponibilidad
    
    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.__numero, self.__piso, self.__tipoHabitacion, self.__precioNoche, self.__diponibilidad)
    
    def getNumero(self):
        return self.__numero
    
    def getPiso(self):
        return self.__piso
    
    def getTipoHabitacion (self):
        return self.__tipoHabitacion
    
    def getPrecioNoche(self):
        return self.__precioNoche
    
    def getDisponibilidad(self):
        return self.__diponibilidad

    def setDisponibilidad(self, dispo):
        self.__diponibilidad = dispo