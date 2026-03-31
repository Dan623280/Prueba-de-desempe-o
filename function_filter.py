
# se importa la function de verificar la student list, las functiones error entero , valor no valido y error estring
from function_r_student import error_entero, list_students, valor_no_valido, error_string, verifi_Estado


#-------------------------
# Menu filter
#-------------------------

def Menu_filter():

    #Mostrar menu
    print("")
    print("1. ID")
    print("2. Name")
    print("3. Age")
    print("4. course")
    print("5. Estado")
    print("6. go_out")
    print("")

    #Pedir option
    option = error_entero("Input option: ")

    #Retorna option
    return option

#-------------------------
# Indice
#-------------------------

def Indice(list_id):

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



#------------------------------
# Name
#------------------------------

def Verifi_name_filter():

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

            # retorna el name
            return name
        
        # si name no esta en list
        else:

            # muestra mensaje de name no exites
            print("----------------------")
            print("-- Name no existe --")
            print("----------------------")



def Name():

    name = Verifi_name_filter()

    #se crea un bucle para recorrer los elementos
    for elemento in list_students:
                
            #si name es igual a name
            if elemento['Name'] == name:
                    
                # se imprimen los data de la list
                print(f"Indice = {elemento['id']}, Name = {elemento['Name']}, Age = {elemento['Age']}, Course = {elemento['Course']}, Estado = {elemento['Estado']}")
    
        

#------------------------------
# Age
#------------------------------

def Verifi_age_filter():

    while True:

        Age = error_entero("insert Age: ")

        list_age = []

        for elemento in list_students:

            list_age.append(elemento['Age'])

        if Age in list_age:

            return Age
        else:

            print("--------------------")
            print("-- Age no existe --")
            print("--------------------")



def Age():

    Age = Verifi_age_filter()

    for elemento in list_students:
                
            if elemento['Age'] == Age:
                    
                print(f"Indice = {elemento['id']}, Name = {elemento['Name']}, Age = {elemento['Age']}, Course = {elemento['Course']}, Estado = {elemento['Estado']}")


#------------------------------
# Course
#------------------------------

def Verifi_course_filter():

    while True:

        course = error_string("insert Course: ")

        list_course = []

        for elemento in list_students:

            list_course.append(elemento['Course'])

        if course in list_course:

            return course
        else:

            print("----------------------")
            print("-- Course no existe --")
            print("----------------------")



def Course():

    course = Verifi_course_filter()

    for elemento in list_students:
                
            if elemento['Course'] == course:
                    
                print(f"Indice = {elemento['id']}, Name = {elemento['Name']}, Age = {elemento['Age']}, Course = {elemento['Course']}, Estado = {elemento['Estado']}")
    

#------------------------------
# Estado
#------------------------------

def Estado():

    estado = verifi_Estado()

    for elemento in list_students:
                
            if elemento['Estado'] == estado:
                    
                print(f"Indice = {elemento['id']}, Course = {elemento['Course']}, Age = {elemento['Age']}, Course = {elemento['Course']}, Estado = {elemento['Estado']}")
    
    