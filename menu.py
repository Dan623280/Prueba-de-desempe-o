# Importar function error entero
from error import error_entero


#-------------------------
# Menu
#-------------------------

def Menu():

    #Mostrar menu
    print("")
    print("1. Register new students")
    print("2. Consult student list")
    print("3. Look for student")
    print("4. update la información de un student.")
    print("5. Delete students")
    print("6. go out")
    print("")

    #Pedir option
    option = error_entero("insert option: ")

    #Retorna option
    return option
