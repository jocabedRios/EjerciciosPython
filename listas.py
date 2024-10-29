# Las listas tienen libertad al momento de guardar la información, se puede guardar distintos tipos de datos dentro de la misma
# por ejemplos cadenas, enteros, flotantes, booleanos incluso otras listas.
mix = [1,2,3.14,True, "cinco",[6,7,8]]
print(mix)
print(len(mix))
print("Primer elemento:", mix[0])
print("Segundo elemento:", mix[1])
print("Tercer elemento:", mix[3])
print("Último elemento:", mix[-1])


# S L I C I N G : También es aplicable para cadenas
print("Retorna los elementos de la lista desde la posición 0 a la 1: [0:2]")
print(mix[0:2])
print("también se puede omitir el 0 y por defult se entenderá que se quiere tomar desde la posición 0, [:2]")
print(mix[:2])
print("para tomar los elemento de la posición 2 hasta la útima posición, [2:]")
print(mix[2:])
print("para tomar todo menos las útimas 2 posiciones [:-2]")
print(mix[:-2])
print("para tomar todo, apartir de la segunda posición menos las útimas 2 posiciones [2:-2]")
print(mix[2:-2])