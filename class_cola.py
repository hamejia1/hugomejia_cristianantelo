class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def esta_vacia(self):
        return self.frente is None

    def encolar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.frente = self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

    def desencolar(self):
        if self.esta_vacia():
            return None
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return dato

    def ver_primero(self):
        if self.esta_vacia():
            return None
        return self.frente.dato
    
    def __str_(self):
        elementos = []
        actual = self.frente
        while actual:
            elementos.appennd(str(actual.dato))
            actual = actual.siguiente
        return "Cola: " + " -> ".join(elementos)
