

# alta_cliente
# baja_cliente
# consultar estado
# modificar datos


### ------------------------------------------------------------------------------- Funcionalidades ----------------------------------------------------------------------------------- ###
from datetime import datetime
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

    return cliente


def baja_cliente(dni):
    clientes_encontrados = []

    with open('Clientes.txt', 'r') as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        cliente = linea.strip().split(', ')
        cliente_dict = {
            'DNI': int(cliente[0].split(' -> ')[1]),
            'Nombre': cliente[1],
            'Apellido': cliente[2],
            'Telefono': cliente[3],
            'Direccion': cliente[4],
            'Fecha_Alta': cliente[5],
            'ISBN_Libro': cliente[6],
            'Estado': cliente[7].split(' ')[1]
        }

        if cliente_dict['DNI'] == dni and cliente_dict['Estado'] == 'Activo' and cliente_dict['ISBN_Libro'] == '':
            cliente_dict['Fecha_Baja'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            cliente_dict['Estado'] = 'Inactivo'
            clientes_encontrados.append(cliente_dict)

    if clientes_encontrados:
        with open('Clientes.txt', 'w') as archivo:
            for linea in lineas:
                cliente = linea.strip().split(', ')
                cliente_dni = int(cliente[0].split(' -> ')[1])
                if cliente_dni != dni:
                    archivo.write(linea)

            for cliente in clientes_encontrados:
                archivo.write(f"Baja de cliente -> {cliente['DNI']}, {cliente['Nombre']}, {cliente['Apellido']}, {cliente['Telefono']}, {cliente['Direccion']}, {cliente['Fecha_Alta']}, {cliente['Fecha_Baja']}, Inactivo \n")

        print("El cliente ha sido dado de baja exitosamente.")
        return clientes_encontrados[0]

    print("No se encontró el cliente o el cliente tiene préstamos activos.")
    return None


def consultar_estado_cliente(dni):
    with open('Clientes.txt', 'r') as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        cliente = linea.strip().split(' | ')
        cliente_dict = {
            'DNI': int(cliente[0].split(': ')[1]),
            'Nombre': cliente[1].split(': ')[1],
            'Apellido': cliente[2].split(': ')[1],
            'Telefono': cliente[3].split(': ')[1],
            'Direccion': cliente[4].split(': ')[1],
            'Fecha_Alta': datetime.strptime(cliente[5].split(': ')[1], '%Y-%m-%d %H:%M:%S.%f'),
            'estado_menu_principal': cliente[6].split(': ')[1],
        }
        if cliente_dict['DNI'] == dni:
            return cliente_dict['estado']

    return 'Cliente no encontrado'


def modificar_datos_cliente(dni, nombre, apellido, telefono, direccion):
    with open('clientes.txt', 'r') as archivo:
        lineas = archivo.readlines()

    encontrado = False
    for i, linea in enumerate(lineas):
        datos = linea.strip().split('|')
        cliente = {
            'DNI': datos[0].strip(),
            'Nombre': datos[1].strip(),
            'Apellido': datos[2].strip(),
            'Telefono': datos[3].strip(),
            'Direccion': datos[4].strip()
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

            lineas[i] = f"{cliente['DNI']} | {cliente['Nombre']} | {cliente['Apellido']} | {cliente['Telefono']} | {cliente['Direccion']}"

            encontrado = True
            break

    if encontrado:
        with open('clientes.txt', 'w') as archivo:
            archivo.writelines(lineas)
        
        registro_actualizacion = f"Actualización de cliente -> DNI: {cliente['DNI']} | Nombre: {cliente['Nombre']} | Apellido: {cliente['Apellido']} | Tel: {cliente['Telefono']} | Dirección: {cliente['Direccion']} | Fecha_Alta: {datetime.now()} | estado_menu_principal: Activo\n"
        with open('Clientes.txt', 'a') as archivo:
            archivo.write(registro_actualizacion)

        return 'Datos actualizados'
    else:
        return 'Cliente no encontrado'


###  ------------------------------------------------------ Funciones para menu modulo clientes ------------------------------------------------------ ###


def pedir_datos_cliente():
    dni = input("Ingrese el DNI: ")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    telefono = input("Ingrese el teléfono: ")
    direccion = input("Ingrese la dirección: ")

    # Llamar a la función "alt_cliente" con los datos ingresados
    alta_cliente(dni, nombre, apellido, telefono, direccion)


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
            estado_menu_principal_menu = False
        
        try:
            opcion = int(input("Elige el numero de opción deseada: "))
            estado_menu_principal = False
        except ValueError:
            mostrar_mensaje_error()
        else:
            opciones = {
                1: submenu_clientes,
                2: 1,
                3: 2,
                4: Salir            
            }

            if opcion in opciones:
                opciones[opcion]()                
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