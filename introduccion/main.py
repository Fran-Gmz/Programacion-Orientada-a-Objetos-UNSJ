from gestorPersona import GestorPersona
from persona import Persona

if __name__ == '__main__':
# Creamos el Gestor Persona
    listaEmpleados = GestorPersona()

# Creamos objetos de la clase Persona
    personaUno = Persona(34400954, 'Morena', 'Diaz', 900000.50)
    personaDos =  Persona(43049132, 'Alfredo', 'Mateo', 745000.50)
    personaTres = Persona(23058234, 'Luis', 'Capone', 1200000.50)
    personaCuatro = Persona(26954234, 'Norman', 'Apache', 920000.00)

# Agregamos los objetos de la clase Persona a la listaEmpleados de la clase Gestor Persona
    listaEmpleados.agregarPersona(personaUno)
    listaEmpleados.agregarPersona(personaDos)
    listaEmpleados.agregarPersona(personaTres)
    listaEmpleados.agregarPersona(personaCuatro)

# Mostramos los bojetos de la listaEmpleados con __str__
    print('Lista de Empleados')
    print(listaEmpleados)

# Mostrar nombre, dni , sueldo del empleado de mayor sueldo
    print('Empleado mayor sueldo')
    empleadoMayor = listaEmpleados.empleadoMayorSueldo()
    print (empleadoMayor)

# Calcular Sueldo Promedio 
    print('\n Sueldo Promedio')
    sueldoPromedio = listaEmpleados.sueldoPromedio()
    print(sueldoPromedio)

# Mostrar empleados que tengan sueldo mayor o igual al sueldo promedio
    print('\n Empleados mayor igual al sueldo promedio ')
    empleadosSueldoPromedio = listaEmpleados.mayorIgualSueldoPromedio(sueldoPromedio)
    print(empleadosSueldoPromedio)

# Ejemplo de como Mostrar Datos de un objeto con __Str__
    print('Datos de un objeto')
    print('{}'.format(str(personaUno)))


   
