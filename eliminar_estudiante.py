# Trae los datos de la lista de estudiantes
from lista_estudiantes import Lista_estudiantes

#importa la function de valor entero y valor no valido
from error import error_entero, valor_no_valido

#function patra eliminar
def Eliminar():

    # se crea una lista para almnacenar los id
    lista_id = []

    #se crea un bucle para recorrer los elementos
    for elemento in Lista_estudiantes:

        # se añade los id a la lista
        lista_id.append(elemento['id'])

    #-------------------------------------------
    #se verifica si hay elementos en la lista
    #-------------------------------------------

    # si no hay elementos
    if len(lista_id) == 0:

        #se imprime un mensaje de error
        print("No Hay elementos en la Lista")

    # si hay elementos
    else:

        # pide el indice con validacion de error
        inidice = error_entero("Colocar indice del cliente: ") 

        # si el idice es mayor al numero ma grande de la lista
        if inidice > max(lista_id):

            #imprime el mensaje de valor no valido
            valor_no_valido()

        #si el indice no es mayor
        else:

            #se crea un bucle para recorrer los elementos
            for elemento in Lista_estudiantes:
            
                # se filtra por el indice
                if elemento['id'] == inidice:
                
                    # se muestra elemento a eliminar
                    print(f"Indice = {elemento['id']}, Nombre = {elemento['Nombre']}, Edad = {elemento['Edad']}, Curso = {elemento['Curso']}, Estado = {elemento['Estado']}")
    
                    # se elimina
                    Lista_estudiantes.remove(elemento)
    
                    # se muestra mensaje informativo
                    print("")
                    print("Elemento eliminado correctamente")
                    print("")

    