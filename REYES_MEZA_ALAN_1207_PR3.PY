# Mensaje de bienvenida al usuario
print("Welcome to REYES_MEZA_ALAN_1207_PRACTICA_07OCT24.py")
print(" ")

print("REYES MEZA ALAN EDUARDO :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

#8- Argumentos arbitrarios de palabras clave, **kwargs
#Si no sabe cuántos argumentos de palabras clave se pasarán a su función, agregue dos asteriscos: ** antes del nombre del parámetro en la definición de la función.
#De esta manera, la función recibirá un diccionario de argumentos y podrá acceder a los elementos en consecuencia:
#Si se desconoce el número de argumentos de palabras clave, agregue un doble ** antes del nombre del parámetro:

#Ícono de validado por la comunidad

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")