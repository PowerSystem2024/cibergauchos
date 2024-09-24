#6.1 Ejercicio 10 No Repetir Caracteres
# Hacer un programa que pida una cadena por teclado, luego 
# meter los caracteres en un alista sin repetir caracteres.

lista = [] #
cadena  = input("Digite una cadena \n")

for  i in cadena: #bucle for para recorrer el objeto cadena.
    if i not in lista: #pregunta si el caracter esta en la lista, si es true avanza.
        lista.append(i) # agregamos a la lista.
 
print(f'\n Lista de caracteres sin repetir ningun caracter: \n {lista}')
