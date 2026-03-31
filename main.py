#importa la function del menu
from menu import Menu

#importa la function de valor no valido
from error import valor_no_valido

# importar function de registro
from registrar_estudiante import Registrar_estudiante

# importar function de consultas
from consultar_lista import Consultar_lista

# importar function de busqueda del estudiante
from buscar_estudiante import Buscar

# importar function de actualizar estudiante
from actualizar_estudiante import Actualizar

# importarfunction de eliminar estudiante
from eliminar_estudiante import Eliminar

# importar function de guardar datos
from guardar_json import Guardar

# importar function de cargar datos
from cargar_Json import Cargar

#-------------------------
# Principal
#-------------------------

# function carga el json
Cargar()

while True:

    # muestra el menu y devuelve la option seleccionada
    option = Menu()

    # option 1 Registra nuevos estudiantes
    if option == 1:

        #function para registrar
        Registrar_estudiante()
    
    # option 2 Consulta la lista de estudiantes
    elif option == 2:

        #function para  consultar listas
        Consultar_lista()

    # option 3 Busca un estudiante
    elif option == 3:

        #function para buscar
        Buscar()

    # option 4 Actualiza la información de un estudiante
    elif option == 4:

        #function para actualizar
        Actualizar()

    # option 5 Elimina estudiantes
    elif option == 5:

        #function para eliminar
        Eliminar()

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