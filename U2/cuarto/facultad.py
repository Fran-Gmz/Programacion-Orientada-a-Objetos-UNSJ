class Facultad:
    __codigo:set
    __nombre:str
    __direccion:str
    __localidad:str
    __telefono:str

    def __init__(self, codigo, nombre, direccion, localidad, telefono):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono

    def __str__(self):
        return 'codigo:{}, nombre:{}, direcciom:{}, localidad:{}, telefono:{}'.format(self.__codigo, self.__nombre, self.__direccion, self.__localidad, self.__telefono)
    
    
    def getCodigo (self):
        return self.__codigo
    
    def getNombre (self):
        return self.__nombre
    
    def getDireccion (self):
        return self.__direccion
    
    def getLocalidad (self):
        return self.__localidad
    
    def getTelefono (self):
        return self.__telefono

