test = hola

from modulos.menu_funciones import mostrar_menu, opcion1, opcion2, opcion3, opcion4, mostrar_mensaje_error, mensaje_dato_no_encontrado

estado = True
estado_menu = True

while estado:

    if estado_menu:
        mostrar_menu()
        estado_menu = False
    
    try:
        opcion = int(input("Elige el numero de opción deseada: "))
        estado = False
    except ValueError:
           mostrar_mensaje_error()
    else:
        opciones = {
            1: opcion1,
            2: opcion2,
            3: opcion3,
            4: opcion4
        }

        if opcion in opciones:
            opciones[opcion]()
            if opcion == 4:
                estado = False      # Salir del bucle si la opción es 4
                estado_menu = True
            else:
                estado = True
                estado_menu = True
        else:
            mensaje_dato_no_encontrado()
            estado = True
            estado_menu = True


        

# correr app -> python TpFinal.py
