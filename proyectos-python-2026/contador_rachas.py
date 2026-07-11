# 1. Variable GLOBAL que iniciará tu racha en cero
dias_de_racha = 0

def registrar_victoria_diaria():
    # 2. Traemos la variable de afuera paa poder modificarla
    global dias_de_racha

    #Sumamos un día a tu racha de éxito
    dias_de_racha = dias_de_racha + 1

    print("\n==============================================")
    print("🔥 ¡Felicidades! Completaste tus metas de hoy.")
    print(f"🏆 Tu racha actual ha subido a: {dias_de_racha} días seguidos.")
    print("==============================================")

def romper_racha():
    global dias_de_racha
    dias_de_racha = 0
    print("\n😢 Oh no, la racha ha vuelto a 0. ¡No te rindas, hoy vuelves a empezar!")

# 3. Motor interactivo para jugar en la terminal

while True:

    print("\n--- 🏁 PANEL DE CONTROL DE RACHAS (FUEGO) ---")
    print("1. Registrar victoria de hoy (¡Estudié!)")
    print("2. Registrar día perdido (No pude estudiar)")
    print("3. Ver racha actual")
    print("4. Salir")

    opcion = input("Elige una opción (1, 2, 3 o 4)")

    if opcion == "1":
        registrar_victoria_diaria()

    elif opcion == "2":
        romper_racha()
    elif opcion == "3":
        print(f"\n📊 Estado: Llevas {dias_de_racha} días manteniendo el hábito vivo.")
    elif opcion == "4":
         print("\n👋 ¡Buen entrenamiento de sábado! Sigue así. ¡Chao!")
    else:
        print("\n❌ Opción inválida. Elige un número del 1 al 4.")
