class Beneficiario:
    __dni:str
    __nombre:str
    __apellido:str
    __carrera:str
    __facultad:str
    __año:str
    __promedio:float
    __idBeca:str

    def __init__(self, dni, nombre, apellido, carrera, facultad, año, promedio, idbeca):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__carrera = carrera
        self.__facultad = facultad
        self.__año = año
        self.__promedio = promedio
        self.__idBeca = idbeca

    def __str__(self):
        return '{},{},{},{},{},{},{},{}'.format(self.__dni, self.__nombre, self.__apellido, self.__carrera, self.__facultad, self.__año, self.__promedio, self.__idBeca)
    
    def __gt__(self, otroBeneficiario):
        return self.__facultad > otroBeneficiario.__facultad
    
    def getDni (self):
        return self.__dni
    
    def getNombre (self):
        return self.__nombre
    
    def getApellido (self):
        return self.__apellido
    
    def getCarrera (self):
        return self.__carrera
    
    def getFacultad (self):
        return self.__facultad
    
    def getAño (self):
        return self.__año
    
    def getPromedio (self):
        return self.__promedio
    
    def getIdbeca (self):
        return self.__idBeca
    
    