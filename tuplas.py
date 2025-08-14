"""tupla = ("oso", "loro", "perro", "gato", "foca")
print(len(tupla))
print(type(tupla))
x = tupla.index("gato")
print(x)

for animales in tupla:
    print(f"numero de animales son: {tupla.index(animales)} es {animales}")"""



"""tupla = ("oso", "loro", "perro", "gato", "foca")
new_list = [x.lower() for x in tupla]
print(new_list)

primer_animal = tupla[1]
ultimo_animal = tupla[-1]
subtupla = tupla [1:4]

print(f"el primer animal es: {primer_animal}")
print(f"el ultimo animal es: {ultimo_animal}")
print(f"animales intermedios son: {subtupla}")

if "pajaro"  in tupla:
    print("es correcto")
else:
    print("no esta en la lista")
"""


# convierte tuplas en lista 
"""
print("conviertalo en lista!")
tupla = ("oso", "loro", "perro", "gato", "foca")
lista = list(tupla)
print(lista)

# añade la lista utilizando append.()

lista.append("tiburón")
lista.append("león")
print(lista)

# eliminar "loro" en la lista"

del lista [1]
print(lista)

# convierta en tuplas y actualizalo!

tupla = tuple(lista)
print(tupla)

# añade un elemento en una tupla existente
another_animal = ("Avestruz",)
tupla += another_animal
print(tupla)

"""



#conviertalo en diccionario!

"""print("conviertalo en diccionario: ")
tupla = ("oso", "loro", "perro", "gato", "foca")
print(tupla)
tupla = (("animal_1", "oso"), ("animal_2", "loro"), ("animal_3", "perro"), ("animal_4", "gato"), ("animal_5", "foca"))
diccionario = dict(tupla)
print(diccionario)"""


# Empaquetar y desempaquetar tuplas


"""tupla = ("oso", "loro", "perro", "gato", "foca")

animal_6 = "dinosaurio"
animal_7 = "tigre"
animal_8 = "Lagarto"
animal_9 = "Ornitorrinco"

nueva_tupla = (animal_6,animal_7,animal_8,animal_9)
print(nueva_tupla)

(animal_1,animal_2,animal_3,animal_4,animal_5) = tupla
print(tupla)

tupla_unida = tupla + nueva_tupla
print(tupla_unida)


#usando el asterisco *

(animal_1,*otros_animales)= tupla_unida
print(animal_1)
print(otros_animales)

(animal_1,animal_2,*otros_animales,ultimo_animal)= tupla_unida
print(animal_1)
print(otros_animales)
print(ultimo_animal)"""




"""comida = [("primero", "macarrones"), ("segundo", "pollo"), ("tercero", "brownie")]
print("la comida es: ")

for numero, plato in comida:
    print(f"{numero} === {plato}")

    pass


x= 0
while x < len(comida):
    print(comida[x])

    x += 1


utiles_escolares = {1 : "lapiz", 2: "boligrafo"}
y = utiles_escolares.items()
print(y)

for clave, valor in utiles_escolares.items():
    print(f"{clave}  {valor}")
    pass
"""

"""tupla = ("oso", "loro", "perro", "gato", "foca")
print(len(tupla))

contador = 0

for x in tupla:
    print(x)

# usamos el bucle con range() y len() para crear un 
# iterable adecuado
for x in range(len(tupla)):
    print(f"la frase es: {tupla[x]}")
    continue

##################################################################
while contador < len(tupla):
    print(f"los nombres de los animales son: {tupla[contador]}")
    contador += 1
    if contador == 2:
        print(contador)"""

tupla = ("oso", "loro", "perro", "gato", "foca")
print(len(tupla))

contador = 0



# usamos el bucle con range() y len() para crear un 
# iterable adecuado
for x in range(len(tupla)):
    print(f"la frase es: {tupla[x]}")
    continue
"""
##################################################################
while contador < len(tupla):
    print(f"los nombres de los animales son: {tupla[contador]}")
    contador += 1
    if contador == 0:
        print(contador)"""


