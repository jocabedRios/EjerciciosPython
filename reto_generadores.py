# Crear un generador de número pares y otro de números impares
def pares(limite):
    a = 2
    while a<=limite:
        if a%2 == 0:
            # Aquí se está utilizando la palabra reservada "yield" para regresar el valor
            yield a
        a+=1

def impares(limite):
    a = 2
    while a<=limite:
        if a%2 == 1:
            yield a
        a+=1

limite_usuario = int(input("Ingresa un límite:"))
print("\nPares:")
for par in pares(limite_usuario):
    print(par)

print("\nImpares:")
for impar in impares(limite_usuario):
    print(impar)