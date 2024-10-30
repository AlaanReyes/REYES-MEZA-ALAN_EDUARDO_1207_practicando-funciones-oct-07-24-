# Mensaje de bienvenida al usuario
print("Welcome to REYES_MEZA_ALAN_1207_PRACTICA_07OCT24.py")
print(" ")

print("REYES MEZA ALAN EDUARDO :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

# Ejemplo de valor de parámetro predeterminado
def my_function(country="no existe"):
    print("I am from " + country)

my_function("Sweden")  # Imprime: I am from Sweden
my_function("India")   # Imprime: I am from India
my_function()          # Imprime: I am from no existe
my_function("Brazil")  # Imprime: I am from Brazil

