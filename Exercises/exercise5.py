"""
Crear una lista con el contenido de la tabla:

ACCIÓN      AVENTURA        DEPORTES
GTA      Assasin's Creed    EA FC 24        
CoD      Crash Bandicoot    Pro 24
PUBG     Prince of Persia   Moto GP 24

Mostrar la información ordenada
"""

table = [
    {
        "categoría": "ACCIÓN",
        "juegos": ["GTA", "Call of Duty", "PUBG"]
    },
    {
        "categoría": "AVENTURA",
        "juegos": ["Assassin's Creed", "Crash Bandicoot", "Prince Of Persia"]
    },
    {
        "categoría": "DEPORTES",
        "juegos": ["EA FC 24", "Pro 24", "Moto GP 24"]
    }
]

for category in table:
    print(f"---------------{category['categoría']}---------------")
    for game in category['juegos']:
        print(game)