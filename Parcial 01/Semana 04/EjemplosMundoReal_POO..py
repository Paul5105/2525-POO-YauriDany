#Sistema de estacionamiento en la ciudad de Azogues

# Clase Vehiculo representa un carro o moto
class Vehiculo:
    def __init__(self, placa, tipo):
        self.placa = placa
        self.tipo = tipo

    def mostrar_info(self):
        return f"Placa: {self.placa} | Tipo: {self.tipo}"


# Clase Estacionamiento administra los vehículos
class Estacionamiento:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.vehiculos = []

    def ingresar_vehiculo(self, vehiculo):
        if len(self.vehiculos) < self.capacidad:
            self.vehiculos.append(vehiculo)
            print(f"Vehículo {vehiculo.placa} ingresado correctamente.")
        else:
            print("Estacionamiento lleno. No se puede ingresar más vehículos.")

    def retirar_vehiculo(self, placa):
        for v in self.vehiculos:
            if v.placa == placa:
                self.vehiculos.remove(v)
                print(f"Vehículo {placa} retirado del estacionamiento.")
                return
        print(f"No se encontró ningún vehículo con placa {placa}.")

    def mostrar_estacionamiento(self):
        print(f"\n--- {self.nombre} - Azogues ---")
        if not self.vehiculos:
            print("No hay vehículos en el estacionamiento.")
        else:
            for v in self.vehiculos:
                print(v.mostrar_info())
        print(f"Espacios disponibles: {self.capacidad - len(self.vehiculos)}\n")


# Programa principal
if __name__ == "__main__":
    parqueadero = Estacionamiento("Parking Azogues Centro", capacidad=3)

    # Ingresar vehículos
    auto1 = Vehiculo("ABC123", "Auto")
    moto1 = Vehiculo("XYZ789", "Moto")

    parqueadero.ingresar_vehiculo(auto1)
    parqueadero.ingresar_vehiculo(moto1)

    parqueadero.mostrar_estacionamiento()

    # Retirar un vehículo
    parqueadero.retirar_vehiculo("ABC123")

    parqueadero.mostrar_estacionamiento()
