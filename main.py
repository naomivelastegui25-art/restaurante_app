# main.py

# 1. IMPORTACIONES: Traemos las clases desde sus carpetas correspondientes
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def ejecutar_sistema():
    # 2. Instanciamos el servicio principal (El Restaurante)
    mi_restaurante = Restaurante("Asadero Amazónico")
    print("=== INICIANDO SISTEMA DE GESTIÓN ===\n")

    # 3. CREACIÓN DE OBJETOS (Productos del Menú)
    plato1 = Producto("Maito de Pescado", 10.50, "Plato Fuerte")
    plato2 = Producto("Caldo de Novillo", 7.00, "Plato Fuerte")
    bebida1 = Producto("Chicha de Chonta", 2.00, "Bebida")
    postre1 = Producto("Helado Artesanal", 1.50, "Postre")

    # 4. AGREGAR OBJETOS AL SERVICIO (Poblar el menú)
    mi_restaurante.registrar_producto(plato1)
    mi_restaurante.registrar_producto(plato2)
    mi_restaurante.registrar_producto(bebida1)
    mi_restaurante.registrar_producto(postre1)

    # 5. Mostrar el menú en consola
    mi_restaurante.mostrar_menu()

    # 6. CREACIÓN DE OBJETOS (Clientes)
    cliente_uno = Cliente("1401234567", "Leonardo Tello")
    cliente_dos = Cliente("1709876543", "Michelita")

    # 7. Registrar los clientes en el restaurante
    mi_restaurante.registrar_cliente(cliente_uno)
    mi_restaurante.registrar_cliente(cliente_dos)

    # 8. SIMULACIÓN DE PEDIDOS (Comunicación entre objetos)
    # Le asignamos productos directamente a la lista de consumo de cada cliente
    cliente_uno.agregar_al_pedido(plato1)
    cliente_uno.agregar_al_pedido(bebida1)

    cliente_dos.agregar_al_pedido(plato2)
    cliente_dos.agregar_al_pedido(bebida1)
    cliente_dos.agregar_al_pedido(postre1)

    # 9. MOSTRAR INFORMACIÓN EN CONSOLA (Reporte Final)
    mi_restaurante.mostrar_resumen_atencion()

if __name__ == "__main__":
    # Arranca la aplicación
    ejecutar_sistema()