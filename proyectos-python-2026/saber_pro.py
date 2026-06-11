class SesionEstudio:

    def __init__(self,tema,duracion_minutos, completado):
        self.tema = tema
        self.duracion_minutos = duracion_minutos
        self.completado = completado
      

    def resumen(self):

        if self.completado == True:

            return  f"¡Felicidades!, Lo lograste estudiar este tema,{self.tema}, en este tiempo, {self.duracion_minutos}  "
        else:
            return  f"No te preocupes, mañana continuas con {self.tema}."
        

        
p1 = SesionEstudio("Lectura critica", 50, True)
p2 = SesionEstudio("Razonamiento Cuantitativo", 40, False)

print(p1.resumen())
print(p2.resumen())

