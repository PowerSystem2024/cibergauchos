# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados celsius
# a fahrenheit y viceversa. Las fórmulas correspondientes son: 
# F = 1.8 * C + 32 fahrenheit
# C = (F - 32) / 1.8 celsius

def celsius_a_fahrenheit(celsius):
    fahrenheit = 1.8 * celsius + 32
    return fahrenheit

def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

grados_celsius = float(input("Proporcione la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(grados_celsius)
print(f"La temperatura en grados de celsius a Fahrenheit es: {fahrenheit}")

grados_fahrenheit = float(input("Proporcione la temperatura en grados Fahrenheit: "))
celsius = fahrenheit_a_celsius(grados_fahrenheit)
print(f"La temperatura en grados de fahrenheit a Celsius es: {celsius}")