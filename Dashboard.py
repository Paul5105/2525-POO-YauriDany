import os

# =======================
# DASHBOARD PERSONALIZADO
# Autor: DANY YAURI
# =======================

def mostrar_codigo(ruta_script):
    try:
        with open(os.path.abspath(ruta_script), 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    print("\n====================================")
    print("   DASHBOARD POO - DANY YAURI")
    print("   Gestión de Tareas por Semana")
    print("====================================")

    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Parcial 01/Semana 02/Tarea Semana 02.py',
        '2': 'Parcial 01/Semana 03/Ejemplo de Programación Tradicional y POO.py',
        '3': 'Parcial 01/Semana 04/EjemplosMundoReal_POO..py',
        '4': 'Parcial 01/Semana 05/Tipos de datos, Identificadores.py',
        '5': 'Parcial 01/Semana 06/Clases, objetos, herencia, encapsulamiento y polimorfismo.py',
        '6': 'Parcial 01/Semana 07/Constructores y Destructores.py',
    }

    while True:
        print("\n¿Qué tarea deseas visualizar?")
        for key in opciones:
            print(f"{key} - {os.path.basename(opciones[key])}")
        print("0 - Salir")

        eleccion = input("Elige una opción: ")

        if eleccion == '0':
            print("Gracias por usar el Dashboard, ¡vuelve pronto! ✨")
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
            input("\nPresiona ENTER para regresar al menú...")
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    mostrar_menu()
