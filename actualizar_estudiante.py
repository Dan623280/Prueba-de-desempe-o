

# se importa la function de verificar estado, la lista de estudiantes, las functiones error entero , valor no valido y error estring
from function_r_estudiante import  verifi_Estado, Lista_estudiantes,error_entero, valor_no_valido, error_string

#-------------------------
# Actualizar
#-------------------------

#se crea la function actualizar
def Actualizar():

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
                
                    # se piden los valores para actualizar
                    elemento['Nombre'] = error_string("Coloque el Nombre")
                    elemento['Edad'] = error_entero("Coloque edad: ")
                    elemento['Curso'] = error_string("Coloque el Curso")
                    elemento['Estado'] = verifi_Estado()