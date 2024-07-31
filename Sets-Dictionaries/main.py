"""
SETs: Es un tipo de dato, para tener una colección de valores, pero que carece de índice y de orden:
"""

persons = {
    "Diego",
    "Manolito",
    "Agripino"
} # Así definimos un Set
print(persons)
print(type(persons))

# Con los Sets, también podemos agregar elementos
persons.add("Víctor")
print(persons)

# De igual forma, podemos eliminar valores con .remove()
persons.remove("Manolito")
print(persons)




"""
DICCIONARIOS: Es un tipo de dato que almacena un conjunto de datos en formato CLAVE-VALOR
    Es parecido a un array asociativo o un objeto JSON
"""
person = {
    "name": "Diego",
    "surname": "Guzmán",
    "web": "gocoding.com"
}

print(type(person))
print(person)
# Accediendo a los índices:
print(person["surname"])
print(person["web"])