# Alta de Libro.
# Consultar un libro/película.
# Modificar Libro.
# Eliminar Libro.


def buscar_libro(ISBN):
    with open('libros.txt', "r+") as archivo:
        libros = archivo.readlines()
        for i, libro in enumerate(libros):
            indice_inicio_ISBN = libro.index("ISBN:") + len("ISBN: ")
            indice_final_ISBN = libro.index(" |", indice_inicio_ISBN)
            libro_ISBN = libro[indice_inicio_ISBN:indice_final_ISBN]
            if libro_ISBN == ISBN:
                return libro, i


def alta_libro(ISBN, titulo, autor, estado, DNI=0):
    resultado = buscar_libro(ISBN)
    if not resultado:
        with open('libros.txt', 'a') as libros:
            libros.write(
                f"ISBN: {ISBN} | Titulo: {titulo} | Autor: {autor} | Estado: {estado} | DNI: {DNI}\n")
        print(f"libro ISBN: {ISBN} | Titulo: {titulo} | Autor: {autor} | Estado: {estado} | DNI: {DNI} agregado con exito")
    else:
        print(f"ya existe un libro con ese ISBN: {resultado[0]} ")


def baja_libro(ISBN):
    resultado = buscar_libro(ISBN)
    if resultado:
        indice = resultado[1]
        with open('libros.txt', "r+") as archivo:
            libros = archivo.readlines()
            del libros[indice]
            archivo.seek(0)
            archivo.writelines(libros)
            archivo.truncate()
    else:
        print(f" No se encontro ningun libro con ISBN {ISBN}, no se puede eliminar ")

def modificar_libro(ISBN, campo, valor):
    resultado = buscar_libro(ISBN)
    if resultado:
        with open('libros.txt', "r+") as archivo:
            libros = archivo.readlines()
            libro, indice = resultado

            indice_inicio_campo = libro.index(f"{campo}:") + len(f"{campo}: ")
            indice_final_campo = libro.index(" |", indice_inicio_campo)

            libro_campo = libro[indice_inicio_campo:indice_final_campo]
            libro_modificado = libro.replace(libro_campo, valor)

            libros[indice] = libro_modificado
            archivo.seek(0)
            archivo.writelines(libros)
            archivo.truncate()
    else:
        print(f" No se encontro ningun libro con ISBN {ISBN}, no se pudo modificar ")
    
def consultar_libro(ISBN):
    resultado = buscar_libro(ISBN)
    if resultado:
        libro, indice = resultado
    print(f"El libro buscado es {libro}")