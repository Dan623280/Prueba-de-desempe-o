
# Trae los datos de la lista de estudiantes
from lista_estudiantes  import Lista_estudiantes

#------------------------------
# consultar
#------------------------------

# crea la function de consultar
def Consultar_lista():

    # se recorre la lista
    for elemento in Lista_estudiantes:

        # se imprimen los datos de la lista
        print(f"Indice = {elemento['id']}, Nombre = {elemento['Nombre']}, Edad = {elemento['Edad']}, Curso = {elemento['Curso']}, Estado = {elemento['Estado']}")