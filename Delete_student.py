# Trae los data de la student list
from list_students import list_students

#importa la function de valor entero y valor no valido
from error import error_entero, valor_no_valido

#function patra Delete
def Delete():

    # se crea una list para almnacenar los id
    list_id = []

    #se crea un bucle para recorrer los elementos
    for elemento in list_students:

        # se añade los id a la list
        list_id.append(elemento['id'])

    #-------------------------------------------
    #se verifica si hay elementos en la list
    #-------------------------------------------

    # si no hay elementos
    if len(list_id) == 0:

        #se imprime un mensaje de error
        print("No Hay elementos en la list")

    # si hay elementos
    else:

        # pide el indice con validacion de error
        inidice = error_entero("insert indice del cliente: ") 

        # si el idice es mayor al numero ma grande de la list
        if inidice > max(list_id):

            #imprime el mensaje de valor no valido
            valor_no_valido()

        #si el indice no es mayor
        else:

            #se crea un bucle para recorrer los elementos
            for elemento in list_students:
            
                # se filtra por el indice
                if elemento['id'] == inidice:
                
                    # se muestra elemento a Delete
                    print(f"Indice = {elemento['id']}, Name = {elemento['Name']}, Age = {elemento['Age']}, Course = {elemento['Course']}, Estado = {elemento['Estado']}")
    
                    # se elimina
                    list_students.remove(elemento)
    
                    # se muestra mensaje informativo
                    print("")
                    print("Elemento eliminado correctamente")
                    print("")

    