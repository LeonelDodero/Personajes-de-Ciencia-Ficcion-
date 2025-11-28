class Personaje:
    #Creamos un personaje segun nombre, especie, planeta, nivel de poder y su respectivo arbol de habilidades 
    def __init__(self, nombre, especie, planeta, nivel_poder,):
        self.nombre = nombre
        self.especie = especie
        self.planeta = planeta
        self.nivel_poder = nivel_poder
        self.habilidades = []        
        self.objetos = []
        self.poder_total = 0
        self.arbol_habilidades = None

        self.poder_total = nivel_poder
    
    def agregar_habilidad(self, habilidad):
        #Se agregan las habilidades y se suma el poder al poder total del personaje
        if habilidad in self.habilidades:
            print('Esta habilidad ya esta aprendida')
        else:
            self.habilidades.append(habilidad)        
            self.poder_total += habilidad.nivel_poder
            print(f"{self.nombre} aprendió la habilidad: {habilidad.nombre}")

    def eliminar_habilidad(self, habilidad):
        #Se elimina la habilidad y se resta el poder al poder total del personaje
        if habilidad in self.habilidades:
            self.habilidades.remove(habilidad)
            self.poder_total -= habilidad.nivel_poder
            print(f"{habilidad.nombre} se elimino de las habilidades de {self.nombre}")
        else:
            print('Esta habilidad no se encuentra')    

    def agregar_objeto(self, objeto):
        #Se agrega el objeto al personaje y se suma el poder extra al poder total del personaje
        if objeto in self.objetos:
            print('Este objeto ya se encuentra en el inventario')
        else:
            self.objetos.append(objeto)
            self.poder_total += objeto.poder_extra
            print(f"{self.nombre} obtuvo el objeto: {objeto.nombre} (+{objeto.poder_extra} poder)")
    
    def eliminar_objeto(self, objeto):
        #Se elimina el objeto de la lista de objetos del personaje y con esto se resta el poder del mismo
        if objeto in self.objetos:
            self.objetos.remove(objeto)
            self.poder_total -= objeto.poder_extra
            print(f"Se eliminó {objeto} de el inventario de {self.nombre}")
        else:
            print(f"{objeto.nombre} no se encuentra en el inventario de {self.nombre}")
            
    def mostrar_informacion(self):
        #Con esto vamos a poder ver la informacion que tiene cada personaje
        print('Nombre:', self.nombre)
        print('Especie:', self.especie)
        print('Planeta:', self.planeta)
        print('Nivel de poder:', self.nivel_poder)
        print('Poder total:', self.poder_total)
        print('Habilidades: ')
        if self.habilidades:
            for h in self.habilidades:
                print('-', h)
        else:
            print('Todavia no se aprendio ninguna habilidad.')
        print('-' * 30)
