#--------------------------
# function de error
#--------------------------


# function mensaje de error
def valor_no_valido():

    # mensaje de error
    print("---------------------")
    print("-- valor no valido --")
    print("---------------------")



# function de error string
def error_string(var):

    #ciclo while
    while True:

        #--------------------------
        # Detectar si hay un error
        #--------------------------

        try:

            # pide valor
            valor = input(f"{var}")

            #retorna valor
            return valor


        except:

            #mensaje de error
            valor_no_valido()


# function de error string
def error_entero(var):

    #ciclo while
    while True:

        #--------------------------
        # Detectar si hay un error
        #--------------------------

        try:

            # pide valor
            valor = int(input(f"{var}"))

            if valor >= 0:

                #retorna valor
                return valor

            else:

                valor_no_valido()

        except:

            #mensaje de error
            valor_no_valido()


# para llamar

# from error import error_entero,error_string, valor_no_valido