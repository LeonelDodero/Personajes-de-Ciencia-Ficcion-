#Del Peral Romina, Dodero Leonel Comisión 5

from habilidad import Habilidad
from objeto import Objeto
from personaje import Personaje
from arbolPersonaje import ArbolPersonajes, NodoPersonaje
from arbolHabilidad import ArbolHabilidades, NodoHabilidad
from gestorMisiones import Mision, GestorMisiones
from grafo import Grafo  
from grafoHabilidades import GrafoHabilidades

# Invocaciones

# Se crean los personajes

Goku = Personaje('Goku', 'Saiyajin', 'Vegeta', 50)
Gohan = Personaje('Gohan', 'Saiyajin', 'Tierra', 80)
Freezer = Personaje('Freezer', 'Demonio del Frío', 'Chalon', 100)
Piccolo = Personaje('Piccolo', 'namekiano', 'Namekusein', 40)

# Se crean las habilidades

Kamehameha = Habilidad('Kamehameha', 1, 20)
Potenciado = Habilidad('Kamehameha Potenciado', 2, 30)
Super = Habilidad('Super Kamehameha', 3, 50)
Super_saiyajin = Habilidad('Super Saiyajin', 1, 50)

# Se crean los objetos

Espada_Z = Objeto('Espada Z', 20)
Semilla = Objeto('Semilla del Ermitaño', 10)

# Se crea el gestor de misiones

gestor = GestorMisiones()

# Se crean misiones
m1 = Mision("Defender la Tierra", nivel_amenaza=1, recompensa=1000)
m2 = Mision("Entrenar en el planeta Bills", nivel_amenaza=3, recompensa=300)
m3 = Mision("Detener a Freezer", nivel_amenaza=2, recompensa=800)

# Agregar a la cola
gestor.agregar_mision(m1)
gestor.agregar_mision(m2)
gestor.agregar_mision(m3)

gestor.mostrar_misiones()

# Atender misiones según prioridad
gestor.proxima_mision()  
gestor.proxima_mision()  
gestor.proxima_mision()  
gestor.proxima_mision()  



Goku.mostrar_informacion()
Goku.agregar_habilidad(Kamehameha)
Goku.agregar_habilidad(Super_saiyajin)
Gohan.agregar_objeto(Espada_Z)
Gohan.agregar_habilidad(Super_saiyajin)
Goku.mostrar_informacion()
Gohan.mostrar_informacion()

# Se crea el arbol binario
arbol = ArbolPersonajes()

# Se insertan los personajes
arbol.insertar(Goku)
arbol.insertar(Gohan)
arbol.insertar(Freezer)
arbol.insertar(Piccolo)

# Se muestra en orden de poder
arbol.mostrar_en_orden()

nodo_base = NodoHabilidad(Kamehameha)
arbol = ArbolHabilidades(nodo_base)

arbol.agregar_mejora("Kamehameha", Potenciado)
arbol.agregar_mejora("Kamehameha Potenciado", Super)
print("Árbol de habilidades de Goku:")
arbol.mostrar()

Goku.mostrar_informacion()

# Se crea el grafo

universo = Grafo()

# Nodos

universo.agregar_nodo("Tierra")
universo.agregar_nodo("Namekusein")
universo.agregar_nodo("Planeta Vegeta")
universo.agregar_nodo("Nave de Freezer")
universo.agregar_nodo("Base Saiyajin")

# Se agregan las rutas, alianzas o conflictos

universo.agregar_arista("Tierra", "Namekusein", "ruta")
universo.agregar_arista("Tierra", "Planeta Vegeta", "alianza")
universo.agregar_arista("Namekusein", "Nave de Freezer", "conflicto")
universo.agregar_arista("Planeta Vegeta", "Base Saiyajin", "ruta")
universo.agregar_arista("Base Saiyajin", "Nave de Freezer", "ruta")

universo.mostrar()

# Se asocian los personajes con los planetas o bases

universo.agregar_arista("Goku", "Tierra", "vive_en")
universo.agregar_arista("Gohan", "Tierra", "vive_en")
universo.agregar_arista("Freezer", "Nave de Freezer", "comanda")

# Se muestra la ruta mas corta de un personaje hasta otro

ruta = universo.bfs("Goku", "Freezer")
print("Ruta más corta:", ruta)

# Se da un orden óptimo de entrenamiento del personaje

grafo = GrafoHabilidades()

grafo.agregar_dependencia(Kamehameha, Potenciado)
grafo.agregar_dependencia(Potenciado, Super)
grafo.agregar_dependencia(Potenciado, Super_saiyajin)

plan = grafo.orden_topologico()

print("Orden óptimo de entrenamiento:")
for h in plan:
    print("-", h.nombre)

# Se utiliza Dijkstra para mostrar el camino más óptimo

universo = Grafo()

universo.agregar_arista("Tierra", "Namek", "ruta espacial", 15)
universo.agregar_arista("Tierra", "Kaio del Norte", "camino serpenteante", 30)
universo.agregar_arista("Namek", "Freezer Planet", "hiper-ruta", 10)
universo.agregar_arista("Kaio del Norte", "Freezer Planet", "teletransporte", 5)

camino, costo = universo.dijkstra("Tierra", "Freezer Planet")

print("Camino óptimo:", camino)
print("Costo total:", costo)
