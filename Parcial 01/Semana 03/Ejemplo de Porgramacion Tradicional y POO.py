print("##Programacion Tradicional##")

#Implementa una solución utilizando estructuras de funciones.
#Define funciones para la entrada de datos diarios (temperaturas) y el cálculo del promedio semanal.
#Organiza el código de manera lógica y funcional utilizando la programación tradicional.

# Lista con las temperaturas de los 7 días
temperaturas = [21.3, 26.0, 22.6, 24.3, 19.9, 26.0, 22.7]

# Función para mostrar las temperaturas ingresadas
def mostrar_temperaturas():
    print("Temperaturas de la semana Tradicional:")
    for i, temp in enumerate(temperaturas):
        print(f"  Día {i + 1}: {temp} °C")

# Función para calcular el promedio
def calcular_promedio():
    if len(temperaturas) == 0:
        return 0
    return sum(temperaturas) / len(temperaturas)

# Uso de funciones
mostrar_temperaturas()
promedio = calcular_promedio()

# Mostrar el resultado
print("Promedio semanal (Tradicional):", round(promedio, 2), "°C")

print("##Programación Orientada a Objetos (POO)##")

#Diseña una solución utilizando el paradigma de POO.
#Crea una clase que represente la información diaria del clima.
#Utiliza métodos de la clase para ingresar datos y calcular el promedio semanal.
#Asegúrate de aplicar conceptos como encapsulamiento, herencia o polimorfismo según sea apropiado.


# Ejemplo: Promedio semanal del clima (con temperaturas fijas)
class ClimaSemanal:
    def __init__(self):
        # Encapsulamos las temperaturas en un atributo privado
        self._temperaturas = [22.5, 23.0, 24.1, 25.3, 24.8, 23.9, 22.7]

    def mostrar_temperaturas(self):
        print("Temperaturas de la semana (POO):")
        for i, temp in enumerate(self._temperaturas):
            print(f"  Día {i + 1}: {temp} °C")

    def calcular_promedio(self):
        if len(self._temperaturas) == 0:
            return 0
        return sum(self._temperaturas) / len(self._temperaturas)

# Crear el objeto y usar sus métodos
clima = ClimaSemanal()
clima.mostrar_temperaturas()
promedio = clima.calcular_promedio()
print("Promedio semanal (POO):", round(promedio, 2), "°C")

#Texto Comparativo:
#Programación Tradicional:#
#Usa funciónes y variables globales.
#No se usan claves
#No se usan objetos
#Estilo Lineal y Sencillo

#Programación Orientada a Objetos
#Encapsula las clases y los métodos.
#Fácil de reutilizar
#Facilita la organización del código.