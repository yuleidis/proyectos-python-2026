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
    #Definimos los códigos de color
    AZUL = "\033[94m"
    VERDE = "\033[92m"
    ROJO = "\033[91m"
    RESET ="\033[0m" # Sirve para volver al color normal



    minutos_totales = 0
    print(f"\n{AZUL}--- 📚 DETALLE DE SESIONES ESTUDIADAS ---{RESET}")

    try:
        with open("progreso.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                tema = datos[0] # posición 0: El nombre del tema
                minutos = int(datos[1]) # Posición 1: Los minutos como números

                #Mostramos cada sesión individualmente en la terminal
                print(f"• {tema}: {VERDE}{minutos} minutos{RESET}")

                #seguimos acumulando el total
                minutos_totales = minutos_totales + int(datos[1])

        print(f"\n📊 Total acumulado: {VERDE}{minutos_totales}{RESET} minutos estudiados.\n")
        
    except FileNotFoundError:
         print(f"{ROJO} ⚠️ El archivo 'progreso.txt' no existe.{RESET}.\n")


# Bucle principal del programa
while True:
    VERDE = "\033[92m"
    RESET = "\033[0m"
    ROJO = "\033[91m"


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
        print(f"👋 {VERDE}¡Buen trabajo hoy! Sigue así. ¡Feliz fin de semana!{RESET}")
        break
    else:
        print(f"❌ Opción {ROJO}inválida.{RESET} Elige 1, 2 o 3.\n")
