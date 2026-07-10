# 1. Variable GLOBAL que lleva la cuenta total de minutos
minutos_totales_semana = 400

def agregar_estudio(minutos_hoy):
    # 2. Con esta palabra clave le damos permiso a la funcion de MODIFICAR la variable de afuera
    global minutos_totales_semana

    #Modificamos el valor de la variable global de forma directa
    minutos_totales_semana = minutos_totales_semana + minutos_hoy
    print(f"✨ ¡Se han sumado {minutos_hoy} minutos al historial!")

# 3. Probamos el funcionamiento en la terminal

print("--- 🛰️ ACTUALIZADOR GLOBAL DE DATOS ---")
print(f"Minutos iniciales: {minutos_totales_semana}")

agregar_estudio(50) # Llamamos a la función

print(f"Minutos actualizados: {minutos_totales_semana}") #El valor cambió afuera