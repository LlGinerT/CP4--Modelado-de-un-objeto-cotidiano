from Modulos.GestorStock import GestorStock


def main():
    almacen = GestorStock("Stock")
    almacen.clasificarStock()
    almacen.mostrarTodo()
    almacen.preparar_pc("Portatil", "02")
    almacen.preparar_formato("Sobremesa")
    almacen.preparar_todos()


if __name__ == "__main__":
    main()
