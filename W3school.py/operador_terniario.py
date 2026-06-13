"""En lugar de Elif:
El operador ternario se puede utilizar en lugar de elifen sentencias if más largas:"""

"""Ejemplo
Asignar:
- "Vie" si numes 5
- "Sáb" si numes 6
- "Dom" si numes 7
- de lo contrario asignar "día de la semana":"""

num = 6

x = "Fri" if num == 5 else "sab" if num == 6 else "sun" if num == 7 else "weekday"

print(x)