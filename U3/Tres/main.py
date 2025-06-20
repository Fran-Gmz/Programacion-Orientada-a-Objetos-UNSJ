from gestorEmpleado import GestorEmpleado
from gestorMatricula import GestorMatricula
from gestorPrograma import GestorPrograma

def test ():
    manejadorEmepleado = GestorEmpleado()
    manejadorPrograma = GestorPrograma()
    manejadorMatricula = GestorMatricula()

    manejadorEmepleado.cargarArchivo()
    manejadorPrograma.cargarArchivo()
    manejadorMatricula.cargarArchivo(manejadorEmepleado, manejadorPrograma)

    print('---------menu---------')
    print('1. Dado el Id del empleado, informe la duración de todos los programas de capacitación en los que está matriculado.')
    print('2.Dado el nombre de un programa de capacitación, muestre el/los empleados matriculados en el mismo.')
    print('3. Informar aquellos Empleados que no han sido matriculados en ningún programa decapacitación.')
    print('4.salir')

    opcion = int(input('Ingresa opcion: '))
    preguntas = True

    while opcion > 0 and opcion < 5:
        if opcion == 1:
            manejadorMatricula.informeDeLosProgramasMatriculado()
        elif opcion == 2:
            manejadorMatricula.mostrarEmpleadosMatriculadosEnUnPrograma()
        elif opcion == 3:
            manejadorMatricula.informarEmpleadosNoMatriculasdos()
        else:
            preguntas = False
            print('Saliste')
        if preguntas == True:
            print('---------menu---------')
            print('1. Dado el Id del empleado, informe la duración de todos los programas de capacitación en los que está matriculado.')
            print('2.Dado el nombre de un programa de capacitación, muestre el/los empleados matriculados en el mismo.')
            print('3. Informar aquellos Empleados que no han sido matriculados en ningún programa decapacitación.')
            print('4.salir')
            opcion = int(input('Ingresa opcion: '))

if __name__ == '__main__':
    test()
