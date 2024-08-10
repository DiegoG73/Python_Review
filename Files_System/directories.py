import os, shutil

#* Crear una carpeta (FOLDER)
if not os.path.isdir('./myfolder'):
    os.mkdir('./myfolder')
else:
    print('El directorio ya existe')
    

#* Eliminar una carpeta
# os.rmdir('./myfolder')

"""∑
#* Copiar una carpeta
original_route = "./myfolder"
new_route = "./myfolder_copy"

shutil.copytree(original_route, new_route)
"""

#* Eliminar la carpeta copiada
# os.rmdir('./myfolder_copy')

#* Listar el contenido de una carpeta
print("El contenido de mi carpeta es:")
content = os.listdir('./myfolder')
# print(content)

for files in content:
    print(f"Fichero: {files}")