import heapq
# Se crean las misiones 
class Mision:
    def __init__(self, nombre, nivel_amenaza, recompensa):
        self.nombre = nombre
        self.nivel_amenaza = nivel_amenaza    
        self.recompensa = recompensa

    def __lt__(self, otra): #Less than (menor que)
        # Compara por nivel de amenaza 
        return self.nivel_amenaza < otra.nivel_amenaza

    def __str__(self):
        return f"{self.nombre} (Amenaza: {self.nivel_amenaza}, Recompensa: {self.recompensa})"

# Se crea un gestor de misiones que las asigna dependiendo el nivel de amenaza que tengan
class GestorMisiones:
    def __init__(self):
        self.cola = []  

    def agregar_mision(self, mision):
        heapq.heappush(self.cola, mision)
        print(f"Misión '{mision.nombre}' agregada con amenaza {mision.nivel_amenaza}")

    def proxima_mision(self):
        if self.cola:
            mision = heapq.heappop(self.cola)
            print(f"Próxima misión: {mision.nombre} (Amenaza {mision.nivel_amenaza})")
            return mision
        else:
            print("No hay misiones pendientes.")
            return None

    def mostrar_misiones(self):
        if not self.cola:
            print("No hay misiones en la cola.")
            return
        print("Misiones en la cola (de mayor a menor prioridad):")
        for m in sorted(self.cola, key=lambda x: x.nivel_amenaza):
            print(f"- {m.nombre} (Amenaza {m.nivel_amenaza}, Recompensa {m.recompensa})")

def asignar_mision(personaje, gestor_misiones):
    mision = gestor_misiones.proxima_mision()
    if mision:
        print(f"{personaje.nombre} acepta la misión '{mision.nombre}' con recompensa {mision.recompensa}.")
        personaje.poder_total += mision.recompensa // 10
