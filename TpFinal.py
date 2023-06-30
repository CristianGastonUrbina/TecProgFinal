from modulos.menu_opciones import mostrar_menu_principal, mostrar_menu_clientes, mostrar_menu_libros, mostrar_menu_prestamos, Salir, mostrar_mensaje_error, mensaje_dato_no_encontrado

# python TpFinal.py

estado = True
estado_menu = True

while estado:

    if estado_menu:
        mostrar_menu_principal()
        estado_menu = False
    
    try:
        opcion = int(input("Elige el numero de opción deseada: "))
        estado = False
    except ValueError:
           mostrar_mensaje_error()
    else:
        opciones = {
            1: mostrar_menu_clientes,
            2: mostrar_menu_libros,
            3: mostrar_menu_prestamos,
            4: Salir            
        }

        if opcion in opciones:
            opciones[opcion]()
            if opcion == 4:
                estado = False      # Salir del bucle si la opción es 4
                estado_menu = True
            else:
                estado = True
                estado_menu = False
        else:
            mensaje_dato_no_encontrado()
            estado = True
            estado_menu = True


        

# correr app -> python TpFinal.py
