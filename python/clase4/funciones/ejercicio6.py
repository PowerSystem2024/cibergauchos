# Ejercicio 6: Tabla de Multiplicar
# Hacer un programa que pida un número por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10, por ejemplo
# Si digita el 5 guarde: 5,10,15,20,25.....
num = int(input('Digite un número: '))
lista = [] # Creamos la lista vacia
for i in range (1, 11): # En un rango del 1 al 10
    lista.append(i*num) # Agrega a la lista el iterador multiplicado al número ingresado

print(f'\n Tabla de multiplicar del {num} es: {lista}')

for indice, i in enumerate(lista):
    print(f'{num} X {i} = {lista[indice]}')