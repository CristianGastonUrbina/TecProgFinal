from datetime import datetime
import os
import time

# ---------------------------------------------------------- FUNCIONES QUE MANEJAN EL MODELO DE DATOS ---------------------------------------------------------- #


def alta_cliente(dni, nombre, apellido, telefono, direccion):

    fecha_alta = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    estado= 'Activo'
    fecha_baja='NULL'
    isbn='NULL'

    cliente = {
        'DNI':dni,
        'Nombre':nombre.strip(),         # Agrego strip() para eliminar los espacios en blanco
        'Apellido':apellido.strip(),
        'Telefono':telefono,
        'Direccion':direccion.strip(),
        'Fecha_Alta':fecha_alta.strip(),
        'Fecha_Baja':fecha_baja.strip(),
        'ISBN_Libro':isbn,
        'Estado':estado.strip() 
    }

    # Registrar el alta en el archivo
    with open('Clientes.txt', 'a') as archivo:
        archivo.write(f"{cliente['DNI']},{cliente['Nombre']},{cliente['Apellido']},{cliente['Telefono']},{cliente['Direccion']},{cliente['Fecha_Alta']},{cliente['Fecha_Baja']},{cliente['ISBN_Libro']},{cliente['Estado']}\n")
    
    print("\nEl cliente ha sido dado de alta exitosamente")
    return cliente

def baja_cliente(dni):
    clientes_encontrados = []

    ruta = 'E:\\Escritorio\\tec-programacion\\TecProgFinal\\modulos\\Clientes.txt'
    with open(ruta, 'r') as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        cliente = linea.strip().split(',')  # ['39931865', 'Damian', 'Fortunesky', '1124354678', 'williams 11', '2023-07-06 22:20:34',  'NULL',  'NULL', 'Activo']
        
        cliente_dict = {
            'DNI': cliente[0],
            'Nombre': cliente[1].strip(),
            'Apellido': cliente[2].strip(),
            'Telefono': cliente[3],
            'Direccion': cliente[4].strip(),
            'Fecha_Alta': cliente[5].strip(),
            'Fecha_Baja': cliente[6].strip(),
            'ISBN_Libro': cliente[7],
            'Estado': cliente[8]  
        }

        if (
            cliente_dict['DNI'] == str(dni) and
            cliente_dict['Estado'] == 'Activo' and
            cliente_dict['ISBN_Libro'] == 'NULL'
        ):
            cliente_dict['Fecha_Baja'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cliente_dict['Estado'] = 'Inactivo'
            clientes_encontrados.append(cliente_dict)

    if clientes_encontrados:
        with open(ruta, 'w') as archivo:
            for linea in lineas:
                
                cliente = linea.split(',')
                cliente_dni = cliente[0]

                # Escribe los registros no coincidentes nuevamente en el archivo
                if cliente_dni != str(dni):
                    archivo.write(linea)
            
            # Recorre y escribe las coincidencias
            for cliente in clientes_encontrados:
                
                archivo.write(
                    f"{cliente['DNI']}, {cliente['Nombre']}, {cliente['Apellido']}, {cliente['Telefono']}, {cliente['Direccion']}, {cliente['Fecha_Alta']}, {cliente['Fecha_Baja']}, {cliente_dict['ISBN_Libro']}, {cliente['Estado']}\n"
                )

        nombre_cliente = f"{clientes_encontrados[0]['Nombre']} {clientes_encontrados[0]['Apellido'] } ha sido dado de baja exitosamente"

        print(nombre_cliente)
        return clientes_encontrados[0]

    print("No se encontró el cliente o el cliente tiene préstamos activos.")
    return None



def consultar_estado_cliente(dni):
    ruta = 'E:\\Escritorio\\tec-programacion\\TecProgFinal\\modulos\\Clientes.txt'

    with open(ruta, 'r') as archivo:
        lineas = archivo.readlines()

    for linea in lineas:

        cliente = linea.split(',')
        
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

        if cliente_dict['DNI'] == str(dni):
            nombre_cliente = cliente_dict['Nombre']
            estado_cliente = cliente_dict['Estado']  
            
            return f"{nombre_cliente}, su estado es: {estado_cliente}"       
        
    return print('Cliente no encontrado')



def modificar_datos_cliente(dni, nombre, apellido, telefono, direccion):
    ruta = 'E:\\Escritorio\\tec-programacion\\TecProgFinal\\modulos\\Clientes.txt'

    with open(ruta, 'r') as archivo:
        lineas = archivo.readlines()

    encontrado = False
    for i, linea in enumerate(lineas):
        datos = linea.strip().split(',')

        cliente = {
            'DNI': datos[0],
            'Nombre': datos[1],
            'Apellido': datos[2],
            'Telefono': datos[3],
            'Direccion': datos[4],
            'Fecha_Alta': datos[5],
            'Fecha_Baja': datos[6],
            'ISBN_Libro': datos[7],
            'Estado': datos[8].strip()
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

            cliente['Fecha_Alta'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            lineas[i] = f"{cliente['DNI']},{cliente['Nombre']},{cliente['Apellido']},{cliente['Telefono']},{cliente['Direccion']},{cliente['Fecha_Alta']},{cliente['Fecha_Baja']},{cliente['ISBN_Libro']},{cliente['Estado']}\n"

            encontrado = True
            break

    if encontrado:
        with open(ruta, 'w') as archivo:
            archivo.writelines(lineas)

        return 'Datos actualizados'
    else:
        return 'Cliente no encontrado'



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
    print(modificar_datos_cliente(dni, nombre, apellido, telefono, direccion))




# ------------------------------------------------------------------- ALERTAS  DE LAS VISTAS ------------------------------------------------------------------- #

def mostrar_menu_principal():
    print("                            ")
    print("╔══════════════════════════╗")
    print("║       Bienvenido a       ║")
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
    print("╠═════════════════════════════════════╣")
    print("║ 1. Alta Cliente                     ║")
    print("║ 2. Baja Cliente                     ║")
    print("║ 3. Consultar estado del cliente     ║")
    print("║ 4. Actualizar Datos                 ║")
    print("║ 5. Volver al Menu Principal         ║")
    print("╚═════════════════════════════════════╝")
    print("                                       ")

def mostrar_mensaje_error():
    print("                                        ")
    print("╔══════════════════════════════════════╗")
    print("║      Error al ingresar dato          ║")
    print("╠══════════════════════════════════════╣")
    print("║ Debe ingresar un Nº de opción válido ║")
    print("╚══════════════════════════════════════╝")
    print("                                        ")

def mensaje_dato_no_encontrado():
    print("                                        ")
    print("╔══════════════════════════════════════╗")
    print("║           Error de busqueda          ║")
    print("╠══════════════════════════════════════╣")
    print("║         Esa opcion no existe         ║")
    print("╚══════════════════════════════════════╝")
    print("                                        ")

def Salir():
    print("                                        ")
    print("╔══════════════════════════════════════╗")
    print("║                Adios                 ║")
    print("╠══════════════════════════════════════╣")
    print("║            Vuelva Pronto!            ║")
    print("╚══════════════════════════════════════╝")
    print("                                        ")

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

                    limpiar_consola()
                    pedir_datos_alta_cliente()
                    time.sleep(3.5)                       # Esperar 2 segundos                                 
                    estado_submenu_clientes = True

                elif opcion_submenu_clientes == 2:

                    limpiar_consola()
                    pedir_datos_baja_cliente()
                    time.sleep(3.5)      
                    estado_submenu_clientes = True

                elif opcion_submenu_clientes == 3:

                    limpiar_consola()
                    pedir_datos_consulta_estado_cliente()
                    time.sleep(3.5)                                   
                    estado_submenu_clientes = True

                elif opcion_submenu_clientes == 4:

                    limpiar_consola()
                    pedir_datos_modificacion_cliente()
                    time.sleep(3.5)       
                    estado_submenu_clientes = True

                elif opcion_submenu_clientes == 5:

                    estado_submenu_clientes = False
                    limpiar_consola()
                    estado_menu_principal = True

                else:
                    print("Opción inválida. Por favor, elige una opción válida.")
        elif opcion == 2:
            # Código para el submenú de libros
            pass
        elif opcion == 3:
            # Código para el submenú de préstamos
            pass
        elif opcion == 4:
            Salir()
            time.sleep(3.5)  
            limpiar_consola()
            estado_menu_principal = False
        else:
            print("Opción inválida. Por favor, elige una opción válida.")

programa()
