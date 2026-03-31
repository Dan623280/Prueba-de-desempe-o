
# function filter contiene las functiones para hacer correcta la busqueda 
from function_filter import Menu_filter, Indice, Name, Age, Course, Estado, valor_no_valido

# se importa la function de la student list
from list_students import list_students

#---------------------------
# Cargar
#---------------------------

# function para Look_for
def Look_for():
    
    # se crea una list para almnacenar los id
    list_id = []

    #se crea un bucle para recorrer los elementos
    for elemento in list_students:

        # se añade los id a la list
        list_id.append(elemento['id'])
    
    #-------------------------------------------
    #se verifica si hay elementos en la list
    #----------------------------------------

    # si no hay elementos
    if len(list_id) == 0:

        #se imprime un mensaje de error        
        print("No Hay elementos en la list")

    # si hay elementos
    else:

        #Pedir option
        option = Menu_filter()

        # option 1  Devuelve los data segun el indice
        if option == 1:

            #function para Look_for indice
            Indice(list_id)

        # option 2  Devuelve los data segun el Name
        elif option == 2:

            #function para Look_for Name
            Name()

        # option 3 Devuelve los data segun la Age
        elif option == 3:

            #function para Look_for Age
            Age()

        # option 4  Devuelve los data segun el Course
        elif option == 4:

            #function para Look_for course
            Course()

        # option 2  Devuelve los data segun el Estado
        elif option == 5:

            #function para Look_for estado
            Estado()

        # cunado el usuario ingresa un valor no valido
        else:

            #imprime valor  no valido
            valor_no_valido()