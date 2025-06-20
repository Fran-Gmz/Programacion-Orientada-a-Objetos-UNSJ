from biblioteca import Biblioteca
from libro import Libro
import csv
class GestorBiblioteca():
    __bibliotecas:list

    def __init__(self):
        self.__bibliotecas = []
    
    def __str__(self):
        s = ''
        long = len(self.__bibliotecas)
        for i in range(long):
            s += str(self.__bibliotecas[i]) + ' \n '
        return s

    def agregarBiblioteca(self, unaBiblioteca):
        self.__bibliotecas.append(unaBiblioteca)

    def cargarBibliotecas (self):
        archivo = open('Biblioteca.csv')
        reader = csv.reader(archivo, delimiter=';')
        i = 0
        for fila in reader:
            if len(fila) == 3:
                i += 1
                nombre = fila[0]
                direccion = fila[1]
                telefono = fila[2]
                unaBiblioteca = Biblioteca(nombre, direccion, telefono)
                self.agregarBiblioteca(unaBiblioteca)
            else:
                titulo = fila[0]
                autor = fila[1]
                isbn = fila[2]
                genero = fila[3]
                unLibro = Libro(titulo, autor, isbn, genero)
                self.__bibliotecas[i - 1].agregarLibro(unLibro)
        archivo.close()

    def buscarBiblioteca (self, nombre):
        i = 0
        long = len(self.__bibliotecas)
        encontrado = False
        posicion = None
        while i < long and encontrado == False:
            if nombre == self.__bibliotecas[i].getNombre():
                encontrado = True
                posicion = i
            else:
                i += 1
        if encontrado == True:
            return posicion
        else:
            print('Biblioteca no encontrada')
        
    def agregarLibro(self):
        nombreBiblioteca = input('Ingresa nombre de la biblioteca a agregar libro: ')
        posicion = self.buscarBiblioteca(nombreBiblioteca)
        if posicion != None:
            titulo = input('Ingresa titulo del libro: ')
            autor = input('Ingresar autor del libro: ')
            isbn = input('Ingresar isbn del libro: ')
            genero = input('Ingresar genero del libro: ')
            unLibro = Libro(titulo, autor, isbn, genero)
            self.__bibliotecas[posicion].agregarLibro(unLibro)
        
    def eliminarLibro(self):
        nombreBiblioteca = input('Ingresa nombre de la biblioteca a eliminar libro: ')
        posicion = self.buscarBiblioteca(nombreBiblioteca)
        if posicion != None:
            titulo = input('Ingresa el titulo del libro a eleminar')
            libro = self.__bibliotecas[posicion].buscarLibroPorTitulo(titulo)
            if libro != None:
                self.__bibliotecas[posicion].eliminarLibro(libro)
    
    def mostrarBibliotecaAutorGeneroDeUnLibro(self):
        titulo = input('Ingresar titulo: ')
        long = len(self.__bibliotecas)
        for i in range(long):
            posicion = self.__bibliotecas[i].buscarLibroPorTitulo(titulo)
            if posicion != None:
                nombreBiblioteca = self.__bibliotecas[i].getNombre()
                print('Se encontro en {}'.format(nombreBiblioteca))
                self.__bibliotecas[i].mostrarAutorGeneroDeUnLibro(posicion)
    
    def mostrarLibros(self):
        nombre = input('Ingresa el nombre: ')
        posicion = self.buscarBiblioteca(nombre)
        if posicion != None:
            print(self.__bibliotecas[posicion])