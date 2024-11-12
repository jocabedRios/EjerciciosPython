# FUNCIONES
# Las funciones de declaran mediante el uso de la palabrta reservada "def"
# Para este caso se le atá asignando un valor por default a la variable de_tal para el caso de no se comparta este parámetro
def greet(fulanito, de_tal="sin apellido"):
    print(f"Hola {fulanito} {de_tal}")

greet("Jocabed", "Ríos")
# Saludo sin enviar "apellido"
greet("Fulanito")
print()

# Aquí se ha creado una calculadora utilizando funciones y un loop
# para permitir que el usuario haga uso de ella cuantas veces lo desee.
def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def calculator():
    while(True):
        print('''I N T R U C C I O N E S:
Selecciona una operación y posteriormente introduce dos valores para realizar la operación.
1. Presiona 1 para realizar una suma.
2. Presiona 2 para realizar una resta.
3. Presiona 3 para realizar una multiplicación.
4. Presiona 4 para realizar una división.
5. Presiona 5 para salir. \n''')
        
        operation = int(input("Operación: "))
        if operation==5:
            print("Saliendo... hasta pronto!")
            break
        value1 = float(input("Primer valor: "))
        value2 = float(input("Segundo valor: "))

        if operation==1:
            print(f"{value1} + {value2} =", add(value1,value2))
        elif operation==2:
            print(f"{value1} - {value2} =", substract(value1,value2))
        elif operation==3:
            print(f"{value1} * {value2} =", multiply(value1,value2))
        elif operation==4:
            print(f"{value1} / {value2} =", divide(value1,value2))
        
        print()

calculator()