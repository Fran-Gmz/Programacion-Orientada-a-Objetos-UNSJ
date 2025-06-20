
import csv
class Biblioteca:
    __nombre:str
    __direccion:str
    __telefono:str
    __lista_Libros:list

    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__lista_Libros = []
    
    def __str__(self):
        s = 'nombre:{}, direccion:{}, telefono:{} \n'.format(self.__nombre, self.__direccion, self.__telefono)
        long = len(self.__lista_Libros)
        for i in range(long):
            s += str(self.__lista_Libros[i]) + ' \n '
        return s
    
    def agregarLibro (self, libro):
        self.__lista_Libros.append(libro)

    def getNombre (self):
        return self.__nombre
    
    def getDireccion (self):
        return self.__direccion
    
    def getTelefono (self):
        return self.__telefono
    
    def buscarLibroPorTitulo(self, titulo):
        i = 0
        long = len(self.__lista_Libros)
        encontrado = False
        posicion = None
        while i < long and encontrado == False:
            if titulo == self.__lista_Libros[i].getTitulo():
                encontrado = True
                posicion = i
            else:
                i += 1
        if encontrado == True:
            return posicion
        else:
            print('No se encontró el libro en {}'.format(self.__nombre))

    def eliminarLibro (self, posicion):
        self.__lista_Libros.pop(posicion)
        print('Libro eliminado.')

    def mostrarAutorGeneroDeUnLibro(self, posicion):
        autor = self.__lista_Libros[posicion].getAutor()
        genero = self.__lista_Libros[posicion].getGenero()
        print('autor:{}, genero:{}.'.format(autor, genero))