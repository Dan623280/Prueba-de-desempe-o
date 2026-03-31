
# function filter contiene las functiones para hacer correcta la busqueda 
from function_filter import Menu_filter, Indice, Nombre, Edad, Curso, Estado, valor_no_valido

# se importa la function de la lista de estudiantes
from lista_estudiantes import Lista_estudiantes

#---------------------------
# Cargar
#---------------------------

# function para buscar
def Buscar():
    
    # se crea una lista para almnacenar los id
    lista_id = []

    #se crea un bucle para recorrer los elementos
    for elemento in Lista_estudiantes:

        # se añade los id a la lista
        lista_id.append(elemento['id'])
    
    #-------------------------------------------
    #se verifica si hay elementos en la lista
    #----------------------------------------

    # si no hay elementos
    if len(lista_id) == 0:

        #se imprime un mensaje de error        
        print("No Hay elementos en la Lista")

    # si hay elementos
    else:

        #Pedir option
        option = Menu_filter()

        # option 1  Devuelve los datos segun el indice
        if option == 1:

            #function para Buscar indice
            Indice(lista_id)

        # option 2  Devuelve los datos segun el Nombre
        elif option == 2:

            #function para Buscar Nombre
            Nombre()

        # option 3 Devuelve los datos segun la edad
        elif option == 3:

            #function para Buscar edad
            Edad()

        # option 4  Devuelve los datos segun el Curso
        elif option == 4:

            #function para Buscar curso
            Curso()

        # option 2  Devuelve los datos segun el Estado
        elif option == 5:

            #function para Buscar estado
            Estado()

        # cunado el usuario ingresa un valor no valido
        else:

            #imprime valor  no valido
            valor_no_valido()