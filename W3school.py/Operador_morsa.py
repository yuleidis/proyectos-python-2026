#EJEMPLO 1


"""entrada = input("Escribe algo")

while entrada != "salir":
    print("Escribiste" + entrada)
    entrada = input("Escribe algo") """


#CODIGO CON MORSA

"""while (entrada := input("Escribe algo")) != "salir":
    print("Escribiste" + entrada)
"""
#EJEMPLO 2
# ##CODIGO SIN EL OPERADOR MORSA
#2. Validar respuestas en bloques if

"""entrada = input ("Escribe tu contraseña")

#forma tradicional
longitud = len(entrada)

if longitud < 8:
    print(f"Contraseña muy corta tienes {longitud} caracteres")"""

#USANDO EL OPERADOR MOSA

"""entrada = input("Digite la contraseña")

if (entrada := len(entrada)) < 8:
    print(f"contraseña muy corta. Tienes {entrada} caracteres.")"""




