"""
Escribir un programa que añada valores a una lista mientras que su longitud sea menor a 120 y luego mostrar la lista

Punto extra: Usar bucle While y For
"""

collection = []
x = 0

for counter in range(0,120):
    collection.append(f"elemento-{counter}")
    print("Mostrando el: " + collection[counter])
    
print(collection[111])


while x < 120:
    collection.append(f"elemento-{x}")
    print("Mostrando el: " + collection[counter])
    x += 1
    
print(collection[77])