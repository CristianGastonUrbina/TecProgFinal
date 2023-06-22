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
        archivo.write(f"Alta de cliente: DNI: {dni} - Nombre: {nombre} - Apellido: {apellido} - Tel: {telefono} - Direccion{direccion} - Fecha_Alta{cliente['Fecha_Alta']} - Estado: Activo - ,\n")

    return cliente

#alta_cliente(39931865, 'Damian', 'Fortumesky', '1124028836', 'Sarmiento 1426')
#print(clientes)

# Función para dar de baja un cliente
def baja_cliente(dni):
    for cliente in clientes:
        if cliente['DNI'] == dni and cliente['ISBN_Libro'] == '':
            cliente['Fecha_baja'] = datetime.now()
            cliente['Estado'] = 'Inactivo'

            with open('Clientes.txt', 'a') as archivo:
                archivo.write(f"Baja de cliente: {cliente['DNI']} - {cliente['Nombre']} - {cliente['Apellido']} - {cliente['Telefono']} - {cliente['Direccion']} - {cliente['Fecha_alta']} - {cliente['Fecha_baja']} - Inactivo\n")

            print("El cliente ha sido dado de baja exitosamente.")
            return cliente
    
    print("No se encontró el cliente o el cliente tiene préstamos activos.")
    return None  # indicar la falta de cliente válido





