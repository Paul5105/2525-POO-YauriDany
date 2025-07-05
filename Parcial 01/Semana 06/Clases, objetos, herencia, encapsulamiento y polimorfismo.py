#Desarrollo de un Programa en Python:##

#Utiliza PyCharm para desarrollar un programa que incluya los siguientes elementos:
#Al menos una clase base y una clase derivada, demostrando el concepto de herencia.
#Implementación de encapsulación en al menos una clase.
#Un ejemplo de polimorfismo, ya sea a través de métodos sobrescritos o utilizando argumentos múltiples/variables.

##Requisitos Específicos:##
#Define atributos y métodos claramente en tus clases.
#Crea instancias de tus clases y utiliza sus métodos para demostrar la funcionalidad de tu programa.


#Eleguí hacer un sistema de hechizos para un videojuego.
#Y comezamos con la clase base que sera hechizo

print("Sistema de Hechizos")

# Clase base: Hechizo
class Hechizo:
    def __init__(self, nombre, poder, mana):
        self._nombre = nombre         # Encapsulado
        self._poder = poder           # Encapsulado
        self._mana = mana             # Encapsulado

    def lanzar(self):
        return f"{self._nombre} lanza un hechizo genérico con poder {self._poder}."

    def mostrar_info(self):
        print(f"Hechizo: {self._nombre} | Poder: {self._poder} | Maná requerido: {self._mana}")

#La herencia de hechizo será (Hechizo de Fuego, Hechizo de Hielo, Hechizo Eléctrico).
#Encapsulamiento lo usamos en atributos con "_ como _nombre, _poder, _mana, etc".
#Polimorfismo será "lanzar()" el cuál se comporta de otra manera según el hechizo.

# Clase derivada: Hechizo de Fuego
class HechizoFuego(Hechizo):
    def __init__(self, nombre, poder, mana, temperatura):
        super().__init__(nombre, poder, mana)
        self._temperatura = temperatura  # Encapsulado

    # Polimorfismo: sobrescritura de método
    def lanzar(self):
        return f"{self._nombre} lanza una bola de fuego que quema con {self._temperatura}°C de calor."


# Clase derivada: Hechizo de Hielo
class HechizoHielo(Hechizo):
    def __init__(self, nombre, poder, mana, congelamiento):
        super().__init__(nombre, poder, mana)
        self._congelamiento = congelamiento  # Encapsulado

    def lanzar(self):
        return f"{self._nombre} lanza una ráfaga helada que congela durante {self._congelamiento} segundos."


# Clase derivada: Hechizo Eléctrico
class HechizoElectrico(Hechizo):
    def __init__(self, nombre, poder, mana, voltaje):
        super().__init__(nombre, poder, mana)
        self._voltaje = voltaje

    def lanzar(self):
        return f"{self._nombre} invoca un rayo de {self._voltaje} voltios. ¡Zas!"


# Crear objetos (hechizos)
fuego = HechizoFuego("Furia de fuego", 80, 50, 1200)
hielo = HechizoHielo("Aliento de hielo", 65, 40, 8)
electrico = HechizoElectrico("Descarga Solar", 90, 60, 15000)

# Mostrar información y lanzar hechizos
hechizos = [fuego, hielo, electrico]

for hechizo in hechizos:
    hechizo.mostrar_info()
    print(hechizo.lanzar())
    print("-" * 40)
#Este sistema de hechizos pueden utilizarlos dentro de x juego los magos.