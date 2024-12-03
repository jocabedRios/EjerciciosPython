# Desarrolla una concesionaria de vehículos en la cual se puedan gestionar las compras y ventas de vehículos. 
# Un usuario podrá ver los vehículos disponibles, su precio y realizar la compra de uno. 
# Aplica los conceptos de programación orientada a objetos vistos en este ejercicio.

class Vehiculo:
    # Constrcutor con las palabra "__init__"
    def __init__(self, matricula, marca, modelo, anio, precio) -> None:
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

#-------------------------------------------------------------------
class Usuario:
    def __init__(self, id, nombre, apellido, fondos) -> None:
        self.id = id
        self.nombre = nombre
        self.apellido1 = apellido
        self.vehiculos = []
        self.fondos = fondos

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
    
    def comprar(self, vehiculo):
        if self.fondos >= vehiculo.precio:
            self.vehiculos.append(vehiculo)
            self.fondos -= vehiculo.precio
            print(f"El usuario {self.nombre} {self.apellido}, ha adquirido el vehículo {vehiculo.modelo} {vehiculo.anio} con matricula {vehiculo.matricula}")
            return True
        else: 
            print("El Usuario no cuenta con los fondos suficientes para comprar el vehículo.")
            return False
    
    def vender(self, concesionaria, vehiculo):
        if  vehiculo in self.vehiculos:
            if(concesionaria.comprar(vehiculo) == True):
                self.vehiculos.remove(vehiculo)
                self.fondos += vehiculo.precio
                print(f"La Concesionaria, ha adquirido el vehículo {vehiculo.modelo} {vehiculo.anio} con matricula {vehiculo.matricula}")
                return True
            else: return False
        else:
            print(f"El vehículo {vehiculo.modelo} {vehiculo.anio} con matricula {vehiculo.matricula} no se encuentra disponible para su venta.")
            return False

#-------------------------------------------------------------------
class Concesionaria:
    def __init__(self, razon_social, fondos) :
        self.razon_social = razon_social
        self.fondos = fondos
        self.vehiculos =  []
        self.usuarios =  []

    def agregar_usuarios(self, usuario):
        self.usuarios.append(usuario)

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def comprar(self, vehiculo):
        if self.fondos >= vehiculo.precio:
            self.vehiculos.append(vehiculo)
            self.fondos -= vehiculo.precio
            print("La Concesionaria ha comprado el vehículo.")
            return True
        else:
            print("La Concesionaria no cuenta con los fondos suficientes para comprar el vehículo.")
            return False
    
    def vender(self, usuario, vehiculo):
        if  vehiculo in self.vehiculos:
            if(usuario.comprar(vehiculo) == True):
                self.vehiculos.remove(vehiculo)
                self.fondos += vehiculo.precio
                print(f"El usuario {usuario.nombre} {usuario.apellido}, ha adquirido el vehículo {vehiculo.modelo} {vehiculo.anio} con matricula {vehiculo.matricula}")
                return True
            else: return False
        else:
            print(f"El vehículo {vehiculo.modelo} {vehiculo.anio} con matricula {vehiculo.matricula} no se encuentra disponible para su venta.")
            return False
    
    def vehiculosDisponibles(self):
        print("Vehiculos disponibles:")
        for vehiculo in self.vehiculos:
            print(f"{vehiculo.modelo} {vehiculo.anio} con matricula {vehiculo.matricula}, Precio: ${vehiculo.precio}.00.")
    
    def registrarUsuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"El usuario {usuario.nombre} {usuario.apellido}, ha sido registrado con éxito!")

# PRUEBAS -------------------------------------------------------------------
# Se creó una Concesionaria con un nombre y fondos
concesionaria = Concesionaria("JOCAR's", 5000000)
# Se crean 4 instancias de Vehículos
vehiculo1 = Vehiculo("JHO987U9", "DeLorean", "DMC-12", 1985, 200000)
vehiculo2 = Vehiculo("990JJ0J0", "Mazda", "Miata", 1995, 150000)
vehiculo3 = Vehiculo("J890YH9L", "Jepp", "Cherokee", 1999, 100000)
vehiculo4 = Vehiculo("J78Y7H08", "Volkswagen", "Bocho", 2000, 100000)
# Se crea un Usuario
usuario = Usuario("001", "Papita","Frita", 150000)
# Se le asigna un Vehículo al Usuario
usuario.agregar_vehiculo(vehiculo1)
# Se registra al usuario dentro de la Concesionaria
concesionaria.agregar_usuarios(usuario)
# Se le asignan Vehículos a la Concesionaria
concesionaria.agregar_vehiculo(vehiculo2)
concesionaria.agregar_vehiculo(vehiculo3)
concesionaria.agregar_vehiculo(vehiculo4)
concesionaria.vehiculosDisponibles()










