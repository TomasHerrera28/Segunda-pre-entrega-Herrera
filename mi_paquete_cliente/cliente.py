from .main import Cliente

def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    email = input("Ingrese el correo electrónico del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    return Cliente(nombre, email, direccion, telefono)
 
def listar_clientes(clientes):
    for cliente in clientes.values():
        print(cliente.nombre, cliente.email, cliente.direccion, cliente.telefono)
