class GestorPersona (object):
    __lista:list

    def __init__(self):
        self.__lista = []

    def __str__(self):
        i = 0 
        s = ''
        for i in range(len(self.__lista)):
            s += str(self.__lista[i]) + '\n'
        return s
    
    def agregarPersona (self, persona):
        self.__lista.append(persona)

    def empleadoMayorSueldo (self):
        sueldo = 0
        for i in range(len(self.__lista)):
            if sueldo <= self.__lista[i].getSueldo():
                sueldo = self.__lista[i].getSueldo()
                persona = i

        datosEmpleado = 'nombre:{},apellido:{},sueldo:{}'.format(self.__lista[persona].getNombre(), self.__lista[persona].getApellido(), str(self.__lista[persona].getSueldo()))

        return datosEmpleado
    
    def sueldoPromedio (self):
        sumador = 0
        for i in range(len(self.__lista)):
            sumador += self.__lista[i].getSueldo()
        sueldoPromedio = sumador / len(self.__lista)
        return sueldoPromedio

    def mayorIgualSueldoPromedio(self, sueldo):
        empleados = ''
        for i in range(len(self.__lista)):
            if sueldo <= self.__lista[i].getSueldo():
                empleados +=  str(self.__lista[i]) + '\n'

        return empleados