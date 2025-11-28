# Se crea el nodo del arbol de evolucion de habilidades
class NodoHabilidad:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        self.mejoras = []   

    def agregar_mejora(self, nodo_hijo):
        self.mejoras.append(nodo_hijo)

# Se crea el arbol general de habilidades
class ArbolHabilidades:
    def __init__(self, raiz=None):
        self.raiz = raiz
    
    def mostrar(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.raiz
        print("   " * nivel + f"{nodo.habilidad.nombre} (Poder {nodo.habilidad.nivel_poder})")
        for mejora in nodo.mejoras:
            self.mostrar(mejora, nivel + 1)
    
    def buscar(self, nodo, nombre):
        #Se crea una funcion para poder buscar una habilidad por nombre
        if nodo is None:
            return None
        if nodo.habilidad.nombre == nombre:
            return nodo
        for mejora in nodo.mejoras:
            resultado = self.buscar(mejora, nombre)
            if resultado:
                return resultado
        return None
    
    def agregar_mejora(self, nombre_base, habilidad_mejora):
        #Se crea una funcion para poder mejorar las habilidades
        nodo_base = self.buscar(self.raiz, nombre_base)
        if nodo_base:
            nodo_base.agregar_mejora(NodoHabilidad(habilidad_mejora))
            print(f"Se agregó la mejora '{habilidad_mejora.nombre}' a '{nombre_base}'")
        else:
            print(f"No se encontró la habilidad base '{nombre_base}'")
