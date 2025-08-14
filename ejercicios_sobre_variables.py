# ejercicios sobre variables
# tipos de datos
""""
var_1 = "hola mundo"
var_2 = "sandra"
num1 = 12

print(var_2)
print(num1)
print("var_1")

#tipos de valores numericos

numero_entero1 = 12
print(numero_entero1)

numero_total1 = numero_entero1 + 3
print(numero_total1)

numero_total1 += 2
print(numero_total1)

valor_aritmetico = 15
valor_aritmetico = valor_aritmetico + 2
print(valor_aritmetico)


resta = 2
resta = valor_aritmetico + resta
print(resta)

multiplicacion = 12 * 12
print(multiplicacion)

multiplicacion = numero_entero1 * valor_aritmetico
print(multiplicacion)

division = multiplicacion / resta
print(division)
print(type(division))


potencia = 12**2 
modulo = 15/2
print(potencia)
print(modulo)


texto = "hola mundo"
text = 'el agua es importante "comillas dobles" para la vida'
text2 = "eso es 'comillas simples' todo amigos"
print(texto)
print(text)
print(text2)


num1 = 3
num2 = 3.5
text = "hola, pablo"
verdadero = True

print(type(num1),type(num2),type(text),type(verdadero))
"""

"""
x = "Lionel Messi"
y = 38
z = "Soccerplayer"

print(x)
print(y)
print(z)

print(x +" " + "is", y, "years old" + " " + "and he is a " + z)



import math
a = 81
raiz_cuadrada = math.sqrt(a)
print(raiz_cuadrada)"""

"""
a = 27
b = 8
raiz_cubica = a **(1/3)
print(raiz_cubica)

raiz_cubica2 = pow(b,1/3)
print(raiz_cubica2)

#usando numpy.cbrt()

import math 
c = 1000
raiz_cubica = math.cbrt(c)
print(raiz_cubica)

from datetime import datetime

ahora = datetime.now()  # Usa la función now directamente
print(ahora)"""


""""
def encontrar_pares(lista):
  
  Encuentra los números pares en una lista.

  Args:
    lista: Una lista de números enteros.

  Returns:
    Una nueva lista que contiene solo los números pares de la lista original.
  """
"""pares = []
  for numero in lista:
    if numero % 2 == 0:
      pares.append(numero)
  return pares

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = encontrar_pares(mi_lista)
print(f"Los números pares en la lista son: {pares}")"""






def name(nombre, apellido):
    return f"{nombre} {apellido}, eres divina"


print(name("andrea", "roncacio"))



