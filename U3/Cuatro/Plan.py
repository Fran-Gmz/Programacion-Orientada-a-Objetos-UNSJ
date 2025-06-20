class Plan:
    __nombreCompania : str
    __duracion : int
    __coberturaGeografica : str
    __precioBase : float
    
    def __init__(self,nombreCompania,duracion,coberturaGeografica,precioBase):
        self.__nombreCompania = nombreCompania
        self.__duracion = duracion
        self.__coberturaGeografica = coberturaGeografica
        self.__precioBase = precioBase
        
    
    def get_nombre(self):
        return self.__nombreCompania

    def get_duracion(self):
        return self.__duracion

    def get_cobertura(self):
        return self.__coberturaGeografica

    def get_precio_base(self):
        return self.__precioBase

    def __str__(self):
        return f"Plan {self.__nombreCompania}: Duración {self.__duracion} meses, Cobertura {self.__coberturaGeografica}, Precio base {self.__precioBase}"
    
    def calcularPrecioFinal(self):
        pass
    
    def mostrar(self):
        print("Nombre: ", self.get_nombre())
        print("Importe: ", self.calcularPrecioFinal())
        print("--------------------------------------------")