from gestorCarrera import GestorCarrera
from gestorFacultad import GestorFacultad

def test():
    manejadorFacultad = GestorFacultad(10)
    manejadorCarreara = GestorCarrera (10)
    #a) Cargar los datos de las Carreras desde el archivoCarreras.csv.
    manejadorCarreara.test()

    #b) Cargar los datos de las Facultades desde del archivoFacultades.csv.
    manejadorFacultad.test()
  
    #c) Dado el Nombre de una Carrera, mostrar el nombre de la Facultad en la que se dicta.
    nombreCarrera='BioIngenieria'
    codigoFacultad = manejadorCarreara.buscarFacultadPorCarrera(nombreCarrera)
    print(manejadorFacultad.buscarFacultadPorCodigo(codigoFacultad))

    #d) Para todas las facultades calcular y mostrar la cantidad de carreras que se dictan en cada una de ellas.
    manejadorFacultad.mostrarCantidadCarreras(manejadorCarreara)

    # e) Dado el nombre de una Facultad, generar un listado ordenado alfabéticamente, quemuestre: nombre y duración de de las carreras que en ella se dictan. Para ello, el analista le solicita que en la clase que representa a las carreras, sobrecargue el operador __lt__.
    nombreFacultad = 'Facultad de ciencias Exactas Fisicas y Naturales'
    codigo = manejadorFacultad.buscarFacultadPorNombre(nombreFacultad)
    manejadorCarreara.mostrarDatosCarreras(codigo)
    
if __name__ == '__main__':
    test()