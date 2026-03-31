
# importa las functiones de errores entero estring y valor no valido
from error import error_string, error_entero, valor_no_valido

# se importa la function de la lista de estudiantes
from lista_estudiantes import Lista_estudiantes

#---------------------------
# verificar nombre
#---------------------------

def verifi_Nombre():

    #crea un ciclo
    while True:

        #pide el nombre
        nombre = error_string("Colocar Nombre: ")

        #crea una lista para almacenar nombres
        lista_nombre = []

        #se crea un bucle para recorrer los elementos
        for elemento in Lista_estudiantes:

            # se añade los nombres a la lista
            lista_nombre.append(elemento['Nombre'])

        # si nombre esta en la lista
        if nombre in lista_nombre:

            # muestra mensaje de nombre ya exites
            print("----------------------")
            print("-- Nombre ya existe --")
            print("----------------------")

        # si nombre no esta en lista
        else:

            # retorna el nombre
            return nombre

#---------------------
# verificar estado        
#---------------------

def verifi_Estado():

    #crea un ciclo
    while True:

        #Mostrar menu
        print("")
        print("1. activo")
        print("2. inactivo")
        print("")

        #Pedir option
        option = error_entero("Colocar Estado: ")

        # option 1 activo
        if option == 1:

            #Retorna activo
            return "activo"
        
        # option 2 inactivo
        elif option == 2:

            #Retorna inactivo
            return "inactivo"
        
        #de lo contrario
        else:

            #imprime valor  no valido
            valor_no_valido()

#---------------------
# id      
#---------------------

# de vuel ve el id para registrar nuevo usuario
def id():

    # se crea una lista para almnacenar los id
    lista_id = []

    # se crea un bucle para recorrer los elementos
    for elemento in Lista_estudiantes:
        
        # se añade los id a la lista
        lista_id.append(elemento['id'])

    # varid trae el numero mas grande que tenga la lista si no hay elementos en la lista va ser igual a 0
    varid = max(lista_id, default=0)

    # retorna el valor mas 1
    return varid + 1
