print(" ******* 1. Doble de los Números *******")
# Dada una lista de números [1, 2, 3, 4, 5], 
# crea una nueva lista que contenga el doble de cada número usando una List Comprehension.
original = [1, 2, 3, 4, 5]
doubles = [x*2 for x in original]
print("Lista original:",original)
print("Lista con valores duplicados:",doubles)

print("\n ******* 2. Filtrar y Transformar en un Solo Paso *******")
# Tienes una lista de palabras ["sol", "mar", "montaña", "rio", "estrella"] 
# y quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas.
words = ["sol", "mar", "montaña", "rio", "estrella"]
len_more_than_3 = [word.upper() for word in words if len(word)>3]
print("Lista de palabras:", words)
print("Lista de palabras con una longitud mayor a 3:", len_more_than_3)

print("\n ******* 3. Crear un Diccionario con List Comprehension")
# Tienes dos listas, una de claves ["nombre", "edad", "ocupación"] y otra de valores ["Juan", 30, "Ingeniero"]. 
# Crea un diccionario combinando ambas listas usando una List Comprehension.
keys = ["nombre", "edad", "ocupación"] 
values = ["Juan", 30, "Ingeniero"]
dictionary = {key:value for value in values for key in keys}
print("Diccionario:", dictionary)

print("\n  ******* 4. Anidación de List Comprehensions *******")
# Calcula la matriz traspuesta utilizando una List Comprehension anidada.
# Dada una lista de listas (una matriz):
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Calcula la matriz traspuesta utilizando una List Comprehension anidada.
traspuesta = [ [row[i] for row in matriz] for i in range(len(matriz[0]))]
print("Matriz:", matriz)
print("Traspuesta:", traspuesta)

print("\n ******* 5. Extraer Información de una Lista de Diccionarios *******")
# Dada una lista de diccionarios que representan personas:
personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]
# Extrae una lista de nombres de personas que viven en “Madrid” y tienen más de 30 años.
madrid_30 = [persona["nombre"] for persona in personas if persona["ciudad"]=="Madrid" and persona["edad"]>30]
print("Personas:", personas)
print("Personas de Madrid mayores de 30:", madrid_30)

print("\n ******* 6. List Comprehension con un else *******")
# Dada una lista de números 
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# crea una nueva lista multiplicando por 2 los números pares y dejando los impares como están.
mul_pares = [numero*2 if numero%2==0 else numero for numero in numeros]
print("Lista de números:", numeros)
print("Duplicar pares de la Lista de números:", mul_pares)
