# Las Comprehension Lists permiten crear de una manera fácil y rápida
# Esta Comprehension List está creando una lista que contiene los cuadrados de los números del 1 al 10
squares = [x**2 for x in range(1,11)]
print("Cuadrados del uno al 10:", squares)

# Esta Comprehension List se llena con datos del 0 al 40 y de 10 en 10
celsius = [10*x for x in range(0, 5)]
print("Temperatura en C°:", celsius)
# Esta Comprehension List convierte los datos en la lista celsius a grados fahrenheit
fahrenheit = [(temp*9/5)+32 for temp in celsius]
print("Temperatura en F°:", fahrenheit)

# Esta Comprehension List contiene los números pares entre el 1 y el 20
evens = [x for x in range (1,21) if x%2==0]
print("Números pares entre el 1 y el 20:", evens)

# Obtener las transpuesta de una matriz (cambiar filas por columnas)
matrix = [[1,2,3], # [[1,4,7]
          [4,5,6],  #  [2,5,8]
          [7,8,9]] #  [3,6,9]]
print("Matriz:", matrix)
# El for "principal" es, for i in range(len(matrix[0])) devolvería 0,1,2
# El for "secundario", for row in matrix intera entre cada fila de la matriz "matrix"
# Por lo tanto en la primera corrida del ciclo estaría tomando el dato con index 0 de cada fila(row) -> 1,4,7
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))] 
print("Matriz transpuesta:", transposed)
