# ******* Doble de los Números *******
# Dada una lista de números [1, 2, 3, 4, 5], 
# crea una nueva lista que contenga el doble de cada número usando una List Comprehension.
original = [1, 2, 3, 4, 5]
doubles = [x*2 for x in original]
print("Lista original:",original)
print("Lista con valores duplicados:",doubles)

# ******* Filtrar y Transformar en un Solo Paso *******
# Tienes una lista de palabras ["sol", "mar", "montaña", "rio", "estrella"] 
# y quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas.
words = ["sol", "mar", "montaña", "rio", "estrella"]
len_more_than_3 = [word.upper() for word in words if len(word)>3]
print("\nLista de palabras:", words)
print("Lista de palabras con una longitud mayor a 3:", len_more_than_3)

# ******* Crear un Diccionario con List Comprehension
# Tienes dos listas, una de claves ["nombre", "edad", "ocupación"] y otra de valores ["Juan", 30, "Ingeniero"]. 
# Crea un diccionario combinando ambas listas usando una List Comprehension.
keys = ["nombre", "edad", "ocupación"] 
values = ["Juan", 30, "Ingeniero"]
dictionary = [{key:value for value in values for key in keys}]
print("\nDiccionario:", dictionary)