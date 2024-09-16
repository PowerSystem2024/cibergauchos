#Ejercicio 9: hacer un programa para calcular el factorial de un número positivo
numeero = int(input("Digite un numero: "))
while numeero < 0:
    print("Error -> El numero tiene que ser positivo")
    numeero = int(input("Digite un numero: "))
factorial = 1
for i in range(1, numeero + 1):
    factorial *= i
print(f"\nEl factorial del numero {numeero} es: {factorial}")