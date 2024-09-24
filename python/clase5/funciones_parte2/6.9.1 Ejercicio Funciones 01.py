def sumar_valor(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado

print(sumar_valor(3, 5, 9, 2, 1))