# Los diccionarios se componen de una clave(key) y un valor(value) y se declaran hacuendo uso de llaves ({})
information = {"Name":"Jocabed", "Lastname":"Ríos", "Age":25}
print("information: ",information)

# Acceder a un valor por medio de su llave
value = information["Name"]
print("Value of \"Name\":", value)

# Obtener las llaves de un diccionario
keys = information.keys()
print("Keys :", keys)

# Obtener los valores de un diccionario
values = information.values()
print("Values :", values)

# Obtener en tuplas los elementos de un diccionario
items = information.items()
print("Items :", items)