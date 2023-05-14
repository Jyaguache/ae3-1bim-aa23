"""
    Crear entidades en la base de datos
"""

from base_datos import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute

# Crear una tabla denominada Jugador
# con atributos: nombre, apellido, equipo, numDorsal

cadena_sql = 'CREATE TABLE Jugador (nombre TEXT, apellido TEXT, equipo TEXT, \
            numDorsal INTEGER)'

# ejecutar el SQL
cursor.execute(cadena_sql)

# cerrar la enlace a la base de datos (recomendado)
cursor.close()
