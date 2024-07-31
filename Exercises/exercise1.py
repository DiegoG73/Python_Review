"""
Hacer un programa que tenga una lista de 8 números enteros y que haga lo siguiente:
    - Recorrer la lista y mostrarla
    - Hacer una función que recorra listas de números y devuelva un string
    - Ordenarla y mostrarla
    - Mostrar su longitud
    - Buscar algún elemento (el que pida el usuario por teclado)
"""

# Creando la lista
numbers = [12,4,8,23,56,90,21,66,78,345,111,911]

# Recorriendo los números:
for number in numbers:
    print(number)
    

# Creando la función del segundo punto (devolver string):
def listToString(list):
    print("########## RECORRERR Y MOSTRAR ##########")
    
    result = ""
    
    for element in list:
        result += str(element)
        result += "\n"
    
    return result
    
print(listToString(numbers))

print("########## ORDENANDO LA LISTA ##########")
numbers.sort()
print(numbers)

print("########## LONGITUD DE LA LISTA ##########")
print(len(numbers))

def searching(list):
    print("\n########## BUSCANDO DENTRO DE LA LISTA ##########")
    value = int(input("Introduce el número que quieras buscar dentro de la lista: "))
    
    if value in list:
        print(f"El número {value} si existe dentro de la lista")
    else:
        print(f"El valor {value} no existe dentro de la lista")

searching(numbers)