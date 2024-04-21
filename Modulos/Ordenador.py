from abc import ABC
from Modulos.App import App

""" 
Clase abstracta de ordenador
 """


class Ordenador(ABC):
    """
    Constructor con los atributos comunes de ordenado

    Args:
    - id(str): ID de identificación del ordenador ordenador
    - marca(str): Marca del ordenador
    - modelo(str): modelo del ordenador
    - procesador(int): Núcleos del procesador
    - ram(int): Gb de memoria ram
    - grafica(str): Modelo de tarjeta gráfica
    - almacenamiento(int): Memoria de disco duro en GB
    """

    def __init__(
        self,
        id: str,
        marca: str,
        modelo: str,
        procesador: int,
        ram: int,
        grafica: str,
        almacenamiento: int,
    ) -> None:
        self._id = str(id)
        self._formato = str
        self._marca = marca
        self._modelo = modelo
        self._procesador = procesador
        self._ram = ram
        self._grafica = grafica
        self._almacenamientoTotal = almacenamiento
        self._almacenamientoActual = self._almacenamientoTotal
        self._almacenamientoStatus = int
        self._apps_instaladas = ""

    def __str__(self) -> str:
        """
        Representación en cadena de texto de un Ordenador y sus atributos
        """
        return f"ID del producto: {self._id}\nMarca: {self._marca}\nModelo: {self._modelo}\nFormato: {self._formato}\nProcesador: {self._procesador} núcleos\nRam: {self._ram} GB\nAlmacenamiento: {self._almacenamientoTotal} GB\n"

    def install_app(self, app: App):
        """
        Metodo para instalar una App y actualizar el almacenamiento disponible

        Args:
        - app(Obj): Recibe un objeto de la clase App
        """
        print(
            f"Instalando: {app.nombre} en {self._modelo}.\nEspacio requerido:{app.tamaño}\nEspacio Actual:{self.almacenamientoActual}\nInstalación completada."
        )
        self._almacenamientoActual -= app.tamaño
        self._apps_instaladas += f"{app.nombre}, "

    @property
    def almacenamientoActual(self):
        """
        Getters del atributo almacenamientoActual del ordenador
        """
        return self._almacenamientoActual

    @property
    def almacenamientoStatus(self):
        """
        Este atributo muestra el porcentaje de espacio disponible del almacenamiento
        """
        self._almacenamientoStatus = int(
            self._almacenamientoActual * 100 / self._almacenamientoTotal
        )
        return f"{self._almacenamientoStatus}%"

    @property
    def marca(self):
        """
        Getters del atributo marca del ordenador
        """
        return self._marca

    @property
    def formato(self):
        """
        Getters del atributo formato del ordenador
        """
        return self._formato

    @property
    def id(self):
        """
        Getters del atributo id del ordenador
        """
        return self._id


class Portatil(Ordenador):
    """
    Clase Portatil que hereda de Ordenador
    añadiendo sus atributos particulares

    Args:
    - bateria(int): capacidad de la batería en Watts hora (Whr)
    - pantalla(int): Tamaño de la pantalla del portátil en pulgadas
    """

    def __init__(
        self,
        id: str,
        marca: str,
        modelo: str,
        procesador: int,
        ram: int,
        grafica: str,
        almacenamiento: int,
        bateria: int,
        pantalla: int,
    ) -> None:
        super().__init__(id, marca, modelo, procesador, ram, grafica, almacenamiento)
        self._formato = "Portatil"
        self.__bateria = bateria
        self.__pantalla = pantalla

    def __str__(self) -> str:
        """
        Representación en cadena de texto de un Portatil, sus atributos
        y si tiene o no apps instaladas
        """
        if len(self._apps_instaladas) == 0:
            return (
                super().__str__()
                + f'Batería: {self.__bateria} Whr\nPantalla: {self.__pantalla}"\n------------------'
            )
        else:
            return (
                super().__str__()
                + f'Batería: {self.__bateria} Whr\nPantalla: {self.__pantalla}"\nApps instaladas: {self._apps_instaladas.strip(", ")}.\n------------------'
            )


class Sobremesa(Ordenador):
    """
    Clase Sobremesa que hereda de Ordenador
    añadiendo sus atributos particulares

    Args:
    - perifericos(dicc): diccionario con un numero variable de argumentos clave-valor
    """

    def __init__(
        self,
        id: str,
        marca: str,
        modelo: str,
        procesador: int,
        ram: int,
        grafica: str,
        almacenamiento: int,
        **perifericos: dict,
    ) -> None:
        super().__init__(id, marca, modelo, procesador, ram, grafica, almacenamiento)
        self._formato = "Sobremesa"
        self.__perifericos = perifericos

    def __str__(self) -> str:
        """
        Representación en cadena de texto de un Sobremesa, sus atributos,
        sus periféricos y si tiene o no apps instaladas
        """
        añadir_perifericos = super().__str__()
        for periferico in self.__perifericos:
            añadir_perifericos += (
                periferico + ": " + str(self.__perifericos[periferico]) + "\n"
            )
        if len(self._apps_instaladas) == 0:
            return añadir_perifericos + "------------------"
        else:
            return (
                añadir_perifericos
                + f"Apps instaladas: {self._apps_instaladas.strip(", ")}.\n------------------"
            )
