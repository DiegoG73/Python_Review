# MANEJO DE ERRORES
#* Capturar excepciones y manejar errores en código susceptible a fallos

"""
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
""" 


#* EXCEPCIONES MÚLTIPLES

try:
    number = int(input("Introduce el número para elevar al cuadrado: "))
    print("El cuadrado del número es: " + str(number * number))
except  TypeError:
    print("Debes convertir tus cadenas a enteros")
except ValueError:
    print("Por favor, introduce un número válido")
except Exception as err:
    print(type(err))
    print(f"Ha ocurrido un error: {type(err).__name__}")