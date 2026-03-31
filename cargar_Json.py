
# se importa la function de la lista de estudiantes
from lista_estudiantes import Lista_estudiantes

#se importa el json
import json

#---------------------------
# Cargar
#---------------------------

# function carga el json
def Cargar():

    # se abre el archivo para leer y se llama por "archivo"
    with open("datos.json", "r", encoding="utf-8") as archivo:
        
        # se leen los datos y seguardan en la variables
        datos_json = json.load(archivo)

    #se ingresan los datos a la variable de la lista de estudiantes
    Lista_estudiantes.extend(datos_json)