# Mensaje de bienvenida al usuario
print("Welcome to REYES_MEZA_ALAN_1207_PRACTICA_07OCT24.py")
print(" ")

print("REYES MEZA ALAN EDUARDO :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

#10- Pasar una lista como argumento
#Puede enviar cualquier tipo de argumento de datos a una función (cadena, número, lista, diccionario, etc.) y será tratado como el mismo tipo de datos dentro de la función.

#P.ej. Si envía una Lista como argumento, seguirá siendo una Lista cuando llegue a la función:

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#11- Regresa Valores
#Para permitir que una función devuelva un valor, utilice la declaración de retorno:
def my_function(x):
  
    print(my_function(3))
    print(my_function(5))
    print(my_function(9))

#12- La declaración del pass
#las definiciones de función no pueden estar vacías, pero si por alguna razón tiene una definición de función sin contenido, ingrese la instrucción pass para evitar recibir un error.

def myfunction():
  pass