# SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla siendo inmutable usado para poner el titulo y autor.

        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"[{self.isbn}] {self.info[0]} - {self.info[1]} ({self.categoria})"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}       # Diccionario {ISBN: Libro}
        self.usuarios = {}     # Diccionario {ID: Usuario}
        self.ids_usuarios = set()  # Conjunto para IDs únicos

    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"⚠️ El libro con ISBN {libro.isbn} ya existe.")
        else:
            self.libros[libro.isbn] = libro
            print(f"✅ Libro '{libro.info[0]}' agregado con éxito.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            eliminado = self.libros.pop(isbn)
            print(f"❌ Libro '{eliminado.info[0]}' eliminado.")
        else:
            print("⚠️ No se encontró un libro con ese ISBN.")

    def registrar_usuario(self, usuario):
        if usuario.user_id in self.ids_usuarios:
            print("⚠️ Ese ID de usuario ya está registrado.")
        else:
            self.usuarios[usuario.user_id] = usuario
            self.ids_usuarios.add(usuario.user_id)
            print(f"✅ Usuario '{usuario.nombre}' registrado con éxito.")

    def dar_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            eliminado = self.usuarios.pop(user_id)
            self.ids_usuarios.remove(user_id)
            print(f"❌ Usuario '{eliminado.nombre}' eliminado.")
        else:
            print("⚠️ No se encontró un usuario con ese ID.")

    def prestar_libro(self, user_id, isbn):
        if user_id not in self.usuarios:
            print("⚠️ Usuario no registrado.")
            return
        if isbn not in self.libros:
            print("⚠️ El libro no está disponible.")
            return

        usuario = self.usuarios[user_id]
        libro = self.libros.pop(isbn)
        usuario.libros_prestados.append(libro)
        print(f"📚 Libro '{libro.info[0]}' prestado a {usuario.nombre}.")

    def devolver_libro(self, user_id, isbn):
        if user_id not in self.usuarios:
            print("⚠️ Usuario no registrado.")
            return

        usuario = self.usuarios[user_id]
        libro_a_devolver = None
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                libro_a_devolver = libro
                break

        if libro_a_devolver:
            usuario.libros_prestados.remove(libro_a_devolver)
            self.libros[isbn] = libro_a_devolver
            print(f"✅ Libro '{libro_a_devolver.info[0]}' devuelto.")
        else:
            print("⚠️ Ese usuario no tiene prestado ese libro.")

    def buscar_libro(self, criterio, valor):
        print(f"🔎 Resultados de búsqueda ({criterio} = {valor}):")
        encontrados = []
        for libro in self.libros.values():
            if (criterio == "titulo" and valor.lower() in libro.info[0].lower()) \
               or (criterio == "autor" and valor.lower() in libro.info[1].lower()) \
               or (criterio == "categoria" and valor.lower() in libro.categoria.lower()):
                encontrados.append(libro)
        if encontrados:
            for l in encontrados:
                print("   ", l)
        else:
            print("⚠️ No se encontraron resultados.")

    def listar_prestamos_usuario(self, user_id):
        if user_id not in self.usuarios:
            print("⚠️ Usuario no registrado.")
            return
        usuario = self.usuarios[user_id]
        print(f"📖 Libros prestados a {usuario.nombre}:")
        if usuario.libros_prestados:
            for libro in usuario.libros_prestados:
                print("   ", libro)
        else:
            print("   (ningún libro prestado)")


# ===============================
# MENÚ INTERACTIVO
# ===============================
def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n=== 📚 MENÚ BIBLIOTECA DIGITAL ===")
        print("1. Agregar libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar préstamos de un usuario")
        print("9. Salir")

        opcion = input("👉 Selecciona una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            isbn = input("ISBN del libro a eliminar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            user_id = input("ID del usuario: ")
            usuario = Usuario(nombre, user_id)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            user_id = input("ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(user_id)

        elif opcion == "5":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(user_id, isbn)

        elif opcion == "6":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(user_id, isbn)

        elif opcion == "7":
            criterio = input("Buscar por (titulo/autor/categoria): ").lower()
            valor = input("Valor de búsqueda: ")
            biblioteca.buscar_libro(criterio, valor)

        elif opcion == "8":
            user_id = input("ID del usuario: ")
            biblioteca.listar_prestamos_usuario(user_id)

        elif opcion == "9":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("⚠️ Opción no válida, intenta de nuevo.")


# Ejecutar menú
if __name__ == "__main__":
    menu()
