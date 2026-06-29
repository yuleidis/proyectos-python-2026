# Lista global para almacenar los diccionarios de cada sesión

historial_completo = []

def registrar_sesion():
    print("\n---📝 REGISTRAR NUEVA SESIÓN ---")
    tema = input("¿Qué tema específico estudiaste?: ")
    minutos = int(input("¿Cuántos minutos le dedicaste?: "))


    print("Selecciona la materia:")
    print("1. Python")
    print("2. Saber pro")
    opc_materia = input("Elige (1 o 2): ")

    materia = "Python" if opc_materia == "1" else "Saber pro"

    #Creamos el diccionario con las etiquetas

    nueva_sesion = {"tema": tema, "minutos": minutos, "materia": materia}
    historial_completo.append(nueva_sesion)
    print("✨ ¡Sesión guardada con éxito en la lista!\n")


def generar_reporte_clasificado():
    print("\n--- 📊 REPORTE DE RENDIMIENTO CLASIFICADO ---")
    if not historial_completo:
       print("⚠️ El historial está vacío. Registra sesiones primero.\n")
       return 

    tot_python = 0
    tot_saber = 0

    for sesion in historial_completo:
        if sesion["materia"] == "Python":
            tot_python += sesion["minutos"]

        else:
            tot_saber += sesion["minutos"]
            print(f"📝 [Saber Pro] {sesion['tema']}: {sesion['minutos']} min")

    print("\n⏱️ TIEMPOS TOTALES ACUMULADOS:")
    print(f"🔹 Total en Programación Python: {tot_python} minutos.")
    print(f"🔹 Total en Pruebas Saber Pro: {tot_saber} minutos.\n")



    # Motor principal del programa

while True:

        print("--- 📱SISTEMA DE CONTROL MULTI-PROYECTO ---")
        print("1. Registrar nueva sesión de estudio")
        print("2. Ver reporte clasificado por materia")
        print("3. Salir del programa")
          

        opcion = input("Elige una opción (1, 2 o 3): ")

        if opcion == "1":
            registrar_sesion()

        elif opcion == "2":
            generar_reporte_clasificado()

        elif opcion == "3":
            print("👋 ¡Excelente semana de trabajo! Disfruta tu fin de semana. ¡Chao!")
            break

        else:
            print("❌ Opción inválida. Intenta de nuevo.\n")



