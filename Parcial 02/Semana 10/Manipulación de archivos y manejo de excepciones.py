import json
import os

class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, "r", encoding="utf-8") as f:
                    self.productos = json.load(f)
            else:
                self.productos = {}
        except json.JSONDecodeError:
            print("⚠️ Error al leer el archivo JSON. Se inicializa inventario vacío.")
            self.productos = {}

    def guardar_inventario(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump(self.productos, f, indent=4, ensure_ascii=False)
        except PermissionError:
            print("❌ No tienes permisos para escribir en el archivo.")

    def añadir_producto(self, producto):
        if producto["ID"] in self.productos:
            print("❌ El ID ya existe. No se puede añadir.")
        else:
            self.productos[producto["ID"]] = producto
            self.guardar_inventario()
            print("✅ Producto añadido con éxito al inventario.json")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            print("✅ Producto eliminado correctamente.")
        else:
            print("❌ No se encontró el producto con ese ID.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto]["cantidad"] = cantidad
            if precio is not None:
                self.productos[id_producto]["precio"] = precio
            self.guardar_inventario()
            print("✅ Producto actualizado en inventario.json")
        else:
            print("❌ No existe un producto con ese ID.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p["nombre"].lower()]
        return encontrados

    def mostrar_todos(self):
        if self.productos:
            for p in self.productos.values():
                print(p)
        else:
            print("📂 El inventario está vacío.")


# =======================
# PROGRAMA PRINCIPAL
# =======================

def menu():
    inventario = Inventario()

    while True:
        print("\n=== SISTEMA DE INVENTARIO ===")
        print("1. Agregar producto")
        print("2. Borrar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            id_prod = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.añadir_producto({
                "ID": id_prod,
                "nombre": nombre,
                "cantidad": cantidad,
                "precio": precio
            })
        elif opcion == "2":
            id_prod = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_prod)
        elif opcion == "3":
            id_prod = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deja vacío si no deseas cambiar): ")
            precio = input("Nuevo precio (deja vacío si no deseas cambiar): ")
            inventario.actualizar_producto(
                id_prod,
                cantidad=int(cantidad) if cantidad else None,
                precio=float(precio) if precio else None
            )
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("❌ No se encontraron coincidencias.")
        elif opcion == "5":
            inventario.mostrar_todos()
        elif opcion == "0":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    menu()