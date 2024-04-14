from abc import ABC


class Ordenador(ABC):

    def __init__(
        self, id, marca, modelo, procesador, ram, grafica, almacenamiento
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

    def __str__(self) -> str:
        return f"ID del producto: {self._id}\nMarca: {self._marca}\nModelo: {self._modelo}\nFormato: {self._formato}\nProcesador: {self._procesador} núcleos\nRam: {self._ram} GB\nAlmacenamiento: {self._almacenamientoTotal} GB\n"

    def install_app(self, app):
        print(
            f"Instalando: {app.nombre} en {self._modelo}.\nEspacio requerido:{app.tamaño}\nEspacio Actual:{self.almacenamientoActual}\nInstalación completada."
        )
        self._almacenamientoActual -= app.tamaño

    @property
    def almacenamientoActual(self):
        return self._almacenamientoActual

    @property
    def almacenamientoStatus(self):
        self._almacenamientoStatus = int(
            self._almacenamientoActual * 100 / self._almacenamientoTotal
        )
        return f"{self._almacenamientoStatus}%"

    @property
    def marca(self):
        return self._marca

    @property
    def formato(self):
        return self._formato

    @property
    def id(self):
        return self._id


class Portatil(Ordenador):

    def __init__(
        self,
        id,
        marca,
        modelo,
        procesador,
        ram,
        grafica,
        almacenamiento,
        bateria,
        pantalla,
    ) -> None:
        super().__init__(id, marca, modelo, procesador, ram, grafica, almacenamiento)
        self._formato = "Portátil"
        self.__bateria = bateria
        self.__pantalla = pantalla

    def __str__(self) -> str:
        return (
            super().__str__()
            + f'Batería: {self.__bateria}\nPantalla: {self.__pantalla}"\n------------------'
        )


class Sobremesa(Ordenador):

    def __init__(
        self,
        id,
        marca,
        modelo,
        procesador,
        ram,
        grafica,
        almacenamiento,
        **perifericos,
    ) -> None:
        super().__init__(id, marca, modelo, procesador, ram, grafica, almacenamiento)
        self._formato = "Sobremesa"
        self.__perifericos = perifericos

    def __str__(self) -> str:
        añadir_perifericos = super().__str__()
        for periferico in self.__perifericos:
            añadir_perifericos += (
                periferico + ": " + str(self.__perifericos[periferico]) + "\n"
            )
        return añadir_perifericos + "------------------"
