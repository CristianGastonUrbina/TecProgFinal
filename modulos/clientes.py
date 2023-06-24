from datetime import datetime

# Lista para almacenar los clientes
clientes = []

# Función para dar de alta a un cliente
def alta_cliente(dni, nombre, apellido, telefono, direccion):
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

#alta_cliente(39874650, 'NombreUsuario', 'ApellidoUsuario', '1124028836', 'Sarmiento 1426')
#print(clientes)

# Función para dar de baja un cliente
def baja_cliente(dni):
    for cliente in clientes:
        if cliente['DNI'] == dni and cliente['ISBN_Libro'] == '':
            cliente['Fecha_baja'] = datetime.now()
            cliente['Estado'] = 'Inactivo'

            with open('Clientes.txt', 'a') as archivo:
                archivo.write(f"Baja de cliente -> DNI: {cliente['DNI']} | Nombre: {cliente['Nombre']} | Apellido: {cliente['Apellido']} | Tel: {cliente['Telefono']} | Direccion: {cliente['Direccion']} | Fecha_Alta: {cliente['Fecha_alta']} | Fecha_Baja: {cliente['Fecha_baja']} | Estado: Inactivo,\n")

            print("El cliente ha sido dado de baja exitosamente.")
            return cliente
    
    print("No se encontró el cliente o el cliente tiene préstamos activos.")
    return None  # indicar la falta de cliente válido

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
def consultar_estado_cliente(dni):
    for cliente in clientes:
        if cliente['DNI'] == dni:
            return cliente['Estado']
    return 'Cliente no encontrado'



"se agrega funciones: modificar_datos_cliente consultar_estado_cliente al modulo clientes"






