from datetime import datetime

# python clientes.py
# alta_cliente
# baja_cliente
# python clientes.py


# Función para dar de alta a un cliente
def alta_cliente(dni, nombre, apellido, telefono, direccion):

    # Lista para almacenar los clientes
    clientes = []

    cliente = {
        'DNI': dni,
        'Nombre': nombre,
        'Apellido': apellido,
        'Telefono': telefono,
        'Direccion': direccion,
        'Fecha_Alta': datetime.now(),
        'Estado': 'Activo',
        'ISBN_Libro': ''
    }
    clientes.append(cliente)

    # Registrar el alta en el archivo
    with open('Clientes.txt', 'a') as archivo:
        archivo.write(f"Alta de cliente -> DNI: {dni} | Nombre: {nombre} | Apellido: {apellido} | Tel: {telefono} | Direccion: {direccion} | Fecha_Alta: {cliente['Fecha_Alta']} | Estado: Activo,\n")

    return cliente

#print(alta_cliente(39874651, 'NombreUsuario2', 'ApellidoUsuario2', '1124028831', 'Sarmiento 1526'))
#print(clientes)


# Baja con manejo de archivos
def baja_cliente(dni):
    clientes_encontrados = []

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
            'Fecha_Alta': datetime.strptime(cliente[5].split(': ')[1], '%Y-%m-%d %H:%M:%S.%f'), # '%Y-%m-%d %H:%M:%S.%f' -> los elementos están separados por guiones y espacios para coincidir con el formato de la cadena de texto de la fecha y hora que se desea convertir.
            'Estado': cliente[6].split(': ')[1],
        }
        if cliente_dict['DNI'] == dni and cliente_dict['Estado'] == 'Activo' and cliente_dict['ISBN_Libro'] == '':
            cliente_dict['Fecha_Baja'] = datetime.now()
            cliente_dict['Estado'] = 'Inactivo'
            clientes_encontrados.append(cliente_dict)

    if clientes_encontrados:
        with open('Clientes.txt', 'w') as archivo:
            for linea in lineas:
                cliente = linea.strip().split(' | ')
                cliente_dni = int(cliente[0].split(': ')[1])
                if cliente_dni != dni:
                    archivo.write(linea)

            for cliente in clientes_encontrados:
                archivo.write(f"DNI: {cliente['DNI']} | Nombre: {cliente['Nombre']} | Apellido: {cliente['Apellido']} | Tel: {cliente['Telefono']} | Direccion: {cliente['Direccion']} | Fecha_Alta: {cliente['Fecha_Alta']} | Fecha_Baja: {cliente['Fecha_Baja']} | Estado: Inactivo\n")

        print("El cliente ha sido dado de baja exitosamente.")
        return clientes_encontrados[0]

    print("No se encontró el cliente o el cliente tiene préstamos activos.")
    return None  # indicar la falta de cliente válido

# Consultar estado con manejo de archivo
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
            'Estado': cliente[6].split(': ')[1],
        }
        if cliente_dict['DNI'] == dni:
            return cliente_dict['Estado']

    return 'Cliente no encontrado'

#print(consultar_estado_cliente(39874657))




"""MENU PARA EJECUTAR MODULO - SIMULACION APP FINAL"""

def mostrar_menu():
    print("Menú:")
    print("1. Alta cliente")
    print("2. Baja cliente")
    print("3. Consultar Estado cliente")

def ejecutar_opcion(opcion):
    if opcion == 1:
        alta_cliente(39874656, 'NombreUsuario9', 'ApellidoUsuario5', '11240288323', 'Sarmiento 15236')
        print("¡Cliente dado de alta!")
    if opcion == 2:
        baja_cliente(39874656)
    if opcion == 3:
        consultar_estado_cliente(39874656)


mostrar_menu()
opcion = int(input("Seleccione una opción: "))
ejecutar_opcion(opcion)











### ------------------------- ANTERIOR - SIN MANEJOR DE ARHIVOS ----------------------------- ###


# Función para modificar el teléfono o dirección de un cliente
def modificar_datos_cliente(dni, nombre, apellido, telefono, direccion):
    for cliente in clientes:
        if cliente['DNI'] == dni:
            if nombre:
                cliente['Nombre'] = nombre
            if apellido:
                cliente['Apellido'] = apellido
            if telefono:
                cliente['Telefono'] = telefono
            if direccion:
                cliente['Direccion'] = direccion

            with open('Clientes.txt', 'a') as archivo:
                archivo.write(f"Actualización de cliente -> DNI: {cliente['DNI']} | Nombre: {cliente['Nombre']} | Apellido: {cliente['Apellido']} | Tel: {cliente['Telefono']} | Direccion: {cliente['Direccion']} | Fecha_Alta: {datetime.now()} | Estado: Activo,\n")
                
            return 'Datos actualizados'
    return 'Cliente no encontrado'





# Función para consultar el estado de un cliente
""" def consultar_estado_cliente(dni):
    for cliente in clientes:
        if cliente['DNI'] == dni:
            return cliente['Estado']
    return 'Cliente no encontrado' """

# Función para dar de baja un cliente
"""def baja_cliente(dni):
    for cliente in clientes:
        if cliente['DNI'] == dni and cliente['ISBN_Libro'] == '':
            cliente['Fecha_baja'] = datetime.now()
            cliente['Estado'] = 'Inactivo'

            with open('Clientes.txt', 'a') as archivo:
                archivo.write(f"Baja de cliente -> DNI: {cliente['DNI']} | Nombre: {cliente['Nombre']} | Apellido: {cliente['Apellido']} | Tel: {cliente['Telefono']} | Direccion: {cliente['Direccion']} | Fecha_Alta: {cliente['Fecha_alta']} | Fecha_Baja: {cliente['Fecha_baja']} | Estado: Inactivo,\n")

            print("El cliente ha sido dado de baja exitosamente.")
            return cliente
    
    print("No se encontró el cliente o el cliente tiene préstamos activos.")
    return None"""  # indicar la falta de cliente válido








