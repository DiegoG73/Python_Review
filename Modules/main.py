"""
Un módulo es una funcionalidad ya hecha, lista para ser reutilizada (Se pueden administrar, instalar y crear)

En Python, por defecto, hay demasiados módulos (https://docs.python.org/3/py-modindex.html), existen otros más
en internet y también, podemos crear nuestros propios módulos
"""


# Así importamos los módulos propios:
import my_module
# También se puede utilizat un alias o importar solo una función específica
from my_module import helloWorld
import my_module as helloCalc
# O, podemos importar TODO lo que hay en el módulo con el "*": 
from my_module import *

#---------------------------------------------------------------------------


print(my_module.calculator(10,23,True))
#---------------------------------------------------------------------------
print(helloWorld("Diego Guzmán"))
#---------------------------------------------------------------------------
print("\n")
#---------------------------------------------------------------------------
print(helloCalc.calculator(12, 57, True))



# Módulo de Fechas:
import datetime

print(datetime.date.today())

complete_date = datetime.datetime.now()
custom_date = datetime.datetime.now()

print(complete_date)
print(complete_date.year)
print(complete_date.month)
print(complete_date.day)


# También, podemos crear fechas con formato personalizado:
custom_date = custom_date.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha personalizada es:", custom_date)

print(datetime.datetime.now().timestamp())




# Módulo de matemáticas:
import math

print("La raíz cuadrada de 10: ", math.sqrt(10))
print("Éste es el número PI:", float(math.pi))

# Funciones para redondear:
print("Redondear a la alza:", math.ceil(111.69)) # Me lo redondea a la alza
print("Redondear a la baja:", math.floor(111.69)) # Me redondea el número a la baja

# Números aleatorios:
import random
print("El número aleatorio entre el 10 y el 367 es:", random.randint(10, 367))  