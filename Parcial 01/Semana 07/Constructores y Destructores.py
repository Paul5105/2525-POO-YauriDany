class Robot:
    def __init__(self, modelo, funcion):
        """
        Constructor: se ejecuta al crear un Robot.
        Inicializa modelo y función.
        """
        self.modelo = modelo     #Guardamos el modelo del robot.
        self.funcion = funcion   #También guardamos su función.
        print(f"🤖 Robot modelo '{self.modelo}' está activo y listo para {self.funcion}.")

    def operar(self):
        print(f"⚙️ Robot '{self.modelo}' está ejecutando su función: {self.funcion}.")

    def __del__(self):
        """
        Destructor: se ejecuta cuando el objeto se elimina.
        Aquí solo mostramos un mensaje.
        """
        print(f"🛑 Robot modelo '{self.modelo}' se ha apagado.")


# Código principal para probar
if __name__ == "__main__":
    print("🔁 Creando robots...\n")
#Creamos dos objetos de la clase robot
    r1 = Robot("25-POO", "limpieza")
    r2 = Robot("26-POO", "exploración")

    r1.operar()
    r2.operar()

#Eliminamos los objetos para activar el destructor.

    print("\n🗑️ Eliminando robots...")
    del r1
    del r2
