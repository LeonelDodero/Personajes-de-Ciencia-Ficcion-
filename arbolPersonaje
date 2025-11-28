# Se crea el nodo del arbol de personajes
class NodoPersonaje:
    def __init__(self, personaje):
        self.personaje = personaje  
        self.izquierdo = None
        self.derecho = None

# Se crea el arbol de personajes segun su nivel de poder
class ArbolPersonajes:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, personaje):
        nuevo_nodo = NodoPersonaje(personaje)

        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)

# Ordena el arbol segun su nivel de poder para que sea un arbol binario de busqueda
    def _insertar_recursivo(self, actual, nuevo_nodo):
        if nuevo_nodo.personaje.poder_total < actual.personaje.poder_total:
            if actual.izquierdo is None:
                actual.izquierdo = nuevo_nodo
            else:
                self._insertar_recursivo(actual.izquierdo, nuevo_nodo)
        else:
            if actual.derecho is None:
                actual.derecho = nuevo_nodo
            else:
                self._insertar_recursivo(actual.derecho, nuevo_nodo)
    
    def mostrar_en_orden(self):
        print("Personajes ordenados por poder total:")
        self._mostrar_en_orden_rec(self.raiz)
        print('-' * 30)

    def _mostrar_en_orden_rec(self, nodo):
        if nodo is not None:
            self._mostrar_en_orden_rec(nodo.izquierdo)
            p = nodo.personaje
            print(f"{p.nombre} - Poder total: {p.poder_total}")
            self._mostrar_en_orden_rec(nodo.derecho)
