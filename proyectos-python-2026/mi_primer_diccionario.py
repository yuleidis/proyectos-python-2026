# 1.Creamos una sesión de estudio usando un diccionario
#Cada dato tiene una etiqueta (clave) y su información (valor)

sesion = {
    "tema": "Diccionarios en Python",
    "minutos": 45,
    "materia_saber_pro": "Razonamiento cuantitativo",
    "completado": True
}

# 2. ¿Cómo mostramos los datos en la terminal?
print("---📱 DATOS EXTRAÍDOS DEL DICCIONARIO ---")

#Accedemos a la información usando su etiqueta entre corchetes

print(f"📚 Tema de hoy: {sesion['tema']}")
print(f"⏱️ Tiempo dedicado: {sesion['minutos']} minutos")
print(f"🎯 Enfocado en: {sesion['materia_saber_pro']} ")

#Podemos modificar un dato fácilmente
sesion["minutos"] = 60
print(f"🔄 Tiempo actualizado: {sesion['minutos']} minutos")

