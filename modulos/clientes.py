from datetime import datetime

# alta_cliente
# baja_cliente
# consultar estado
# modificar datos


### ------------------------------------------------------------------------------- Funcionalidades ----------------------------------------------------------------------------------- ###
def alta_cliente(dni, nombre, apellido, telefono, direccion):

    cliente = {
        'DNI': dni,
        'Nombre': nombre,
        'Apellido': apellido,
        'Telefono': telefono,
        'Direccion': direccion,
        'Fecha_Alta': datetime.now(),
        'ISBN_Libro': '',
        'Estado': 'Activo'
    }
    # Registrar el alta en el archivo
    with open('Clientes.txt', 'a') as archivo:
        archivo.write(f"Alta de cliente -> {cliente['DNI']}, {cliente['Nombre']}, {cliente['Apellido']}, {cliente['Telefono']}, {cliente['Direccion']}, {cliente['Fecha_Alta']}, {cliente['ISBN_Libro']}, Activo \n")

    print("\nEl cliente ha sido dado de alta exitosamente")
    return cliente


def baja_cliente(dni):
    clientes_encontrados = []

    with open('clientes.txt', 'r') as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        cliente = linea.strip().split(' -> ')[1].split(', ')

        if len(cliente) >= 8:
            estado = cliente[7]
        else:
            estado = ''

        cliente_dict = {
            'DNI': int(cliente[0]),
            'Nombre': cliente[1],
            'Apellido': cliente[2],
            'Telefono': cliente[3],
            'Direccion': cliente[4],
            'Fecha_Alta': cliente[5],
            'ISBN_Libro': cliente[6],
            'Estado': estado
        }

        if (
            cliente_dict['DNI'] == dni and
            cliente_dict['Estado'] == 'Activo' and
            cliente_dict['ISBN_Libro'] == ''
        ):
            cliente_dict['Fecha_Baja'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            cliente_dict['Estado'] = 'Inactivo'
            clientes_encontrados.append(cliente_dict)

    if clientes_encontrados:
        with open('clientes.txt', 'w') as archivo:
            for linea in lineas:
                cliente = linea.strip().split(' -> ')[1].split(', ')
                cliente_dni = int(cliente[0])
                if cliente_dni != dni:
                    archivo.write(linea)

            for cliente in clientes_encontrados:
                archivo.write(
                    f"Baja de cliente -> {cliente['DNI']}, {cliente['Nombre']}, {cliente['Apellido']}, {cliente['Telefono']}, {cliente['Direccion']}, {cliente['Fecha_Alta']}, {cliente['Fecha_Baja']}, Inactivo\n"
                )

        print("El cliente ha sido dado de baja exitosamente.")
        return clientes_encontrados[0]

    print("No se encontró el cliente o el cliente tiene préstamos activos.")
    return None

baja_cliente(39931865)

def consultar_estado_cliente(dni):
    with open('Clientes.txt', 'r') as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        cliente = linea.strip().split(', ')
        cliente_dict = {
            'DNI': int(cliente[0]),
            'Nombre': cliente[1],
            'Apellido': cliente[2],
            'Telefono': cliente[3],
            'Direccion': cliente[4],
            'Fecha_Alta': datetime.strptime(cliente[5], '%Y-%m-%d %H:%M:%S.%f'),
            'Estado': cliente[7],
        }
        if cliente_dict['DNI'] == dni:
            return cliente_dict['estado_menu_principal']

    return 'Cliente no encontrado'


def modificar_datos_cliente(dni, nombre, apellido, telefono, direccion):
    with open('Clientes.txt', 'r') as archivo:
        lineas = archivo.readlines()

    encontrado = False
    for i, linea in enumerate(lineas):
        datos = linea.strip().split(', ')
        cliente = {
            'DNI': datos[0],
            'Nombre': datos[1],
            'Apellido': datos[2],
            'Telefono': datos[3],
            'Direccion': datos[4]
        }

        if cliente['DNI'] == dni:
            if nombre:
                cliente['Nombre'] = nombre
            if apellido:
                cliente['Apellido'] = apellido
            if telefono:
                cliente['Telefono'] = telefono
            if direccion:
                cliente['Direccion'] = direccion

            lineas[i] = f"{cliente['DNI']}, {cliente['Nombre']}, {cliente['Apellido']}, {cliente['Telefono']}, {cliente['Direccion']}, {datos[5]}, {datos[6]}, {datos[7]}"

            encontrado = True
            break

    if encontrado:
        with open('Clientes.txt', 'w') as archivo:
            archivo.writelines(lineas)
        
        registro_actualizacion = f"Actualización de cliente -> {cliente['DNI']}, {cliente['Nombre']}, {cliente['Apellido']}, {cliente['Telefono']}, {cliente['Direccion']}, {datetime.now()}, {datos[6]}, {datos[7]}"
        with open('Clientes.txt', 'a') as archivo:
            archivo.write(registro_actualizacion)

        return 'Datos actualizados'
    else:
        return 'Cliente no encontrado'


###  ------------------------------------------------------ Funciones para menu modulo clientes ------------------------------------------------------ ###


def pedir_datos_cliente():
    flag_dni = True
    while flag_dni:
        try:
            dni = int(input("Ingrese el DNI: "))
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")

            flag_telefono = True
            while flag_telefono:
                try:
                    telefono = int(input("Ingrese el teléfono: "))
                    flag_telefono = False
                except ValueError:
                    print("El teléfono debe ser numérico")
            
            direccion = input("Ingrese la dirección: ")

            flag_dni = False
        except ValueError:
                print("El DNI debe ser numerico")

    return  alta_cliente(dni, nombre, apellido, telefono, direccion)
   


def baja_datos_cliente():
    dni = input("Ingrese el DNI: ")
    
    # Llamar a la función "baja_cliente" con los datos ingresados
    baja_cliente(dni)


def consultar_estado_cliente():
    dni = input("Ingrese el DNI: ")
    
    # Llamar a la función con los datos ingresados
    consultar_estado_cliente(dni)

def modificar_datos_cliente():
    dni = input("Ingrese el DNI: ")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    telefono = input("Ingrese el teléfono: ")
    direccion = input("Ingrese la dirección: ")
    
    # Llamar a la función con los datos ingresados
    modificar_datos_cliente(dni, nombre, apellido, telefono, direccion)

###  ---------------------------------------------------------- ALERTAS ---------------------------------------------------------- ###

def mostrar_menu_principal():
    print("                            ")
    print("╔══════════════════════════╗")
    print("║      Bienvenido a        ║")
    print("║    Biblioteca IFTS24     ║")
    print("╠═════════════════════════ ╣")
    print("║ 1. Gestion Clientes      ║")
    print("║ 2. Gestion Libros        ║")
    print("║ 3. Gestion Prestamos     ║")
    print("║ 4. Salir                 ║")
    print("╚══════════════════════════╝")
    print("                            ")

def submenu_clientes():
    print("                                       ")
    print("╔═════════════════════════════════════╗")
    print("║           Gestion Clientes          ║")
    print("║                                     ║")
    print("╠═════════════════════════════════════╣")
    print("║ 1. Alta Cliente                     ║")
    print("║ 2. Baja Cliente                     ║")
    print("║ 3. Consultar estado del cliente     ║")
    print("║ 4. Actualizar Datos                 ║")
    print("║ 7. Salir                            ║")
    print("╚═════════════════════════════════════╝")
    print("                                       ")

def mostrar_mensaje_error():
    print("                                        ")
    print("╔══════════════════════════════════════╗")
    print("║      Error al ingresar dato !        ║")
    print("╠══════════════════════════════════════╣")
    print("║ Debe ingresar un Nº de opción válido ║")
    print("╚══════════════════════════════════════╝")
    print("                                        ")

def mensaje_dato_no_encontrado():
    print("                                        ")
    print("╔══════════════════════════════════════╗")
    print("║         Error de busqueda !          ║")
    print("╠══════════════════════════════════════╣")
    print("║         Esa opcion no existe         ║")
    print("╚══════════════════════════════════════╝")
    print("                                        ")

def Salir():
    print("                       ")
    print("      Hasta luego!     ")
    print("                       ")


### ---------------------------------------------------------------------------------- APP ENTRADA ---------------------------------------------------------------------------------- ###

def programa():
    estado_menu_principal = True

    while estado_menu_principal:

        if estado_menu_principal:
            mostrar_menu_principal()        
        try:
            opcion = int(input("Elige el numero de opción deseada: "))
            estado_menu_principal = False
        except ValueError:
            mostrar_mensaje_error()
        else:           
            opciones = {
                1: submenu_clientes,
                2: "submenu_libros",
                3: "submenu_prestamos",
                4: Salir            
            }

            if opcion in opciones:
                opciones[opcion]()  
                if opcion == 4:
                    estado_menu_principal = False
            else:
                mensaje_dato_no_encontrado()
                estado_menu_principal = True
        
        # Aca comienza la gestion del submnu
        estado_submenu = True

        while estado_submenu:
            try:
                opcion_submenu_clientes = int(input("Elige el numero de opción deseada: "))
                estado_submenu = False
            except ValueError:
                mostrar_mensaje_error()
            else:
                ops_clientes = {
                    1: pedir_datos_cliente,
                    2: baja_datos_cliente,
                    3: consultar_estado_cliente,
                    4: modificar_datos_cliente,
                    5: Salir
                }

                if opcion in ops_clientes:
                    ops_clientes[opcion]()                
                else:
                    mensaje_dato_no_encontrado()
                    estado_submenu = True

programa()
