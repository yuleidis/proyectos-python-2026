class SesionEstudio:
    def __init__ (self, tema, duracion_minutos, completado):

        self.tema = tema
        self.duracion_minutos = duracion_minutos
        self.completado = completado

# 1. Creamos las sesiones de estudio (tus objetos)
p1 = SesionEstudio("Lectura critica",50, True)
p2 = SesionEstudio("razonamiento cuantico",40, True)
p3 = SesionEstudio("Ingles", 30, False  ) # Esta no se completo

# 2. Guardamos los objetos dentro de una lista básica

mis_sesiones = [p1, p2, p3]

# 3.Creamos una variable para acumular los minutos

minutos_total = 0

# 4. Usamos un bucle 'for' para recorrer la lista

for sesion in mis_sesiones:
    #solo sumamos los minutos si la sesión fue completada
    if sesion.completado:
        minutos_total = minutos_total + sesion.duracion_minutos

print(f"¡Excelente trabajo! Has completado un total de {minutos_total} minutos de estudio.")