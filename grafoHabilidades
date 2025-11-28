import heapq

class Grafo:
    def __init__(self):
        self.adyacencias = {}  
    
    def agregar_nodo(self, nodo):
        if nodo not in self.adyacencias:
            self.adyacencias[nodo] = []

    def agregar_arista(self, nodo1, nodo2, tipo="ruta", peso = 1):
        self.agregar_nodo(nodo1)
        self.agregar_nodo(nodo2)
        self.adyacencias[nodo1].append((nodo2, tipo, peso))
        self.adyacencias[nodo2].append((nodo1, tipo, peso))  

    def dijkstra(self, inicio, objetivo):
        distancias = {nodo: float("inf") for nodo in self.adyacencias}
        distancias[inicio] = 0

        anterior = {nodo: None for nodo in self.adyacencias}

        cola = [(0, inicio)]  

        while cola:
            costo_actual, nodo_actual = heapq.heappop(cola)

            if nodo_actual == objetivo:
                break

            if costo_actual > distancias[nodo_actual]:
                continue

            for vecino, tipo, peso in self.adyacencias[nodo_actual]:
                nuevo_costo = costo_actual + peso

                if nuevo_costo < distancias[vecino]:
                    distancias[vecino] = nuevo_costo
                    anterior[vecino] = nodo_actual
                    heapq.heappush(cola, (nuevo_costo, vecino))

        camino = []
        actual = objetivo
        while actual is not None:
            camino.insert(0, actual)
            actual = anterior[actual]

        return camino, distancias[objetivo]

    def mostrar(self):
        print("Mapa del Universo:")
        for nodo, vecinos in self.adyacencias.items():
            print(f"{nodo}, {vecinos}")
        print("-" * 40)

    def bfs(self, inicio, objetivo):
        from collections import deque
        
        visitados = set()
        cola = deque([(inicio, [inicio])])  

        while cola:
            nodo, camino = cola.popleft()
            if nodo == objetivo:
                return camino  
            if nodo not in visitados:
                visitados.add(nodo)

                for vecino, tipo, peso in self.adyacencias.get(nodo, []):
                    if vecino not in visitados:
                        cola.append((vecino, camino + [vecino]))
        
        return None  

    def dfs(self, inicio, objetivo, visitados=None, camino=None):
        if visitados is None:
            visitados = set()
        if camino is None:
            camino = [inicio]

        if inicio == objetivo:
            return camino

        visitados.add(inicio)

        for vecino, tipo, peso in self.adyacencias.get(inicio, []):
            if vecino not in visitados:
                resultado = self.dfs(vecino, objetivo, visitados, camino + [vecino])
                if resultado:
                    return resultado

        return None
