"""
Para hoy, en tu segundo bloque de programación de las 02:00 PM, tenemos el reto definitivo de la semana: crear tu primera aplicación interactiva completa.
"""

def guardar_sesion():
    tema = input("¿Qué tema estudiaste hoy?")
    minutos = input("¿Cuántos minutos le dedicaste?:")

    try:
        with open("progreso.txt","a", encoding ="utf-8") as archivo:
            archivo.write(f"{tema},{minutos}\n")
        print("✨ ¡Sesión guardada con éxito! \n") 
    except Exception as e:
        print(f"❌ Error al guardar: {e}\n")


def ver_reporte():
    minutos_totales = 0
    try:
        with open("progreso.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                minutos_totales = minutos_totales + int(datos[1])
            print(f"📊 Reporte Actualizado: Llevas {minutos_totales} minutos estudiados en total.\n")
    except FileNotFoundError:
         print("⚠️ El archivo 'progreso.txt' no existe. Registra una sesión primero.\n")


# Bucle principal del programa
while True:
    print("--- 📝 CONTROL DE ESTUDIO MULTI-PROFESIONAL ---")
    print("1. Registrar nueva sesión de estudio")
    print("2. Ver reporte de minutos totales")
    print("3. Salir del programa")

    option = input("Elige una opción (1, 2 o 3): ")

    if option == "1":
        guardar_sesion()

    elif option == "2":
        ver_reporte()
    elif option == "3":
        print("👋 ¡Buen trabajo hoy! Sigue así. ¡Feliz fin de semana!")
        break
    else:
        print("❌ Opción inválida. Elige 1, 2 o 3.\n")
