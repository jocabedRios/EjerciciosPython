# lambda, sólo necesita parámetros y una operación para poder aplicar a ella
add = lambda a, b: a+b
print("8 + 13 =", add(8,13))

numbers = range(11)
# En esta línea se está generando una lista por medio de un "mapeo" de los valores contenidos en la lista numbers,
# y se está obteniendo el cuadrado de cada uno haciendo uso de una función lambda
squared_numbers = list(map(lambda x: x**2, numbers))
print("Cuadrado de los números del 0 al 10:", squared_numbers)

# Para este caso se utiliza "filter" para aplicar un filtro y obtener los números pares entre el 0 y el 10
# haciendo uso de una función lambda
even_numbers = list(filter(lambda x: x%2==0, numbers))
print("Números pares del 0 al 10:", even_numbers)