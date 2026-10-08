
ROJO_PASTEL  = "\033[38;5;210m"
ROSA_CLARO = "\033[38;5;218m"
RESET = "\033[0m"

productos = []

while True: 
    print(f"{ROSA_CLARO}{'='*45}{RESET}")
    print(f"{ROSA_CLARO}||{RESET}  🌸 Sistema de gestion de productos 🌸  {ROSA_CLARO}||{RESET}")
    print(f"{ROSA_CLARO}={RESET}"*45)
    print(f"{ROSA_CLARO}1.{RESET} Agregar productos")
    print(f"{ROSA_CLARO}2.{RESET} Mostrar productos")
    print(f"{ROSA_CLARO}3.{RESET} Buscar productos")
    print(f"{ROSA_CLARO}4.{RESET} Eliminar productos")
    print(f"{ROSA_CLARO}5.{RESET} Salir")

    opcion = input(f"{ROSA_CLARO}Elegi una opcion del 1 al 5: {RESET}").strip()

    match opcion:
        case "1":
            print(f"{ROSA_CLARO}--- Agregar producto ---{RESET}")
        
            nombre = input(f"{ROSA_CLARO}Nombre del producto: {RESET}").strip().title()
            while nombre == "" or nombre.isdigit():
                print(f"{ROJO_PASTEL}Error: El nombre ingresado es invalido.{RESET}")
                nombre = input(f"{ROSA_CLARO}Nombre del producto: {RESET}").strip()

            categoria = input(f"{ROSA_CLARO}Categoria del producto: {RESET}").strip().title()
            
            while categoria == "" or categoria.isdigit():
                print(f"{ROJO_PASTEL}Error: La categoria ingresada es invalida.{RESET}")
                categoria = input(f"{ROSA_CLARO}Categoria del producto: {RESET}").strip()

            precio_str = input(f"{ROSA_CLARO}Precio (sin centavos): {RESET}").strip().title()
            while not precio_str.isdigit():
                print(f"{ROJO_PASTEL}Error: Ingresa solo números positivos, sin centavos.{RESET}")
                precio_str = input(f"{ROSA_CLARO}Precio (sin centavos): {RESET}").strip()
            precio_int = int(precio_str)

            datos = [nombre, categoria, precio_int]
            productos.append(datos)
            print(f"Producto {ROSA_CLARO}{nombre}{RESET} agregado con exito.")
        
        case "2":
            print(f"{ROSA_CLARO}--- Lista de Productos ---{RESET}")

            if len(productos) == 0:
                print(f"{ROJO_PASTEL}Error: Todavía no hay ningun producto cargado.{RESET}")
                print("Puedes ingresar productos eligiendo la opcion 1.")
            else:
                for i in range(len(productos)):
                    print(f"{ROSA_CLARO}🌸 ID: {i+1}{RESET}\n - Productos: {productos[i][0]},\n - Categoría: {productos[i][1]},\n - Precio: {productos[i][2]}")
        
        case "3":
            print(f"{ROSA_CLARO}--- Buscar producto ---{RESET}")

            if len(productos) == 0:
                print(f"{ROJO_PASTEL}Error: Todavia no hay productos cargados.{RESET}")
                print("Puedes ingresar productos eligiendo la opcion 1.")
            else:
                encontrado = 0

                while encontrado == 0:
                    busqueda = input(f"{ROSA_CLARO}Nombre del producto a buscar: {RESET}").strip().lower()

                    while busqueda == "":
                        print(f"{ROJO_PASTEL}Error: La busqueda no puede estar vacia.{RESET}")
                        busqueda = input(f"{ROSA_CLARO}Nombre del producto a buscar: {RESET}").strip().lower()

                    for i in range(len(productos)):
                        if busqueda in productos[i][0].lower():
                            print(f"{ROSA_CLARO}🌸 ID: {i+1}{RESET}\n - Producto: {productos[i][0]}\n - Categoría: {productos[i][1]}\n - Precio: ${productos[i][2]}")
                            encontrado += 1

                    if encontrado == 0:
                        print(f"{ROJO_PASTEL}Error: No hay ningun producto con ese nombre. Por favor, intenta de nuevo.{RESET}")
                    else:
                        print(f"{ROSA_CLARO}Productos encontrados: {encontrado}{RESET}")

        case "4":
            print(f"{ROSA_CLARO}--- Eliminar productos---{RESET}")
            if len(productos) == 0:
                print (f"{ROJO_PASTEL}Error: No se han encontrado productos cargados.{RESET}")
            else:
                for i in range(len(productos)):
                        print(f"{ROSA_CLARO}🌸 ID: {i+1}{RESET}\n - Producto: {productos[i][0]}\n - Categoría: {productos[i][1]}\n - Precio: ${productos[i][2]}")

                id_eliminar = input(f"{ROSA_CLARO}Numero de producto a eliminar (ID): {RESET}").strip()

                while not id_eliminar.isdigit():
                    print(f"{ROJO_PASTEL}Error: Por favor, ingresa un numero valido.{RESET}")
                    id_eliminar = input(f"{ROSA_CLARO}Numero de producto a eliminar: {RESET}").strip()

                posicion = int(id_eliminar) - 1

                if 0 <= posicion < len(productos):
                    eliminado = productos.pop(posicion)
                    print(f"{ROSA_CLARO}Se eliminó el producto: {eliminado[0]}{RESET}")
                else:
                    print(f"{ROJO_PASTEL}Error: El numero de producto ingresado no existe.{RESET}")

        case "5":
            print(f"{ROSA_CLARO}{'='*75}{RESET}")
            print(f"{ROSA_CLARO}||{RESET} 🌸 Gracias por utilizar nuestro sistema de gestion de productos. 🌸  {ROSA_CLARO}||{RESET}")
            print(f"{ROSA_CLARO}{'='*75}{RESET}")
            break
        case _:
            print(f"{ROJO_PASTEL}Opcion no valida. Por favor, elige un numero del 1 al 5.{RESET}")
