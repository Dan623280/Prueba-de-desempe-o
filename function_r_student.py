
# importa las functiones de errores entero estring y valor no valido
from error import error_string, error_entero, valor_no_valido

# se importa la function de la student list
from list_students import list_students

#---------------------------
# verificar name
#---------------------------

def verifi_Nombre():

    #crea un ciclo
    while True:

        #pide el name
        name = error_string("insert Name: ")

        #crea una list para almacenar names
        list_name = []

        #se crea un bucle para recorrer los elementos
        for elemento in list_students:

            # se añade los names a la list
            list_name.append(elemento['Name'])

        # si name esta en la list
        if name in list_name:

            # muestra mensaje de name ya exites
            print("----------------------")
            print("-- Name ya existe --")
            print("----------------------")

        # si name no esta en list
        else:

            # retorna el name
            return name

#---------------------
# verificar estado        
#---------------------

def verifi_Estado():

    #crea un ciclo
    while True:

        #Mostrar menu
        print("")
        print("1. active")
        print("2. inactive")
        print("")

        #Pedir option
        option = error_entero("insert Estado: ")

        # option 1 active
        if option == 1:

            #Retorna active
            return "active"
        
        # option 2 inactive
        elif option == 2:

            #Retorna inactive
            return "inactive"
        
        #de lo contrario
        else:

            #imprime valor  no valido
            valor_no_valido()

#---------------------
# id      
#---------------------

# de vuel ve el id para register nuevo usuario
def id():

    # se crea una list para almnacenar los id
    list_id = []

    # se crea un bucle para recorrer los elementos
    for elemento in list_students:
        
        # se añade los id a la list
        list_id.append(elemento['id'])

    # varid trae el numero mas grande que tenga la list si no hay elementos en la list va ser igual a 0
    varid = max(list_id, default=0)

    # retorna el valor mas 1
    return varid + 1
