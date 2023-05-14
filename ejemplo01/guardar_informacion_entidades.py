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
# se recuerda los atributos: nombre, liga, pais, cantJugador
# 1 Equipo
nombre = "Atletico de Madrid"
liga = "Santander"
pais = "España"
cantJugador = 25
cadena_sql = """INSERT INTO Equipo (nombre, liga, pais, cantJugador) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, liga, pais, cantJugador)

# ejecutar el SQL
cursor.execute(cadena_sql)

# 2 Equipo
nombre = "Barcelona FC"
liga = "Santander"
pais = "España"
cantJugador = 25
cadena_sql = """INSERT INTO Equipo (nombre, liga, pais, cantJugador) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, liga, pais, cantJugador)

# ejecutar el SQL
cursor.execute(cadena_sql)

# 3 Equipo
nombre = "Real Madrid"
liga = "Santander"
pais = "España"
cantJugador = 25
cadena_sql = """INSERT INTO Equipo (nombre, liga, pais, cantJugador) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, liga, pais, cantJugador)

# ejecutar el SQL
cursor.execute(cadena_sql)

# 4 Equipo
nombre = "Bayern Munich"
liga = "Bundesliga"
pais = "Alemania"
cantJugador = 25
cadena_sql = """INSERT INTO Equipo (nombre, liga, pais, cantJugador) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, liga, pais, cantJugador)

# ejecutar el SQL
cursor.execute(cadena_sql)


# confirmar los cambios a través del objeto importado de tip Connection
conn.commit()

# cerrar el enlace a la base de datos (recomendado)
cursor.close()
