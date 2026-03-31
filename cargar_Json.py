
# se importa la function de la student list
from list_students import list_students

#se importa el json
import json

#---------------------------
# Cargar
#---------------------------

# function carga el json
def Cargar():

    # se abre el archivo para leer y se llama por "archivo"
    with open("data.json", "r", encoding="utf-8") as archivo:
        
        # se leen los data y seguardan en la variables
        data_json = json.load(archivo)

    #se ingresan los data a la variable de la student list
    list_students.extend(data_json)