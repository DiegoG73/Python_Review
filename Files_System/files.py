from io import open
import pathlib

# Abrir archivos:
route = str(pathlib.Path().absolute()) + "/text_file.txt"
file = open(route, "a+")


# Escribir dentro de un archivo
file.write("************** Soy un texto introducido desde Python **************\n") 

# Debemos SIEMPRE cerrar el archivo:
file.close()



# Abrir archivo (el permiso "r" es de sólo lectura)
route = str(pathlib.Path().absolute()) + "/text_file.txt"
file = open(route, "r")

# Leer contenido
