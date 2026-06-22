# modelos/cliente.py

class Cliente:
    def __init__(self, cedula: str, nombre: str):
        """
        Constructor de la clase Cliente.
        Cada cliente tiene su identificación, nombre y una lista vacía para sus pedidos.
        """
        self.cedula = cedula
        self.nombre = nombre
        self.pedido_actual = []  # Aquí se guardarán los objetos de la clase Producto

    def agregar_al_pedido(self, producto):
        """Método para añadir un plato o bebida a la cuenta del cliente."""
        self.pedido_actual.append(producto)

    def calcular_total_consumo(self):
        """Método que recorre los productos pedidos y suma sus precios."""
        total = sum(p.precio for p in self.pedido_actual)
        return total

    def __str__(self):
        """Método especial para representar al cliente como texto."""
        return f"Cliente: {self.nombre} | C.I.: {self.cedula}"