from Plan import Plan
class Telefonia(Plan):
    __tipoLlamada : str
    __cantidadMinutos : int
    
    def __init__(self, nombreCompania, duracion, coberturaGeografica, precioBase,tipoLlamada,cantidadMinutos):
        super().__init__(nombreCompania, duracion, coberturaGeografica, precioBase)
        
        self.__tipoLlamada = tipoLlamada
        self.__cantidadMinutos = cantidadMinutos
        
    def getTipoLlamada(self):
        return self.__tipoLlamada
    def getCantidadMinutos(self):
        return self.__cantidadMinutos
    
    def __str__(self):
        return f"{super().__str__()}, Tipo llamada: {self.__tipoLlamada}, Cantidad de minutos: {self.__cantidadMinutos}"
    
    def calcularPrecioFinal(self):
        importe = 0
        if(super().get_cobertura() == "Nacional e Internacional"):
            #Calcular correctamente el porcentaje
            importe += int(super().get_precio_base()) * 20 
        else:
            if(self.__tipoLlamada == "locales"):
                #Calcular correctamente el porcentaje
                importe += int(super().get_precio_base()) * 7 
        return importe