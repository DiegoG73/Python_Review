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
read_file = open(route, "r")

# Leer contenido
# content = read_file.read()
# print(content)


# Leyendo el contenido línea a línea 
list = read_file.readlines()
read_file.close()

for phrase in list:
    if not phrase.isnumeric():
        print("- " + phrase.center(50))
        
        
        
#* Copiar archivos, renombrar/mover archivos y eliminarlos:
import shutil
#! Copiar:
original_route = str(pathlib.Path().absolute()) + "/text_file.txt"
new_route = str(pathlib.Path().absolute()) + "/copied_file.txt"
alternative_route = "./Exercises/copied_file.txt"
# shutil.copyfile(original_route, alternative_route)
#! Renombrar arcehivos

shutil.copyfile 



#! Renombrar/Mover el archivo
original_route = str(pathlib.Path().absolute()) + "/text_file.txt"
new_route = str(pathlib.Path().absolute()) + "/NEW_copied_text.txt"
shutil.move(original_route, new_route)

#! ELIMINAR archivos
import os

new_route = str(pathlib.Path().absolute()) + "/NEW_copied_text.txt"
os.remove(new_route)

#! Comprobando si existe un directorio:
import os.path
# print(os.path.abspath("./"))

findout_route = os.path.abspath("./Files_System") + "/files.py"
print(findout_route)


if os.path.isfile(findout_route):
    print("El archivo existe")
else:
    print("El archivo no existe")