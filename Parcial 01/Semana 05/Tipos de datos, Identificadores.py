#El siguiente programa se encarga de saludar según la hora que estemos en formato de 24 horas.
# Solicitamos la hora como número entero de 0 a 23 para que cumpla el formato de 24 horas, usando el identificador snake case.
hora_actual = int(input("Ingrese la hora actual (0 a 23)"))

# Verificar si la hora es válida.
es_valida = 0 <= hora_actual <= 23  # booleano

# Mostrar saludo según la hora (24 horas).
if es_valida:
    if 6 <= hora_actual < 12:
        saludo = "¡Buenos días! Que tenga un buen inicio de jornada"
    elif 12 <= hora_actual < 18:
        saludo = "¡Buenas tardes! Es hora del almuerzo"
    else:
        saludo = "¡Buenas noches! Es hora de descansar"

    # Mostrar el saludo.
    print("\n--- Saludo ---")
    print(saludo)
else:
    print("Hora no válida. Debe estar entre 0 y 23.")
#Gracias
