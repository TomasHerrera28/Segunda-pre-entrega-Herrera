
class Cliente:
    def __init__(self, nombre, email, direccion, telefono):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre}"

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Email: {self.email}, Dirección: {self.direccion}, Teléfono: {self.telefono}"

    def actualizar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion
        return f"La nueva dirección de {self.nombre} es {self.direccion}"