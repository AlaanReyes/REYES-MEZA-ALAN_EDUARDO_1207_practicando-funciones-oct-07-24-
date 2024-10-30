# Mensaje de bienvenida al usuario
print("Welcome to REYES_MEZA_ALAN_1207_PRACTICA_07OCT24.py")
print(" ")

print("REYES MEZA ALAN EDUARDO :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

# 13 - Argumentos sólo posicionales
def my_function(x, /):
    print(x)

my_function(3)  # Correcto, imprime 3

# 14 - Sin / se permite usar argumentos de palabras clave
def my_function(x):
    print(x)

my_function(x=3)  # Correcto, imprime 3

# 15 - Error al usar argumento de palabra clave con /
def my_function(x, /):
    print(x)

# my_function(x=3)  # Esto dará un error: "TypeError: my_function() got an unexpected keyword argument 'x'"

# 16 - Argumentos de solo palabras clave
def my_function(*, x):
    print(x)

my_function(x=3)  # Correcto, imprime 3

# 17 - Sin *, se permite usar argumentos posicionales
def my_function(x):
    print(x)

my_function(3)  # Correcto, imprime 3

# 18 - Error al usar argumento posicional con *
def my_function(*, x):
    print(x)

# my_function(3)  # Esto dará un error: "TypeError: my_function() takes 0 positional arguments but 1 was given"

# 19 - Combinar solo posicional y solo palabras clave
def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

my_function(5, 6, c=7, d=8)  # Correcto, imprime 26
