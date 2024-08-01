"""
Crear un programa que compruebe si una variable está vacía, y, si está vacía, rellenarla con texto en minúsculas
y mostrarlo en mayúsculas
"""

text = "Halo Wars 2"

if len(text.strip()) <= 0:
    text = "vacío"
    textUp = text.upper()
    print(textUp)
else:
    print(f"La variable dice {text}")