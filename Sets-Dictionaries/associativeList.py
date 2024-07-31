"""
Creando una lista con diccionarios
"""

contacts = [
    {
        'name': 'Antonio',
        'email': 'antonio@antonio.com'
    },
    {
        'name': 'Rogelio',
        'email': 'roger@rogelio.com'
    },
    {
        'name': 'Macedonio',
        'email': 'macedonio@donmace.com'
    }
]

print(contacts)

# Accediendo a los valores de los diccionarios dentro de listas:
print(contacts[0]['name'])
print(contacts[2]['name'])

# Modificando los valores de los diccionarios dentro de listas:
contacts[0]['name'] = "Toño"
print(contacts[0]['name'])

# Mostrando el listado completo de contactos (iterandolos):
print("\n")
for contact in contacts:
    print(f"Name: {contact['name']}\nEmail: {contact["email"]}")
    print("\n")