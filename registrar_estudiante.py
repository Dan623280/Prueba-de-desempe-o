
# se importa la function de verificar estado, la lista de estudiantes, las functiones error entero , valor no valido y error estring, verificar nombre y id
from function_r_estudiante import Lista_estudiantes, error_entero, verifi_Nombre, verifi_Estado, id, error_string

#function para registrar
def Registrar_estudiante():

    # se crea una variable que llama una funcion que verifica si el usuario esta en la lista
    nombre = verifi_Nombre() 

    # se verifica que la edad no tenga errores
    edad = error_entero("Colocar Edad: ")

    # se verifica que el curso no tenga errores
    curso = error_string("Colocar Curso: ")

    # se verifica que el usuario aiga colocado estado activo o inactivo
    Estado = verifi_Estado()
    
    # trae el id del nuevo registro
    numero = id()

    #añade los datos a un dicionario
    datos = {
 
        'id': numero, 
        'Nombre': nombre, 
        'Edad': edad, 
        'Curso': curso, 
        'Estado': Estado

    } 
    
    #se duarda el dicionario
    Lista_estudiantes.append(datos)