"""
    Guarda información en las entidades en la base de datos
"""

from base_datos import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute

# Crear una cadena que almacene la sentencia de ingreso de información
# se recuerda los atributos: nombre, apellido, equipo, numDorsal
# 1 Jugador
nombre = "Lionel"
apellido = "Messi"
equipo = "Paris Saint Germain PSG"
numDorsal = 30
cadena_sql = """INSERT INTO Jugador (nombre, apellido, equipo, numDorsal) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, equipo, numDorsal)

# ejecutar el SQL
cursor.execute(cadena_sql)

# 2 Jugador
nombre = "Neymar"
apellido = "da Silva"
equipo = "Paris Saint Germain PSG"
numDorsal = 10
cadena_sql = """INSERT INTO Jugador (nombre, apellido, equipo, numDorsal) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, equipo, numDorsal)

# ejecutar el SQL
cursor.execute(cadena_sql)

# 3 Jugador
nombre = "Kilian"
apellido = "Mbappe"
equipo = "Paris Saint Germain PSG"
numDorsal = 7
cadena_sql = """INSERT INTO Jugador (nombre, apellido, equipo, numDorsal) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, equipo, numDorsal)

# ejecutar el SQL
cursor.execute(cadena_sql)

# 4 Jugador
nombre = "Erling"
apellido = "Haaland"
equipo = "Manchester City"
numDorsal = 9
cadena_sql = """INSERT INTO Jugador (nombre, apellido, equipo, numDorsal) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, equipo, numDorsal)

# ejecutar el SQL
cursor.execute(cadena_sql)


# confirmar los cambios a través del objeto importado de tip Connection
conn.commit()

# cerrar el enlace a la base de datos (recomendado)
cursor.close()
