# Argumentos, variables en funciones
def listarNombres(*nombres):
    for nombre in nombres: #se convierte en una tupla
        print(nombre)
listarNombres("Juan", "Pedro", "Maria", "Luis", "Ana", "Jose")
listarNombres("Danilo", "Lucas" , "Miguel", "Carlos", "Fernando", "Javier", "Joaquin",)

def listarTerminos(**terminos):
    for key, value in terminos.items():
        print(f"La clave es: {key}: y el valor: {value}")

listarTerminos() # si no recibe argumentos, no se muestra nada
listarTerminos(IDE = "Integrated Development Environment", PK = "Primary Key", FK = "Foreign Key", DB = "Data Base", API = "Application Programming Interface")
listarTerminos(Nombre = "Leonel Messi")