from Modulos.Ordenador import Portatil, Sobremesa


class FactoriaOrdenadores:

    def __init__(self, stock) -> None:
        self._componentes = stock

    def instanciarProducto(self, formatoPc, id):

        if formatoPc == "Portatil":
            atributos_pc = self._componentes["Portatil"][id]
            return Portatil(id=id, **atributos_pc)

        elif formatoPc == "Sobremesa":
            atributos_pc = self._componentes["Sobremesa"][id]
            perifericos = atributos_pc.pop("perifericos")
            return Sobremesa(id=id, **atributos_pc, **perifericos)
