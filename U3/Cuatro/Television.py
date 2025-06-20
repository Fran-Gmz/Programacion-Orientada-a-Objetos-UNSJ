from Plan import Plan
class Television(Plan):
    __cantidadCanalesNacionales: int
    __cantidadCanalesInternacionales : int
    
    def __init__(self, nombreCompania, duracion, coberturaGeografica, precioBase,cantidadCanalesNacionales,cantidadCanalesInternacionales):
        super().__init__(nombreCompania, duracion, coberturaGeografica, precioBase)
        self.__cantidadCanalesNacionales = cantidadCanalesNacionales
        self.__cantidadCanalesInternacionales = cantidadCanalesInternacionales
        
    def getcantidadCanalesNacionales(self):
        return self.__cantidadCanalesNacionales
    
    def getcantidadCanalesInternacionales(self):
        return self.__cantidadCanalesInternacionales
    
    def __str__(self):
        return f"{super().__str__()}, Canales nacionales: {self.__cantidadCanalesNacionales}, Canales internacionales: {self.__cantidadCanalesInternacionales}"
    
    def calcularPrecioFinal(self):
        importe = 0
        #Calcular correctamente el porcentaje
        importe += int(super().get_precio_base()) * 15 
        return importe