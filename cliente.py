class Cliente:
    def __init__(self, nombre, email, direccion, telefono):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}, Dirección: {self.direccion}, Teléfono: {self.telefono}"

    def hacer_pedido(self, pedido):
        print(f"{self.nombre} ha realizado el siguiente pedido: {pedido}")

class ClienteRegistrado(Cliente):
    def __init__(self, nombre, email, direccion, telefono, usuario, contraseña):
        super().__init__(nombre, email, direccion, telefono)
        self.usuario = usuario
        self.contraseña = contraseña

    def login(self, usuario, contraseña):
        if usuario == self.usuario and contraseña == self.contraseña:
            return True
        else:
            return False

    def cambiar_contraseña(self, nueva_contraseña):
        self.contraseña = nueva_contraseña
        print("Contraseña cambiada exitosamente.")