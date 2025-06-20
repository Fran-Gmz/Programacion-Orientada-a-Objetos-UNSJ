from gestorAtencion import gestorAtencion
from gestorPacientes import gestorPaciente

def test():
    manejadorPaciente = gestorPaciente()
    manejadorAtencion = gestorAtencion(20)

    manejadorPaciente.testPacientes()
    manejadorAtencion.testAtenciones()

    print('Menu1')
    print('1. informar las atenciones realizadas en dicha fecha y el importe que debe disponer la UNSJ en esa fecha.')
    print('2. informar Nombre y apellido, y cantidad de atenciones que tuvo.')
    print('3. Listar nombre, apellido de los pacientes que no tuvieron ninguna atención')
    print('4.Listar los Pacientes, ordenados por Apellido, de menor a mayor por unidad')
    print('5. Salir')
    menu = int(input('Elige opcion: '))
     
    while menu > 0 and menu < 5:
        if menu == 1:
            fecha=input('ingresa fecha: ')
            manejadorAtencion.informeDeFecha(fecha)
        elif menu == 2:
            dni= input('ingresa dni: ')
            manejadorPaciente.BuscarNombreApellido(dni, manejadorAtencion)
        elif menu == 3:
            manejadorPaciente.listarPacientesSinAtencion(manejadorAtencion)
        elif menu == 4:
            manejadorPaciente.listarPacientesPorApellido()

        print('\n 1. informar las atenciones realizadas en dicha fecha y el importe que debe disponer la UNSJ en esa fecha.')
        print('2. informar Nombre y apellido, y cantidad de atenciones que tuvo.')
        print('3. Listar nombre, apellido de los pacientes que no tuvieron ninguna atención')
        print('4.Listar los Pacientes, ordenados por Apellido, de menor a mayor por unidad')
        print('5. Salir')
        menu = int(input('Elige opcion: '))
     

if __name__ == '__main__':
    test()