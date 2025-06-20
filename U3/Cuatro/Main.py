from GestorPlan import GestorPlan
def menu(opcion):
    if opcion == 1:
        cantidad = lplanes.retornarLongitudLista()
        print("Ingrese una posicion entre 1 y " ,cantidad)
        posicion = input()
        lplanes.mostrarTipoSegunPosicion(int(posicion) - 1)
        
    elif opcion == 2:
        # cobertura = input("Ingrese cobertura geografica")
        lplanes.mostrarPorCoberturaGeografica("Regional")
    elif opcion == 4:
        lplanes.mostrarTodosPlanes()

if __name__ == '__main__':
    lplanes = GestorPlan()
    lplanes.leerCsv()
    lplanes.mostrar()
    
    print("------- MENU ----------")
    print("1- Mostrar tipo de plan ")
    print("2- Mostrar cantidad de planes por cobertura geografica")
    print("3- Mostrar nombres de compañias")
    print("4- Listar planes")
    print("5- Salir")
    opcion = 0
    while(opcion !=5):
        opcion = (int(input("Seleccione opcion: ")))
        menu(opcion)  
    