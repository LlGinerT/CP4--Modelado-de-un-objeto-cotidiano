import json
from Modulos.Ordenador import Portatil, Sobremesa


class FactoricaOrdenadores:
    """Clase que permite instanciar cualquier objeto heredado de la clase 'Ordenador', 
    adquiere la responsabilidad de la creación de los objetos heredados de 'Ordenador' a partir de un 
    archivo json con las especificaciones.

    Args:
    - stock(json): archivo json con los componentes del ordenador a instanciar
    """
    def __init__(self, stock: json) -> None:
        self._componentes = stock

    def instanciar_ordenador(self, formatoPc: str, id: str):
        """Instancia un objeto de tipo 'formatoPc' ('Portatil' | 'Sobremesa') a partir de 
        un ID y los atributos correspondientes del stock.
        
        Args:
        - formatoPc (str): Tipo de ordenador a instanciar ('Portatil' | 'Sobremesa').
        - id (str): ID del ordenador a instanciar.
        
        Returns:
        - Ordenador: 'Portatil' | 'Sobremesa'.
        """
        if formatoPc == "Portatil":
            """ Instancia un ordenador con formato Portátil y 
            los componentes dentro de un id especifico """
            componentes_pc = self._componentes["Portatil"][id]
            return Portatil(id=id, **componentes_pc)

        elif formatoPc == "Sobremesa":
            """ Instancia un ordenador con formato Sobremesa y
            un id especifico, primero extrae y crea un diccionario con los periféricos
            de dentro de los componentes, para luego desempaquetarlo"""
            componentes_pc = self._componentes["Sobremesa"][id]
            perifericos = componentes_pc.pop("perifericos")
            return Sobremesa(id=id, **componentes_pc, **perifericos)
