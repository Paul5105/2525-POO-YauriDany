import json
import os

# ========================
# Clase Producto
# ========================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        """Convierte el producto a diccionario (para guardar en JSON)."""
        return {
            "ID": self.id_producto,
            "Nombre": self.nombre,
            "Cantidad": self.cantidad,
            "Precio": self.precio
        }

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


# ========================
# Clase Inventario
# ========================
class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}  # Usamos un diccionario {ID: Producto}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga el inventario desde archivo JSON."""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r", encoding="utf-8") as f:
                    datos = json.load(f)
                    for id_producto, datos_producto in datos.items():
                        self.productos[id_producto] = Producto(
                            id_producto,
                            datos_producto["Nombre"],
                            datos_producto["Cantidad"],
                            datos_producto["Precio"]
                        )
                print("Inventario cargado exitosamente ✅")
            except Exception as e:
                print(f"Error al cargar inventario: {e}")
        else:
            print("No existe inventario, se creará uno nuevo.")

    def guardar_inventario(self):
        """Guarda el inventario en archivo JSON."""
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump({id: p.to_dict() for id, p in self.productos.items()}, f, indent=4)
            print("Inventario guardado correctamente 💾")
        except Exception as e:
            print(f"Error al guardar inventario: {e}")

    def añadir_producto(self, producto):
        if producto.id_producto in self.productos:
            print("⚠️ El ID ya existe en el inventario.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_inventario()
            print(f"Producto '{producto.nombre}' añadido ✅")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            eliminado = self.productos.pop(id_producto)
            self.guardar_inventario()
            print(f"Producto '{eliminado.nombre}' eliminado ✅")
        else:
            print("⚠️ El ID no existe en el inventario.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            self.guardar_inventario()
            print("Producto actualizado ✅")
        else:
            print("⚠️ El ID no existe en el inventario.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("⚠️ No se encontró ningún producto con ese nombre.")

    def mostrar_todos(self):
        if self.productos:
            print("\n--- Inventario Completo ---")
            for p in self.productos.values():
                print(p)
        else:
            print("El inventario está vacío.")


# ========================
# Menú interactivo
# ========================
def menu():
    inventario = Inventario()

    while True:
        print("\n========== MENÚ INVENTARIO ==========")
        print("1. Agregar pproducto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("0. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id_p = input("ID del producto: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_p, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_p = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (Enter para no actualizar datos): ")
            precio = input("Nuevo precio (Enter para no actualizar datos): ")
            inventario.actualizar_producto(
                id_p,
                int(cantidad) if cantidad else None,
                float(precio) if precio else None
            )

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "0":
            print("Saliendo... 👋")
            break
        else:
            print("⚠️ Opción inválida, intenta de nuevo.")


# ========================
# Ejecutar programa
# ========================
if __name__ == "__main__":
    menu()

