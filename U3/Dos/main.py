from gestorBiblioteca import GestorBiblioteca

def test():
    manejadorBiblioteca = GestorBiblioteca()
    manejadorBiblioteca.cargarBibliotecas()

    print('__________MENU___________')
    print('1.Agregar Libro')
    print('2.Eliminar Libro')
    print('3.Mostrar biblioteca, nombre del Autor y género.')
    print('4.Listar Libros')
    print('5.Salir')
    opcion = 4
    while opcion > 0 and opcion < 5:
        if opcion == 1:
            manejadorBiblioteca.agregarLibro()
        elif opcion == 2:
            manejadorBiblioteca.eliminarLibro()
            print(manejadorBiblioteca)
        elif opcion == 3:
            manejadorBiblioteca.mostrarBibliotecaAutorGeneroDeUnLibro()
        elif opcion == 4:
            manejadorBiblioteca.mostrarLibros()

if __name__ == '__main__':
    test()