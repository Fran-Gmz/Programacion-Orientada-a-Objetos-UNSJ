from accidentes import accidentes
from departamentos import Departamento
from gestorDepartamentos import GestorDepartamentos

def test():
    gestorDpto = GestorDepartamentos()
    gestorDpto.cargar()
    
    #a. Dado un numero de mes, mostrar para cada uno de los Departamentosnombre del departamento y el total de accidentes ocurridos en el mes dado.
    mes = 1
    gestorDpto.mostrarAccidentesPorMes(mes)




    #b. Dado un mes, mostrar nombre de departamento y cantidad de accidentes, para el departamento que tuvo la mayor cantidad de accidentes.
    #c. Dado el nombre de un departamento indicar la cantidad total de accidentes ocurridos el año anterior.
    #d. Mostrar los datos registrados con el siguiente formato. La fila “TOTAL” se debe mostrar el total de accidentes del mes."""


if __name__ == '__main__':
    test()