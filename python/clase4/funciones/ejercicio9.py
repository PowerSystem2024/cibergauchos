# Ejercicio 9: Mostrar una frase sin espacios y contar su longitud.
# Ejemplo = Vivir por siempre en paz
# Vivirporsiempreenpaz
# N° Caracteres= 21
frase1 = input('Digite una frase: ') # Pide una frase por consola
frase2 = " "
for i in frase1: 
    if i != " ": # si el iterador es diferente a un espacio vacio
        frase2 += i # guarda el elemento en la variable frase2
frase1 = frase2
print(f'\nFrase Final: {frase1}')
print(f'\nN° de caracteres: {len(frase1)}') # con cadenas la funcion len nos muestra la cantidad de caracteres