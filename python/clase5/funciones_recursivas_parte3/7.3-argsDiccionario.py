def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ["Danilo", "Juakin", "Ali"]
desplegarNombres(nombres2)
desplegarNombres("Gino") 
#desplegarNombres(10) # nos devuelve error porque no es un iterable
desplegarNombres((10, 11)) # se convierte en una tupla y si recorre
desplegarNombres([12, 13]) # se convierte en una lista