
#* Importamos el módulo de MySQL connector:
import mysql.connector

#! Conexión a la base de datos
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_review"
)
# print(database)


#! Creando el cursor para la base de datos (como en el archivo sqlite.py) 
#* El buffered=True se coloca para evitar fallos al utilizar el cursor varias veces
cursor = database.cursor(buffered=True)
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS python_review")

cursor.execute("SHOW DATABASES")


for db in cursor:
    print(db)
"""
    
#! Creando tablas en la base de datos:
cursor.execute("""
    CREATE TABLE IF NOT EXISTS VEHICLES(
        id int(10) auto_increment not null,
        brand varchar(40) not null,
        model varchar(40) not null,
        price float(10, 2) not null,
        CONSTRAINT pk_vehicle PRIMARY KEY(id)
    )
""")

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)


"""
#! Inserción de un dato en la base de datos:
cursor.execute("INSERT INTO VEHICLES VALUES(null, 'Ferrari', 'SF90 Spider', 995000)")
database.commit()
"""

#! Inserción masiva de datos:
cars = [
    ('Lamborghini', 'Huracán Performante', 300000),
    ('Tesla', 'Model S', 100000),
    ('Jaguar', 'Type X', 12000),
    ('Citroën', 'Saxo', 14500),
    ('Mercedes', 'GLA 500', 56000)
]

"""
cursor.executemany("INSERT INTO VEHICLES VALUES (null, %s, %s, %s)", cars)
database.commit()
"""

#! Sacando toda la información de mi base de datos con Python y MySQL
cursor.execute("SELECT * FROM VEHICLES WHERE price <= 15000 AND brand = 'Jaguar'")
result = cursor.fetchall()

print("---------- TODOS MIS COCHES  ----------")
for car in result:
    print(car[1], car[3])


"""
#! Sacando solo información concreta con FetchOne:
cursor.execute("SELECT * FROM VEHICLES")
car = cursor.fetchone()

print(car)
"""


#! BORRANDO DATOS:
cursor.execute("DELETE FROM VEHICLES WHERE brand = 'Ferrari'")
database.commit()

print(cursor.rowcount, "Deleted!")

#! ACTUALIZAR REGISTROS:
cursor.execute("UPDATE VEHICLES SET model='AMG GT' WHERE brand = 'Mercedes'")
database.commit()

print(cursor.rowcount, "Updated!") 