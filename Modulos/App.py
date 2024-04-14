class App:

    def __init__(self, nombre, tamaño):
        self._nombre = nombre
        self._tamaño = tamaño

    @property
    def nombre(self):
        return self._nombre

    @property
    def tamaño(self):
        return self._tamaño
