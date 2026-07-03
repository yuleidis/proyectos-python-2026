import json # Importamos la herramienta para manejar archivos JSON

historial_completo = []

def guardar_en_disco():
    #Guarda la lista de diccionarios en un archivo real
    with open("historial.json", "w", encoding="utf-8") as archivo:
        json.dump(historial_completo, archivo, indent = 4)

def cargar_desde_disco():
    global historial_completo
    try:
        # Intentamos leer el archivo si ya exite
        with open("historial.json", "r", encoding="utf-8") as archivo:
            historial_completo = json.load(archivo)

    except FileNotFoundError:
        #Si no existe, dejamos la lista vacía sin romper el programa
        historial_completo = []

def registrar_sesion():
    print("\n--- 📝 REGISTRAR NUEVA SESIÓN ---")
    tema = input("¿Qué tema específico estudiaste?:")
    
    # 1. SISTEMA DE SEGURIDAD: Validamos si el tema ya existe

    ya_existe = False

    for sesion in historial_completo:
        if sesion["tema"].lower() == tema.lower(): 
            ya_existe = True
            break # Si lo encuentra detiene la busqueda de inmediato


    if ya_existe:
        print(f"⚠️ ¡Atención El tema '{tema}' ya está resgistrado en tu historial.")
        print("Usa un nombre diferente o elimina la sesión anterior primero.")
        return #Este ' return' detiene la función aqui y no guarda nada
    
    #2. Si el tema no existe, el programa continúa normalmente abajo

    minutos = int(input("¿Cuántos minutos le dedicaste?:"))
    print("Selecciona la materia:\n1. Python\n2. Saber Pro")
    opc_materia = input("Elige (1 o 2): ")

    materia = "Python" if opc_materia == "1" else "Saber Pro"

    nueva_sesion = {"tema": tema, "minutos": minutos, "materia": materia}
    historial_completo.append(nueva_sesion)

    guardar_en_disco () # Guardamos automáticamente en el archivo
    print("✨ ¡Sesión guardada con éxito en el archivo historial.jso!\n")




def generar_reporte_clasificado():
    print("\n==================================================")
    print("\n--- 📊 REPORTE DE RENDIMIENTO CLASIFICADO ---")
    print("==================================================")

    if not historial_completo:
        print("⚠️ El historial está vacío. Registra sesiones primero.\n")
        return
    
    tot_python = 0
    tot_saber = 0

    #Cabecera de la tabla con espacios fijos
    #En python ':<25' significa: 'deja un espacio de 25 caracteres alineado a la izquierda'
    print(f"{'MATERIA':<15} | {'TEMA':<20} | {'DURACION':<10}")
    print("-" * 52)

    for sesion in historial_completo:
        materia_formato = f"[{sesion['materia']}]"
        tema_formato = sesion["tema"]
        minutos_formato = f"{sesion['minutos']} min"

        #Imprimimos la fila perfectamente alineada en columnas
        print(f"{materia_formato:<15} | {tema_formato:<20} | {minutos_formato:<10} ")


        #Sumamos a los acumuladores normales
        if sesion["materia"] == "Python":
            tot_python += sesion["minutos"] 
            

        else:
            tot_saber += sesion["minutos"]
        
    print("-" * 52)
    print(f"\n🔹 Total en programación Python: {tot_python} min.")
    print(f"🔹 Total en Saber Pro: {tot_saber} min.\n")   
    print("==================================================\n") 





def eliminar_sesion():
    print("\n--- 🗑️ ELIMINAR SESIÓN DE ESTUDIO ---")
    if not historial_completo:
        print("⚠️ El historial está vacío. No hay nada que eliminar.\n")
        return
    
    tema_a_borrar = input("Escribe el nombre EXACTO del tema que quieres eliminar: ")

    encontrado = False

    #Recorremos la lista para buscar el diccionario que coincida
    for sesion in historial_completo:
        if sesion["tema"].lower() == tema_a_borrar.lower():
            historial_completo.remove(sesion) # Lo borramos de la lista
            encontrado = True
            break #Salimos del bucle una vez borrado

    if encontrado:
        guardar_en_disco() # Guardamos los cambio den el archivo .json
        print(f"✨ ¡La sesión de '{tema_a_borrar}' fue eliminada con éxito!\n")

    else:
     print(f"❌ No se encontró ninguna sesión con el tema '{tema_a_borrar}'.\n")







# Al arrancar el programa, cargamos los datos guardados anteriormente

cargar_desde_disco()

while True:
    print("--- 📱 SISTEMA PERMANENTE MULTI-PROYECTO ---")
    print("1. Registrar nueva sesión de estudio")
    print("2. Ver reporte clasificado por materia")
    print("3. Eliminar una sesión por material")
    print("4. Salir del programa")

    opcion = input("Elige una opción (1, 2,3 o 4):")


    if opcion == "1":
        registrar_sesion()
    elif opcion == "2":
        generar_reporte_clasificado()

    elif opcion == "3":
        eliminar_sesion()

    elif opcion == "4":
        print("👋¡ Datos asegurados! Buen descanso. ¡Chao!")
        break

    else:
        print("❌ Opción inválida. \n")

