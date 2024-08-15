
#* CONEXIÓN A LA BASE DE DATOS

#! Imporamos el módulo de SQLite3:
import sqlite3

#! Conexión
connection = sqlite3.connect('test.db')

#! Crear un cursor: ME PERMITE REALIZAR CONSULTAS A LA BASE DE DATOS:
cursor = connection.cursor()

#! CREANDO LA TABLA (SE HACE CON CONSULTAS SQL):
cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    title VARCHAR(255), 
    description TEXT, 
    price int(255)
)""")

#! Guardar los cambios con un commit:
connection.commit()

"""
#! Insertar datos en la tabla:
cursor.execute("INSERT INTO products VALUES (null, '1st Product', 'Description of the product', 550)")
connection.commit()
"""


#! BORRAR TODOS LOS DATOS DE LA TABLA
cursor.execute("DELETE FROM products")
connection.commit()

#! INSERTAR MUCHOS REGISTROS DE UNA SOLA VEZ:
products = [
    ("Laptop", "Buena laptop de 2024", 1000),
    ("Mouse", "Buen mouse para la pc", 100),
    ("Monitor", "Buen monitor para la pc", 700),
    ("Teclado", "Buen teclado para la pc", 100),
]
cursor.executemany("INSERT INTO products VALUES (null, ?, ?, ?)", products)
connection.commit()


#! ACTUALIZAR DATOS DE LA TABLA:
cursor.execute("UPDATE products SET price=150 WHERE price=100")


#! LISTAR DATOS DE MI TABLA:
cursor.execute("SELECT * FROM products WHERE price > 100")
products = cursor.fetchall()

for product in products:
    print("ID:", product[0])
    print("Title:", product[1])
    print("Description:", product[2])
    print("Price:", product[3])
    print("\n")
    
product = cursor.fetchone()
print(product)



#! Cerrar la conexión
connection.close()