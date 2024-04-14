import json
from Modulos.App import App
from Modulos.Factoria import FactoriaOrdenadores


class GestorStock:

    def __init__(self, stock):
        self._portatiles = []
        self._sobremesas = []
        self._todos = []
        self._programas = [App("Windows", 60), App("Spotify", 4), App("Chrome", 2)]
        self._rutaStock = "Config/" + stock + ".json"
        self._estantes = {"Portatil": self._portatiles, "Sobremesa": self._sobremesas}

    def clasificarStock(self):

        with open(self._rutaStock, "r", encoding="UTF-8") as archivo:
            stock = json.load(archivo)

        fabrica = FactoriaOrdenadores(stock)
        for formato in stock:
            for producto in stock[formato]:
                productoAlmacenado = fabrica.instanciarProducto(formato, producto)
                self._estantes[formato].append(productoAlmacenado)

        for estantes in self._estantes.values():
            self._todos.append(estantes)

    def mostrar(self, formato):
        for producto in self._estantes[formato]:
            print(producto)

    def mostrarTodo(self):
        for estantes in self._todos:
            for producto in estantes:
                print(producto)

    def preparar_pc(self, formato, id):
        pc = list(filter(lambda x: x.id == id, self._estantes[formato]))
        for programa in self._programas:
            pc[0].install_app(programa)
            print(f"El estado actual del disco duro es: {pc[0].almacenamientoStatus}")
            print("------------------")

    def preparar_formato(self, formato):
        for pc in self._estantes[formato]:
            for programa in self._programas:
                pc.install_app(programa)
            print(f"El estado actual del disco duro es: {pc.almacenamientoStatus}")
            print("------------------")

    def preparar_todos(self):
        for estantes in self._todos:
            for pc in estantes:
                for programa in self._programas:
                    pc.install_app(programa)
                    print(
                        f"El estado actual del disco duro es: {pc.almacenamientoStatus}"
                    )
                    print("------------------")
