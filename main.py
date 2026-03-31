#importa la function del menu
from menu import Menu

#importa la function de valor no valido
from error import valor_no_valido

# importar function de registro
from register_student import register_student

# importar function de consultas
from Consult_list import Consult_list

# importar function de busqueda del student
from Look_for_student import Look_for

# importar function de update student
from Update_student import update

# importarfunction de Delete student
from Delete_student import Delete

# importar function de guardar data
from guardar_json import Guardar

# importar function de cargar data
from cargar_Json import Cargar

#-------------------------
# Principal
#-------------------------

# function carga el json
Cargar()

while True:

    # muestra el menu y devuelve la option seleccionada
    option = Menu()

    # option 1 Registra nuevos students
    if option == 1:

        #function para register
        register_student()
    
    # option 2 Consulta la student list
    elif option == 2:

        #function para  Consult lists
        Consult_list()

    # option 3 Busca un student
    elif option == 3:

        #function para Look_for
        Look_for()

    # option 4 Actualiza la información de un student
    elif option == 4:

        #function para update
        update()

    # option 5 Elimina students
    elif option == 5:

        #function para Delete
        Delete()

    # option 6 Sale del programa
    elif option == 6:

        #function para Guardar
        Guardar()

        #se termina el ciclo
        break

    # cunado el usuario ingresa un valor no valido
    else:

        #imprime valor  no valido
        valor_no_valido()