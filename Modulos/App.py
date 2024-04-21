class App:
    """
    Clase App que representa un programa con su nombre y tamaño

    Args:
    - nombre(str): Nombre de la aplicación
    - tamaño(int): Tamaño de la aplicación
    """

    def __init__(self, nombre: str, tamaño: int):
        self._nombre = nombre
        self._tamaño = tamaño

    @property
    def nombre(self):
        """
        Getter del atributo nombre

        Returns:
        - nombre(str)
        """
        return self._nombre

    @property
    def tamaño(self):
        """
        Getter del atributo tamaño

        Returns:
        - tamaño(int)
        """
        return self._tamaño
