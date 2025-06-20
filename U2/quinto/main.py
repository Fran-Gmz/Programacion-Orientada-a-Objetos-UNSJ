from gestorBeca import GestorBeca
from gestorBeneficiario import GestorBeneficiario

def test():
    manejadorBecas = GestorBeca(5)
    manejadorBeneficiario = GestorBeneficiario(10)

    manejadorBecas.test()
    manejadorBeneficiario.test()
  
    #a. Leer por teclado un tipo de Beca, e informar los beneficiarios de dicha beca y el importe total que debe disponer la Secretaría para el pago de dicha Beca.
    #nombreBeca = input("Ingresa Nombre: ")
    #manejadorBecas.beneficiariosYimporteTotal(nombreBeca, manejadorBeneficiario)

    #b. Leer por teclado un dni, informar si el beneficiario tiene más de una beca, mostrando nombre y apellido.
    #dni = input('Ingresa dni: ')
    #manejadorBeneficiario.masDeUnaBeca(dni)

    #c. Listar los beneficiarios, ordenados de mayor a menor por Facultad. Regla de negocio: para resolver este último punto, el analista le solicita que sobrecargue el operador “>”.
    #smanejadorBeneficiario.listarBeneficiarios()

    #d. Listar nombre, apellido y promedio de los estudiantes, que poseyendo un promedio mayor que 8, no poseen beca de ayuda económica.
    


if __name__ == '__main__':
    test()