# Ejercicio 7: Juego Adivina el número.
# Generar un numero aleatorio entre 1 y 100,
# ir pidiendo numeros indicando si el numero es menor o mayor al ingresado
# hasta acertar, tambien mostrar el número de intentos.
import random
print(f'\tBienvenido al juego ¡Adivina el numero.!')
numAleatorio = random.randint(1, 100) # Tener en cuenta que toma el 100. no uno menos o uno mas.
contador = 0
while True:
    num = int(input('Digite un número: '))
    contador += 1
    if num > numAleatorio: # Si el ingresado es mayor
        print(f'\tEl numero es muy grande, digite uno menor.')
    elif num < numAleatorio: # Si el ingresado es menor
        print(f'\tEl numero es muy chico, digite uno mayor.')
    else: # Si los numeros coinciden!
        print(f'¡FELICITACIONES!, Has encontrado el número aleatorio: {numAleatorio}')
        break # Rompe el bucle.
print(f'Has encontrado el numero en {contador} intentos, ¡bien hecho!')