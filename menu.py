# Importar function error entero
from error import error_entero


#-------------------------
# Menu
#-------------------------

def Menu():

    #Mostrar menu
    print("")
    print("1. Registrar nuevos estudiantes")
    print("2. Consultar la lista de estudiantes")
    print("3. Buscar un estudiante")
    print("4. Actualizar la información de un estudiante.")
    print("5. Eliminar estudiantes")
    print("6. Salir")
    print("")

    #Pedir option
    option = error_entero("Colocar option: ")

    #Retorna option
    return option
