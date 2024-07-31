#* Métodos y funciones predefinidas de las listas:

singers = ["Elvis Presley", "Eminem", "Drake", "Travis Scott", "Aurora"]
numbers = [1,2,5,8,3,4]

# Ordenar una lista:
print(numbers)
numbers.sort()
print(numbers)

# Añadir elementos
singers.append("Sam Smith")
singers.insert(2, "Pop Smoke") # Añade un elemento en el índice especificado
# Imprimiendo el resultado:
print(singers)


# Eliminando elementos de una lista
singers.pop(1) # Éste método lo hace con base a un índice que nosotros especifiquemos
print(singers)
singers.remove("Sam Smith")
print(singers)



# Dar la vuelta a una lista:
print(numbers)
numbers.reverse()
print(numbers)



# Buscando dentro de la lista:
print('Drake' in singers)



# Contando elementos:
print(singers)
print(len(singers))




# Contando la cantidad de veces que aparece un elemento dentro de la lista:
print(numbers)
numbers.append(8)
print(numbers.count(8))


# Conseguir un índice
print(f"El índice al que pertenece 'Drake' es: {singers.index("Drake")}")





# Unir Listas:
singers.extend(numbers)
print(singers)

numbers.extend(singers)
print(numbers)