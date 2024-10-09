# Mensaje de bienvenida al usuario
print("Welcome to REYES_MEZA_ALAN_1207_PRACTICA_07OCT24.py")
print(" ")

print("REYES MEZA ALAN EDUARDO :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

# Función que suma cuatro números (dos posicionales y dos nombrados)
def my_function(a, b, /, *, c, d):
    """
    Suma cuatro números.
    
    Parámetros:
    a (int): Primer número.
    b (int): Segundo número.
    c (int): Tercer número (nombrado).
    d (int): Cuarto número (nombrado).
    
    Salida:
    Imprime la suma de a, b, c y d.
    """
    print(a + b + c + d)

# Llamada a la función con ejemplos
my_function(5, 6, c=7, d=8)  # Salida: 26
print(" ")

# Función que imprime cada elemento de una lista
def my_function(food):
    """
    Imprime cada elemento de la lista proporcionada.
    
    Parámetros:
    food (list): Lista de alimentos.
    
    Salida:
    Imprime cada elemento de la lista.
    """
    for x in food:
        print(x)

# Lista de frutas
fruits = ["apple", "banana", "cherry"]
my_function(fruits)  # Salida: cada fruta en una línea
print(" ")

# Función con un parámetro con valor por defecto
def my_function(country="Norway"):
    """
    Imprime el país de origen.
    
    Parámetros:
    country (str): Nombre del país (valor por defecto es "Norway").
    
    Salida:
    Imprime el país.
    """
    print("I am from " + country)

# Llamadas a la función con diferentes países
my_function("Sweden")  # Salida: I am from Sweden
my_function("India")   # Salida: I am from India
my_function()          # Salida: I am from Norway
my_function("Brazil")  # Salida: I am from Brazil
print(" ")

# Función que imprime el apellido a partir de argumentos nombrados
def my_function(**kid):
    """
    Imprime el apellido a partir de argumentos nombrados.
    
    Parámetros:
    **kid: Argumentos nombrados (deben incluir 'lname').
    
    Salida:
    Imprime el apellido.
    """
    print("His last name is " + kid["lname"])

# Llamada a la función con nombre y apellido
my_function(fname="Tobias", lname="Refsnes")  # Salida: His last name is Refsnes
print(" ")

# Función que acepta solo un argumento posicional
def my_function(x, /):
    """
    Imprime el valor del argumento proporcionado.
    
    Parámetros:
    x (int): Un número entero.
    
    Salida:
    Imprime el número.
    """
    print(x)

# Llamada a la función
my_function(3)  # Salida: 3
print(" ")

# Función lambda que suma 10 a un número
x = lambda a: a + 10
print(x(5))  # Salida: 15
print(" ")

# Función lambda que suma tres números
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))  # Salida: 13
print(" ")

def my_function(fname):
  print(fname + " REYES")

my_function("ALAN")
my_function("SOFIA")
my_function("JOSE")
print(" ")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("REYES MEZA", "ALAN EDUARDO")
print(" ")

#Si no sabe cuántos argumentos se pasarán a su función, agregue un * antes del nombre del parámetro en la definición de la función.
#De esta manera, la función recibirá una tupla de argumentos y podrá acceder a los elementos en consecuencia:
#Si se desconoce el número de argumentos, agregue un * antes del nombre del parámetro:

def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
print(" ")

# Función que devuelve una función lambda multiplicadora
def myfunc(n):
    """
    Devuelve una función lambda que multiplica un número por n.
    
    Parámetros:
    n (int): Número por el cual se multiplicará.
    
    Salida:
    Una función lambda que multiplica su entrada por n.
    """
    return lambda a: a * n

# Creando un triplicador
mytripler = myfunc(3)
print(mytripler(11))  # Salida: 33
print(" ")

# Crear un duplicador y un triplicador
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))  # Salida: 22
print(mytripler(11))  # Salida: 33
print(" ")

# Ejemplo de uso de listas
cars = ["Ford", "Volvo", "BMW"]
print(" ")

# Modificando la lista de coches
x = cars[0]          # Ford
cars[0] = "Toyota"   # Cambiando Ford a Toyota
x = len(cars)       # Longitud de la lista
for x in cars:
    print(x)        # Salida: Toyota, Volvo, BMW
print(" ")

# Función que multiplica un número por 5
def my_function(x):
    """
    Multiplica el número proporcionado por 5.
    
    Parámetros:
    x (int): Un número entero.
    
    Salida:
    Retorna el resultado de 5 * x.
    """
    return 5 * x

# Llamadas a la función
print(my_function(3))  # Salida: 15
print(my_function(5))  # Salida: 25
print(my_function(9))  # Salida: 45

# Función recursiva que suma números
def tri_recursion(k):
    """
    Ejemplo de recursión que suma números desde k hasta 0.
    
    Parámetros:
    k (int): Un número entero positivo.
    
    Salida:
    Imprime la suma acumulativa.
    """
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)  # Muestra resultados de la recursión
print(" ")

# Importación de la biblioteca random
import random

# Función para simular un tiro a puerta
def tiro_a_puerta():
    """
    Simula un tiro a puerta aleatorio.
    
    Salida:
    Devuelve True si el tiro es a gol, False en caso contrario.
    """
    return random.choice([True, False])  # Devuelve True o False

# Función para simular un partido
def jugar_partido(equipo1, equipo2):
    """
    Simula un partido de fútbol entre dos equipos.
    
    Parámetros:
    equipo1 (str): Nombre del primer equipo.
    equipo2 (str): Nombre del segundo equipo.
    
    Salida:
    Retorna la cantidad de goles de ambos equipos.
    """
    goles_equipo1 = 0
    goles_equipo2 = 0

    for _ in range(90):  # Simulamos los 90 minutos de un partido
        if tiro_a_puerta():
            goles_equipo1 += 1
        
        if tiro_a_puerta():
            goles_equipo2 += 1

    return goles_equipo1, goles_equipo2

# Función para determinar el ganador
def determinar_ganador(goles1, goles2, equipo1, equipo2):
    """
    Determina el ganador del partido.
    
    Parámetros:
    goles1 (int): Goles del equipo 1.
    goles2 (int): Goles del equipo 2.
    equipo1 (str): Nombre del primer equipo.
    equipo2 (str): Nombre del segundo equipo.
    
    Salida:
    Retorna un mensaje indicando el ganador o si hay empate.
    """
    if goles1 > goles2:
        return f"El ganador es: {equipo1}"
    elif goles2 > goles1:
        return f"El ganador es: {equipo2}"
    else:
        return "El partido ha terminado en empate."

# Función principal para jugar el partido
def main():
    """
    Función principal que inicia el juego y muestra los resultados.
    """
    equipo1 = input("Nombre del equipo 1: ")
    equipo2 = input("Nombre del equipo 2: ")

    goles1, goles2 = jugar_partido(equipo1, equipo2)

    print(f"\nResultado final:")
    print(f"{equipo1} {goles1} - {goles2} {equipo2}")
    
    # Llamar a la función para determinar el ganador
    resultado = determinar_ganador(goles1, goles2, equipo1, equipo2)
    print(resultado)

if __name__ == "__main__":
    main()
    print(" ")

# Función para verificar la calificación
def verificar_aprobacion(calificacion, umbral=6):
    """
    Verifica si la calificación está aprobada.
    
    Parámetros:
    calificacion (float): Calificación del estudiante.
    umbral (float): Valor de umbral para aprobar (default es 6).
    
    Salida:
    Retorna un mensaje indicando si aprobó o no.
    """
    if calificacion >= umbral:
        return "¡Aprobaste!"
    else:
        return "No aprobaste."

# Función principal para verificar la calificación
def main():
    """
    Función principal que solicita una calificación y muestra el resultado.
    """
    try:
        calificacion = float(input("Ingresa tu calificación: "))
        resultado = verificar_aprobacion(calificacion)
        print(resultado)
    except ValueError:
          print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()