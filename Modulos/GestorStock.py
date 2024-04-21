import json
from Modulos.App import App
from Modulos.Factoria import FactoricaOrdenadores
from Modulos.Ordenador import Ordenador


class GestorStock:
    """
    Clase que "imita" la conexión con una base de datos de PCs disponibles
    y su gestión.

    Args:
    - stock(str): Nombre del archivo json que se usa para "imitar" una base de datos (Se debe quitar el .json del nombre).
    """

    def __init__(self, stock: str):
        self._stockPcs: list[Ordenador] = []
        self._programas: list[App] = [
            App("Windows", 60),
            App("Spotify", 4),
            App("Chrome", 2),
        ]
        self._rutaStock: str = "Config/" + stock + ".json"

    def descargarStock(self):
        """
        Este método, "descarga" los PCs disponibles de nuestra "base de datos imaginaria", en este caso un json,
        e instanciando un OBJETO de la CLASE FactoriaOrdenadores,
        se instancian y se almacenan los OBJETOS de las clases heredadas de Ordenador para su posterior uso
        """
        with open(self._rutaStock, "r", encoding="UTF-8") as archivo:
            stock = json.load(archivo)

        fabrica = FactoricaOrdenadores(stock)
        for formato in stock:
            for producto in stock[formato]:
                self._stockPcs.append(fabrica.instanciar_ordenador(formato, producto))

    def mostrar_formato(self, formato: str):
        """
        Método que muestra por pantalla los OBJETOS almacenados en 'self._stockPcs' filtrados por su atributo formato.

        Args:
        - formato(str): Tipo de ordenador a mostrar('Portatil'|'Sobremesa')
        """
        for pc in self._stockPcs:
            if pc.formato == formato:
                print(pc)

    def mostrar_todo(self):
        """
        Método que muestra todos los OBJETOS almacenados en 'self._stockPcs'
        """
        for pc in self._stockPcs:
            print(pc)

    def preparar_formato(self, formato: str):
        """
        Método que instala las aplicaciones de self._programas ,
        usando el método 'install_app' de la clase 'Ordenador', filtrados por 'formato'.

        Args:
        - formato(str): Tipo de ordenador a mostrar('Portatil'|'Sobremesa')
        """
        for pc in self._stockPcs:
            if pc.formato == formato:
                for programa in self._programas:
                    pc.install_app(programa)
                    print(
                        f"El estado actual del disco duro es: {pc.almacenamientoStatus}"
                    )
                    print("------------------")

    def preparar_todo(self):
        """
        Método que instala las aplicaciones de 'self._programas'
        usando el método 'install_app' de la clase 'Ordenador'.
        """
        for pc in self._stockPcs:
            for programa in self._programas:
                pc.install_app(programa)
                print(f"El estado actual del disco duro es: {pc.almacenamientoStatus}")
                print("------------------")
