from Modulos.GestorStock import GestorStock


def main():
    """Instanciamos el GestoStock con el json donde tenemos
    los ordenadores con los que vamos a trabajar
    """
    main_menu = True
    menu_mostrar = False
    menu_preparar = False
    sobremeas_preparados = False
    portatiles_preparados = False
    almacen = GestorStock("Stock")
    print("Descargando lista de ordenadores disponibles")
    print("------------------")
    # "Descargamos" los Pcs de la base de datos falsa,
    # lo cual instancia todos los ordenadores disponibles
    # cumpliendo con el requisito de instanciar mínimo 3 portátiles.
    almacen.descargarStock()
    while main_menu:
        while menu_mostrar:
            try:
                print("Elija una opción:")
                print("1) Mostrar todos los ordenadores disponibles")
                print("2) Mostrar los ordenadores de un formato")
                print("3) Atrás")
                match int(input()):
                    case 1:
                        print("------------------")
                        almacen.mostrar_todo()
                        menu_mostrar = False

                    case 2:
                        print("------------------")
                        print("Elegir formato:")
                        print("1) Portátiles")
                        print("2) Sobremesas")
                        match int(input()):
                            case 1:
                                print("------------------")
                                almacen.mostrar_formato("Portatil")
                                menu_mostrar = False

                            case 2:
                                print("------------------")
                                almacen.mostrar_formato("Sobremesa")
                                menu_mostrar = False

                            case _:
                                print(
                                    "Opción no valida, Por favor introduzca un valor valido"
                                )

                    case 3:
                        menu_mostrar = False
                        break

                    case _:
                        print("Opción no valida, Por favor introduzca un valor valido")

            except ValueError:
                print("Valor no valido, Por favor introduzca un valor valido")
        while menu_preparar:

            try:
                print("Elija una opción:")
                print("1) Preparar todos los ordenadores disponibles")
                print("2) Preparar los ordenadores de un formato")
                print("3) Atrás")
                match int(input()):
                    case 1:
                        print("------------------")
                        if sobremeas_preparados and portatiles_preparados:
                            print("Todos los ordenadores ya están preparados")
                            menu_preparar = False
                        elif sobremeas_preparados and not portatiles_preparados:
                            print(
                                "Los sobremesas ya están preparados\nPreparando portátiles."
                            )
                            print("------------------")
                            almacen.preparar_formato("Portatil")
                            portatiles_preparados = True
                            menu_preparar = False
                        elif portatiles_preparados and not sobremeas_preparados:
                            print(
                                "Los portátiles ya están preparados\nPreparando sobremesas."
                            )
                            print("------------------")
                            almacen.preparar_formato("Sobremesa")
                            sobremeas_preparados = True
                            menu_preparar = False
                        elif not sobremeas_preparados and not portatiles_preparados:
                            almacen.preparar_todo()
                            menu_preparar = False
                            sobremeas_preparados = True
                            portatiles_preparados = True

                    case 2:
                        print("------------------")
                        print("Elegir formato:")
                        print("1) Portátiles")
                        print("2) Sobremesas")
                        match int(input()):
                            case 1:
                                print("------------------")
                                almacen.preparar_formato("Portatil")
                                menu_preparar = False
                                portatiles_preparados = True

                            case 2:
                                print("------------------")
                                almacen.preparar_formato("Sobremesa")
                                menu_preparar = False
                                sobremeas_preparados = True

                            case _:
                                print(
                                    "Opción no valida, Por favor introduzca un valor valido"
                                )

                    case 3:
                        menu_preparar = False
                        break

                    case _:
                        print("Opción no valida, Por favor introduzca un valor valido")

            except ValueError:
                print("Valor no valido, Por favor introduzca un valor valido")
        try:
            print("Elija una opción:")
            print("1) Mostrar ordenadores disponibles")
            print("2) Preparar ordenador")
            print("3) Salir")
            match int(input()):
                case 1:
                    print("------------------")
                    menu_mostrar = True

                case 2:
                    print("------------------")
                    menu_preparar = True

                case 3:
                    main_menu = False
                    break

                case _:
                    print("Opción no valida, Por favor introduzca un valor valido")

        except ValueError:
            print("Valor no valido, Por favor introduzca un valor valido")


if __name__ == "__main__":
    main()
