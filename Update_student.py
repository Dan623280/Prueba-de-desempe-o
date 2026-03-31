

# se importa la function de verificar estado, la student list, las functiones error entero , valor no valido y error estring
from function_r_student import  verifi_Estado, list_students,error_entero, valor_no_valido, error_string

#-------------------------
# update
#-------------------------

#se crea la function update
def update():

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
                
                    # se piden los valores para update
                    elemento['Name'] = error_string("Place the Name: ")
                    elemento['Age'] = error_entero("Place the Age: ")
                    elemento['Course'] = error_string("Place the Course: ")
                    elemento['Estado'] = verifi_Estado()