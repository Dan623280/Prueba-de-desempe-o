
# se importa la function de verificar la lista de estudiantes, las functiones error entero , valor no valido y error estring
from function_r_estudiante import error_entero, Lista_estudiantes, valor_no_valido, error_string, verifi_Estado


#-------------------------
# Menu filter
#-------------------------

def Menu_filter():

    #Mostrar menu
    print("")
    print("1. ID")
    print("2. Nombre")
    print("3. Edad")
    print("4. curso")
    print("5. Estado")
    print("6. Salir")
    print("")

    #Pedir option
    option = error_entero("Input option: ")

    #Retorna option
    return option

#-------------------------
# Indice
#-------------------------

def Indice(lista_id):

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



#------------------------------
# Nombre
#------------------------------

def Verifi_nombre_filter():

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

            # retorna el nombre
            return nombre
        
        # si nombre no esta en lista
        else:

            # muestra mensaje de nombre no exites
            print("----------------------")
            print("-- Nombre no existe --")
            print("----------------------")



def Nombre():

    nombre = Verifi_nombre_filter()

    #se crea un bucle para recorrer los elementos
    for elemento in Lista_estudiantes:
                
            #si nombre es igual a nombre
            if elemento['Nombre'] == nombre:
                    
                # se imprimen los datos de la lista
                print(f"Indice = {elemento['id']}, Nombre = {elemento['Nombre']}, Edad = {elemento['Edad']}, Curso = {elemento['Curso']}, Estado = {elemento['Estado']}")
    
        

#------------------------------
# Edad
#------------------------------

def Verifi_edad_filter():

    while True:

        edad = error_entero("Colocar Edad: ")

        lista_edad = []

        for elemento in Lista_estudiantes:

            lista_edad.append(elemento['Edad'])

        if edad in lista_edad:

            return edad
        else:

            print("--------------------")
            print("-- Edad no existe --")
            print("--------------------")



def Edad():

    edad = Verifi_edad_filter()

    for elemento in Lista_estudiantes:
                
            if elemento['Edad'] == edad:
                    
                print(f"Indice = {elemento['id']}, Nombre = {elemento['Nombre']}, Edad = {elemento['Edad']}, Curso = {elemento['Curso']}, Estado = {elemento['Estado']}")


#------------------------------
# Curso
#------------------------------

def Verifi_curso_filter():

    while True:

        curso = error_string("Colocar Curso: ")

        lista_curso = []

        for elemento in Lista_estudiantes:

            lista_curso.append(elemento['Curso'])

        if curso in lista_curso:

            return curso
        else:

            print("----------------------")
            print("-- Curso no existe --")
            print("----------------------")



def Curso():

    curso = Verifi_curso_filter()

    for elemento in Lista_estudiantes:
                
            if elemento['Curso'] == curso:
                    
                print(f"Indice = {elemento['id']}, Nombre = {elemento['Nombre']}, Edad = {elemento['Edad']}, Curso = {elemento['Curso']}, Estado = {elemento['Estado']}")
    

#------------------------------
# Estado
#------------------------------

def Estado():

    estado = verifi_Estado()

    for elemento in Lista_estudiantes:
                
            if elemento['Estado'] == estado:
                    
                print(f"Indice = {elemento['id']}, Curso = {elemento['Curso']}, Edad = {elemento['Edad']}, Curso = {elemento['Curso']}, Estado = {elemento['Estado']}")
    
    