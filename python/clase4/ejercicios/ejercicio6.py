# Ejercicio 6: modificar los elementos de una lista
lista_numeros = list(range(1, 11))
for i in lista_numeros:
    print(i, end="-")

valor = int(input("\nDigite un valor a multiplicar: "))
#multiplicar todos los elementos de la lista
for indice, i in enumerate(lista_numeros):
    lista_numeros[indice] *= valor

print(f"lista final con los elementos multiplicados: {valor}")
for i in lista_numeros:
    print(i, end="-")
print("")
print("Fin")