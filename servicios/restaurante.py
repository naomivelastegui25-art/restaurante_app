# servicios/restaurante.py

class Restaurante:
    def __init__(self, nombre: str):
        """
        Constructor del servicio Restaurante.
        Inicializa las listas globales para controlar el negocio.
        """
        self.nombre = nombre
        self.menu_productos = []       # Catálogo de comida disponible
        self.clientes_registrados = []  # Historial de clientes en el local

    def registrar_producto(self, producto):
        """Agrega un objeto Producto al menú."""
        self.menu_productos.append(producto)
        print(f"[Menú] Registrado con éxito: {producto.nombre}")

    def registrar_cliente(self, cliente):
        """Registra a un cliente en el sistema del restaurante."""
        self.clientes_registrados.append(cliente)
        print(f"[Sistema] Cliente ingresado: {cliente.nombre}")

    def mostrar_menu(self):
        """Imprime de forma ordenada el menú actual en la consola."""
        print(f"\n--- MENÚ DE {self.nombre.upper()} ---")
        if not self.menu_productos:
            print("El menú está vacío por ahora.")
        for prod in self.menu_productos:
            print(f" * {prod}")  # Aquí actúa el __str__ de Producto
        print("-" * 35)

    def mostrar_resumen_atencion(self):
        """Genera un reporte final de lo que consumió cada cliente y su cuenta."""
        print(f"\n==========================================")
        print(f"   REPORTES DE CONSUMO - {self.nombre.upper()}   ")
        print(f"==========================================")
        for cli in self.clientes_registrados:
            print(cli)  # Aquí actúa el __str__ de Cliente
            print(" Detalle del pedido:")
            if not cli.pedido_actual:
                print("   - No ha ordenado nada aún.")
            for prod in cli.pedido_actual:
                print(f"   • {prod.nombre} (${prod.precio:.2f})")
            print(f" Total a Cancelar: ${cli.calcular_total_consumo():.2f}")
            print("." * 42)