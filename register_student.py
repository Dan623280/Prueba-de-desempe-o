
# se importa la function de verificar estado, la student list, las functiones error entero , valor no valido y error estring, verificar name y id
from function_r_student import list_students, error_entero, verifi_Nombre, verifi_Estado, id, error_string

#function para register
def register_student():

    # se crea una variable que llama una funcion que verifica si el usuario esta en la list
    name = verifi_Nombre() 

    # se verifica que la Age no tenga errores
    Age = error_entero("insert Age: ")

    # se verifica que el course no tenga errores
    course = error_string("insert Course: ")

    # se verifica que el usuario aiga colocado estado active o inactive
    Estado = verifi_Estado()
    
    # trae el id del nuevo registro
    numero = id()

    #añade los data a un dicionario
    data = {
 
        'id': numero, 
        'Name': name, 
        'Age': Age, 
        'Course': course, 
        'Estado': Estado

    } 
    
    #se duarda el dicionario
    list_students.append(data)