# se importa la function de la student list
from list_students import list_students

import json

#---------------------------
# Guardar
#---------------------------

# function Guardar el json
def Guardar():

    # se abre el archivo para escribir y se llama por "archivo"
    with open("data.json", "w", encoding="utf-8") as archivo:

        # se escriben los data de la list en el archivo
        json.dump(list_students, archivo, indent=4, ensure_ascii=False)