# Mensaje de bienvenida al usuario
print("Welcome to REYES_MEZA_ALAN_1207_PRACTICA_07OCT24.py")
print(" ")

print("REYES MEZA ALAN EDUARDO :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

## Ejemplo 1: Llamar a la función con dos argumentos
def my_function(fname, refsnes):
    print(fname + " " + refsnes)

my_function("Emil", "Refsnes")
my_function("Tobias", "Refsnes")
my_function("Linus", "Refsnes")

# Ejemplo 2: Llamar a la función con 2 argumentos
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")

# Ejemplo 3: Llamar a la función con 1 argumento (esto dará un error)
def my_function(fname, lname):
    print(fname + " " + lname)

# my_function("Emil")  # Esta línea está comentada porque causará un error.

# Ejemplo 4: Usar un número variable de argumentos
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#7- También puede enviar argumentos con la sintaxis clave = valor.

#De esta forma no importa el orden de los argumentos.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")