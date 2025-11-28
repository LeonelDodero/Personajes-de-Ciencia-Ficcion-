class Objeto:
    #Creamos el objeto el cual va a tener un poder extra que se va a agregar al poder de cada personaje
    def __init__(self, nombre, poder_extra = 0):
        self.nombre = nombre
        self.poder_extra = poder_extra
    
    def __str__(self):
        if self.poder_extra > 0:
            return f"{self.nombre} (+{self.poder_extra} poder)"
        else:
            return self.nombre
