# se importa la function de la lista de estudiantes
from lista_estudiantes import Lista_estudiantes

import json

#---------------------------
# Guardar
#---------------------------

# function Guardar el json
def Guardar():

    # se abre el archivo para escribir y se llama por "archivo"
    with open("datos.json", "w", encoding="utf-8") as archivo:

        # se escriben los datos de la lista en el archivo
        json.dump(Lista_estudiantes, archivo, indent=4, ensure_ascii=False)