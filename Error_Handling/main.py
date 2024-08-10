# MANEJO DE ERRORES
#* Capturar excepciones y manejar errores en código susceptible a fallos


#! Try 
try: 
    name = input("¿Cuál es tu nombre? ")

    if len(name) > 1:
        user_name = "Tu nombre es: " + name

    print(user_name)
except:
    print("Ha ocurrido un error, por favor ingresa un nombre válido")
else:
    print("El nombre es válido")
finally:
    print("Terminó la ejecución")