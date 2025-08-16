# ======================================
# SISTEMA DE GESTIÓN DE INVENTARIOS
# Autor: Dany Yauri
# ======================================

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


# Clase Inventario
class Inventario:
    def __init__(self):
        # Usamos un diccionario con ID como clave y Producto como valor
        self.productos = {}

    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("❌ Error: El ID ya existe en el inventario.")
        else:
            self.productos[producto.get_id()] = producto
            print("✅ Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("🗑️ Producto eliminado con éxito.")
        else:
            print("❌ Error: No existe un producto con ese ID.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            print("✅ Producto actualizado correctamente.")
        else:
            print("❌ Error: No se encontró el producto.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            print("\n🔍 Resultados de búsqueda:")
            for p in resultados:
                print(p)
        else:
            print("❌ No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if self.productos:
            print("\n📦 Inventario completo:")
            for p in self.productos.values():
                print(p)
        else:
            print("📂 El inventario está vacío.")


# Interfaz de usuario en consola
def menu():
    inventario = Inventario()

    while True:
        print("\n==============================")
        print("  SISTEMA DE INVENTARIO - MENÚ")
        print("==============================")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID: ")
            nombre = input("Ingrese nombre: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (ENTER para omitir): ")
            precio = input("Nuevo precio (ENTER para omitir): ")
            inventario.actualizar_producto(
                id_producto,
                cantidad=int(cantidad) if cantidad else None,
                precio=float(precio) if precio else None
            )

        elif opcion == "4":
            nombre = input("Ingrese nombre o parte del nombre: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "0":
            print("👋 Gracias por usar el sistema de inventario.")
            break

        else:
            print("❌ Opción inválida, intenta de nuevo.")


if __name__ == "__main__":
    menu()
