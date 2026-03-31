
# Trae los data de la student list
from list_students  import list_students

#------------------------------
# Consult
#------------------------------

# crea la function de Consult
def Consult_list():

    # se recorre la list
    for elemento in list_students:

        # se imprimen los data de la list
        print(f"Indice = {elemento['id']}, Name = {elemento['Name']}, Age = {elemento['Age']}, Course = {elemento['Course']}, Estado = {elemento['Estado']}")