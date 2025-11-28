class Habilidad:
    
    #Creamos la habilidad que va a tener un nombre, un nivel de habilidad que va a poder ir evolucionando y un nivel de poder que va a incrementar segun el nivel de la habilidad
    def __init__(self, nombre, nivel_habilidad, nivel_poder):
        self.nombre = nombre
        self.nivel_habilidad = nivel_habilidad
        self.nivel_poder = nivel_poder

    def __str__(self):
        return f"{self.nombre} (Nivel {self.nivel_habilidad}, Poder {self.nivel_poder})"
