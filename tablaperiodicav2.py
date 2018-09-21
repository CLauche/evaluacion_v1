class Tabla_Periodica:
    def __init__(self):
        super().__init__()
        self._list = []
    def agregar_elemento(self, elemento):
        return self._list.append(elemento)
    def elementos_agregados(self):
        return self._list
    def elementoS(self, simbolo):
        for elemento in self._list:
            if (elemento.simbolo() == simbolo):
                return elemento
        else:
            return None
    def elementoN(self, numeroAtomico):
        for elemento in self._list:
            if (elemento.numeroAtomico() == numeroAtomico):
                return elemento
        else:
            return None

