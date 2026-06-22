# modelos/producto.py

class Producto:
    def __init__(self, nombre: str, precio: float, categoria: str):
        """
        Constructor de la clase Producto.
        Define los atributos básicos de cualquier elemento del menú.
        """
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria  # Ejemplo: 'Plato Fuerte', 'Bebida', 'Postre'

    def __str__(self):
        """
        Método especial __str__().
        Permite que al imprimir un objeto Producto, se muestre como texto legible.
        """
        return f"{self.nombre} ({self.categoria}) - ${self.precio:.2f}"