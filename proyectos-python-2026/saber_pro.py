class SesionEstudio:

    def __init__(self,tema,duracion_minutos, completado):
        self.tema = tema
        self.duracion_minutos = duracion_minutos
        self.completado = completado
        self.completado = True

    def resumen(self):

        if self.completado == True:

            return  f"¡Felicidades!, Lo lograste realizar estos temas,{self.tema}, en este tiempo, {self.duracion_minutos}  "
        else:
            return  "No te preocupes, mañana continuas"
        

        
p1 = SesionEstudio("Lectura critica", 50, "True" )

print(p1.resumen())
#print(p1.resumen())


