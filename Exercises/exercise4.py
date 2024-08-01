"""
Crear un script que tenga 4 variables que sean: una lista, un string, un entero, y un booleano y que imprima
un mensaje según el tipo de dato de cada variable. Usar funciones
"""
def typeTranslate(typeOf):
    result = None
    if typeOf == list:
        result = "List"
    elif typeOf == str:
        result = "String"
    elif typeOf == bool:
        result = "Boolean"
    elif typeOf == int:
        result = "Integer"
        
    return result

def dataType(data, typeOf):
    test = isinstance(data, typeOf)
    result = ""
    
    if test:
        result = print(f"Esta variable es de tipo: {typeTranslate(typeOf)}")
    else:
        result = None
        
    return result

my_list = ["Hello World", 73]
my_string = "Hello my friend"
my_integer = 73
my_bool = False


print(dataType(my_list, list))