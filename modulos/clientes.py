from datetime import datetime
import os


# ---------------------------------------------------------- FUNCIONES QUE MANEJAN EL MODELO DE DATOS ---------------------------------------------------------- #


def alta_cliente(dni, nombre, apellido, telefono, direccion):

    cliente = {
        'DNI': dni,
        'Nombre': nombre,
        'Apellido': apellido,
        'Telefono': telefono,
        'Direccion': direccion,
        'Fecha_Alta': datetime.now(),
        'Fecha_Baja': 'NULL',
        'ISBN_Libro': 'NULL',
        'Estado': 'Activo'
    }
    # Registrar el alta en el archivo
    with open('Clientes.txt', 'a') as archivo:
        archivo.write(f"Alta de cliente -> {cliente['DNI']}, {cliente['Nombre']}, {cliente['Apellido']}, {cliente['Telefono']}, {cliente['Direccion']}, {cliente['Fecha_Alta']}, {cliente['Fecha_Baja']}, {cliente['ISBN_Libro']}, {cliente['Estado']} \n")

    print("\nEl cliente ha sido dado de alta exitosamente")
    return cliente

#alta_cliente(39234543, 'Damian', 'Fortunesky', 1123456789, 'sarasa 123')


def baja_cliente(dni):
    clientes_encontrados = []

    ruta = 'E:\\Escritorio\\tec-programacion\\TecProgFinal\\modulos\\Clientes.txt'
    with open(ruta, 'r') as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        cliente = linea.strip().split(' -> ')[1].split(', ')

        cliente_dict = {
            'DNI': cliente[0],
            'Nombre': cliente[1],
            'Apellido': cliente[2],
            'Telefono': cliente[3],
            'Direccion': cliente[4],
            'Fecha_Alta': cliente[5],
            'Fecha_Baja': cliente[6],
            'ISBN_Libro': cliente[7],
            'Estado': cliente[8]
        }

        if (
            cliente_dict['DNI'] == str(dni) and
            cliente_dict['Estado'] == 'Activo' and
            cliente_dict['ISBN_Libro'] == 'NULL'
        ):
            cliente_dict['Fecha_Baja'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            cliente_dict['Estado'] = 'Inactivo'
            clientes_encontrados.append(cliente_dict)

    if clientes_encontrados:
        with open(ruta, 'w') as archivo:
            for linea in lineas:
                cliente = linea.strip().split(' -> ')[1].split(', ')
                cliente_dni = cliente[0]

                if cliente_dni != str(dni):
                    archivo.write(linea)

            for cliente in clientes_encontrados:
                archivo.write(
                    f"Baja de cliente -> {cliente['DNI']}, {cliente['Nombre']}, {cliente['Apellido']}, {cliente['Telefono']}, {cliente['Direccion']}, {cliente['Fecha_Alta']}, {cliente['Fecha_Baja']}, NULL, {cliente['Estado']}\n"
                )

        print("El cliente ha sido dado de baja exitosamente.")
        return clientes_encontrados[0]

    print("No se encontró el cliente o el cliente tiene préstamos activos.")
    return None

#baja_cliente(39234543)


def consultar_estado_cliente(dni):
    ruta = 'E:\\Escritorio\\tec-programacion\\TecProgFinal\\modulos\\Clientes.txt'

    with open(ruta, 'r') as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        cliente = linea.strip().split(', ')
        
       
        cliente_dict = {
            'DNI': cliente[0][cliente[0].rfind('>') + 1:].strip(),
            'Nombre': cliente[1],
            'Apellido': cliente[2],
            'Telefono': cliente[3],
            'Direccion': cliente[4],
            'Fecha_Alta': datetime.strptime(cliente[5], '%Y-%m-%d %H:%M:%S.%f'),
            'Estado': cliente[8]
        }

        if cliente_dict['DNI'] == str(dni):
            ultimo_registro = cliente_dict['Estado']  
            return f"Su estado como cliente es: {ultimo_registro}"       
        
    return print('Cliente no encontrado')

#print(consultar_estado_cliente(39234543))


def modificar_datos_cliente(dni, nombre, apellido, telefono, direccion):

    ruta = 'E:\\Escritorio\\tec-programacion\\TecProgFinal\\modulos\\Clientes.txt'

    with open(ruta, 'r') as archivo:
        lineas = archivo.readlines()

    encontrado = False
    for i, linea in enumerate(lineas):
        datos = linea.strip().split(', ')
        cliente = {
            'DNI': datos[0][datos[0].rfind('>') + 1:].strip(),
            'Nombre': datos[1],
            'Apellido': datos[2],
            'Telefono': datos[3],
            'Direccion': datos[4],
            'Fecha_Alta': datos[5],
            'Fecha_Baja': datos[6],
            'ISBN_Libro': datos[7],
            'Estado': datos[8]
        }

        if cliente['DNI'] == str(dni):
            if nombre:
                cliente['Nombre'] = nombre
            if apellido:
                cliente['Apellido'] = apellido
            if telefono:
                cliente['Telefono'] = str(telefono)
            if direccion:
                cliente['Direccion'] = direccion

            cliente['Fecha_Alta'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

            lineas[i] = f"{cliente['DNI']}, {cliente['Nombre']}, {cliente['Apellido']}, {cliente['Telefono']}, {cliente['Direccion']}, {cliente['Fecha_Alta']}, {cliente['Fecha_Baja']}, {cliente['ISBN_Libro']}, {cliente['Estado']}\n"

            encontrado = True
            break

    if encontrado:

        registro_actualizacion = f"Actualizacion de cliente -> {cliente['DNI']}, {cliente['Nombre']}, {cliente['Apellido']}, {cliente['Telefono']}, {cliente['Direccion']}, {cliente['Fecha_Alta']}, {cliente['Fecha_Baja']}, {cliente['ISBN_Libro']}, {cliente['Estado']}\n"
        with open(ruta, 'a') as archivo:
            archivo.write(registro_actualizacion)

        return 'Datos actualizados'
    else:
        return 'Cliente no encontrado'

#print(modificar_datos_cliente(39234543, "Damian", "Fortunesky", 1123456789, "nuevaDireccion2"))



# -------------------------------------------- FUNCIONES QUE MANEJAN LAS SOLICITUDES DE LOS USUARIOS, LOS CONTROLADORES -------------------------------------------- #


def pedir_datos_alta_cliente():
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
    
    # Llamar a la función con los datos ingresados
    alta_cliente(dni, nombre, apellido, telefono, direccion)
   

def pedir_datos_baja_cliente():
    flag_dni = True
    while flag_dni:
        try:
            dni = int(input("Ingrese el DNI: "))
            flag_dni = False
        except ValueError:
            print("El DNI debe ser numérico")
    
    # Llamar a la función "baja_cliente" con los datos ingresados
    baja_cliente(dni)



def pedir_datos_consulta_estado_cliente():
    flag_dni = True
    while flag_dni:
        try:
            dni = int(input("Ingrese el DNI: "))
            flag_dni = False
        except ValueError:
            print("El DNI debe ser numérico")
    
    # Llamar a la función con los datos ingresados
    print(consultar_estado_cliente(dni))


def pedir_datos_modificacion_cliente():
    flag_dni = True
    while flag_dni:
        try:
            dni = int(input("Ingrese el DNI: "))
            flag_dni = False
        except ValueError:
            print("El DNI debe ser numérico")
    
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
    
    # Llamar a la función con los datos ingresados
    # modificar_datos_cliente(dni, nombre, apellido, telefono, direccion)
    print(modificar_datos_cliente(dni, nombre, apellido, telefono, direccion))




# ------------------------------------------------------------------- ALERTAS  DE LAS VISTAS ------------------------------------------------------------------- #

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
    print("║ 5. Salir                            ║")
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

def limpiar_consola():
    # Diferentes comandos para limpiar la consola en distintos sistemas operativos
    comandos_limpiar = {
        'posix': 'clear',  # Linux y macOS
        'nt': 'cls'  # Windows
    }

    # Obtener el comando correspondiente al sistema operativo actual
    comando = comandos_limpiar.get(os.name)

    # Si no se encuentra el comando correspondiente, se imprime un mensaje
    if comando is None:
        print("No se pudo limpiar la consola. Por favor, borra manualmente.")

    # Ejecutar el comando para limpiar la consola
    os.system(comando)


# ---------------------------------------------------- FUNCIONES QUE MANEJAN LA INTERFAZ, ES DECIR, LAS VISTAS DEL CLIENTE --------------------------------------- #

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
            continue

        if opcion == 1:
            estado_submenu_clientes = True

            while estado_submenu_clientes:
                limpiar_consola()
                submenu_clientes()

                try:
                    opcion_submenu_clientes = int(input("Elige el número de opción deseada: "))
                    estado_submenu_clientes = False 
                except ValueError:
                    print("Por favor, ingresa un número válido.")
                    continue
                
                if opcion_submenu_clientes == 1:
                    pedir_datos_alta_cliente()
                elif opcion_submenu_clientes == 2:
                    pedir_datos_baja_cliente()
                elif opcion_submenu_clientes == 3:
                    pedir_datos_consulta_estado_cliente()
                elif opcion_submenu_clientes == 4:
                    pedir_datos_modificacion_cliente()
                elif opcion_submenu_clientes == 5:
                    estado_submenu_clientes = False
                else:
                    print("Opción inválida. Por favor, elige una opción válida.")
        elif opcion == 2:
            # Código para el submenú de libros
            pass
        elif opcion == 3:
            # Código para el submenú de préstamos
            pass
        elif opcion == 4:
            estado_menu_principal = False
        else:
            print("Opción inválida. Por favor, elige una opción válida.")

programa()



"""
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
        
        # Aca comienza la gestion del submenu
        estado_submenu = True

        while estado_submenu:
            try:
                opcion_submenu_clientes = int(input("Elige el numero de opción deseada: "))
                estado_submenu = False
            except ValueError:
                mostrar_mensaje_error()
            else:
                ops_clientes = {
                    1: pedir_datos_alta_cliente,
                    2: pedir_datos_baja_cliente,
                    3: pedir_datos_consulta_estado_cliente,
                    4: pedir_datos_modificacion_cliente,
                    5: Salir
                }

                if opcion_submenu_clientes in ops_clientes:
                    ops_clientes[opcion_submenu_clientes]()                         
                else:
                    mensaje_dato_no_encontrado()
                    estado_submenu = True

programa()
"""