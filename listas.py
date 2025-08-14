""""
nombre = input("ingresa su nombre:")
print(nombre)

nombre1 = input("ingresa su nombre:")
print(nombre1)

nombre2 = input("ingresa su nombre:")
print(nombre2)

lista_aprendices= [nombre, nombre1, nombre2]
frase = f"quien es el vocero de la ficha? {nombre1}" 
print(frase)
longitud = len(lista_aprendices)
print(longitud)

for x in lista_aprendices:
    print(x)


#indexacion negativa 
lista_aprendices= ["pablo", "sara", "juan", "leidy", "wendy","victoria"]
print(type(lista_aprendices))

ultima_posicion = lista_aprendices[-1]
print(ultima_posicion)

posiciones_intermedio = lista_aprendices [1:4]
print(posiciones_intermedio)

valor_final = lista_aprendices [:4]
print(valor_final)

valor_inicial = lista_aprendices [1:]
print(valor_inicial)

default = lista_aprendices [-5:-2]
print(default)

if "juan" in lista_aprendices:
    print(f"si, {lista_aprendices[2]} está en la lista de aprendices SENA")




#comprobar si una lista contiene o no

nombre = input("ingrese su nombre:")
print(nombre)

nombre1 = input("ingrese su nombre:")
print(nombre1)

nombre2 = input("ingrese su nombre:")
print(nombre2)

lista_animal = [nombre, nombre1, nombre2]
print(type(lista_animal))


animal = nombre
animal1 = nombre1
animal2 = nombre2
animal_3 = "tiburon"

if animal_3 in lista_animal:
    print("si esta en la lista")

else:
    print("no esta incluida")


#Modificar o cambiar los elementos de las listas
numeroentero_1 = int(input("ingresa un numero:"))
numeroentero_2 = int(input("ingresa un numero:"))
numeroentero_3 = int(input("ingresa un numero:"))
numeroentero_4 = int(input("ingresa un numero:"))
numeroentero_5 = int(input("ingresa un numero:"))
numeroentero_6 = int(input("ingresa un numero:"))
print(numeroentero_1 ,numeroentero_2, numeroentero_3, numeroentero_4, numeroentero_5, numeroentero_6)

lista_numeros = [numeroentero_1, numeroentero_2, numeroentero_3, numeroentero_4,numeroentero_5,numeroentero_6]
print(type(lista_numeros))

lista_numeros[1] = 34
print(lista_numeros)

lista_numeros[1:4] = [14,35,20]
print(lista_numeros)

lista_numeros[:4] = [2,3,6,7]
print(lista_numeros)

lista_numeros[1:] = [5,10,24,51,17,27]
print(lista_numeros)

lista_numeros[-1] = 28
print(lista_numeros)

lista_numeros[-5:-1] = [100,23,321,99]
print(lista_numeros)



#ejercicio con el metodo insert()

lista_vehiculos = ["carro", "moto", "helicoptero","bicicleta"]
lista_vehiculos.insert(3,"bus")
print(lista_vehiculos)



#AGREGAR ELEMENTOS DE LAS LISTAS

lista_vehiculos = ["carro", "moto", "helicoptero","bicicleta"]
lista_vehiculos.append("tren")
print(lista_vehiculos)

lista_vehiculos2 = ["avion", "limusina", "scooter", "tractor"]
lista_vehiculos.extend(lista_vehiculos2)
print(lista_vehiculos)

lista_vehiculos2.extend(lista_vehiculos)
print(lista_vehiculos2) 




#Eliminar elementos de las listas
a_universidades2 = ["Santo Tomas", "Manuela Beltran", "Politecnico", "Javeriana"]

del lista_universidades2[1]
print(lista_universidades2)
print(type(lista_universidades2))


lista_universidades2.clear()
print(lista_universidades2)
lista_universidades = ["Uniminuto", "CUN", "Sergio Arboleda", "ECCI", "Los Andes"]

lista_universidades.remove("Uniminuto")
print(lista_universidades)

lista_universidades.pop(1)
print(lista_universidades)

lista_universidades.pop()
print(lista_universidades)

"""

"""list"""


"""keywords = []
ocurrencias = []

for x in range(5):
    keyword = input("ingresa una palabra:")
    if keyword == "fin":
        break

    else:
        keywords.append(keyword)

        print(keywords)


posicion = 0
while(True):
    if posicion >= (len(keywords)):
       break
    if keywords[posicion] == '':
        keywords.pop(posicion)
    elif keywords[posicion].isnumeric():
        keywords.pop(posicion)
    else:
        posicion += 1


print("lista de keywords corregida")
print(keywords)


texto = "hola"

for x in range(len(keywords)):
    ocurrencias.append(0)


for palabra in texto:
    for keyword in keywords:
        if keyword == palabra:
            pos = keywords.index(keyword)
    for keyword in keywords:
        if keyword == palabra:
            pos = keywords.index(keyword)"""


#ejercicios con bucles
"""
lista_universidades2 = ["Santo Tomas", "Manuela Beltran", "Politecnico", "Javeriana"]

for x in lista_universidades2:
    print(x)
"""
"""for x in range(len(lista_universidades2)):
    print(lista_universidades2[x])"""

"""contador = 0 
while contador < len(lista_universidades2):
    print(lista_universidades2[contador])
    contador += 1"""
""""
new_list= ["holamundo" for x in lista_universidades2]
print(new_list)
"""

""""lista_universidades2.sort()
print(lista_universidades2)"""

"""new_list = [x.upper() for x in lista_universidades2]
print(new_list)"""


"""lista_universidades2 = ["santo tomas", "Manuela Beltran", "Politecnico", "javeriana"]

lista_universidades2.sort()
print(lista_universidades2)

lista_universidades2.sort(key = str.lower)
print(lista_universidades2)"""


"""lista_ropa = ["sweaters", "zapatos", "jeans", "camisetas"]
lista_ropa.sort(reverse = True)
print(lista_ropa)

lista_ropa = ["sweaters", "Zapatos", "jeans", "Camisetas"]
lista_ropa.reverse()
print(lista_ropa)"""

"""lista_ropa = ["sweaters", "Zapatos", "jeans", "Camisetas"]
lista_ropa.copy()
print(lista_ropa)

lista_ropa = ["sweaters", "Zapatos", "jeans", "Camisetas"]
mi_lista = list(lista_ropa)
print(mi_lista)"""

"""lista_ropa = ["sweaters", "Zapatos", "jeans", "Camisetas"]
mi_lista = lista_ropa[:]
print(mi_lista)

lista_ropa = ["sweaters", "Zapatos", "jeans", "Camisetas","sweaters"]
x = lista_ropa.index("sweaters")
print(x)"""

"""lista_numeros = [5,10,24,51,17,27]
lista_ropa = ["sweaters", "Zapatos", "jeans", "Camisetas","sweaters"]
lista_random = lista_numeros + lista_ropa
print(lista_random)


lista_numeros = [5,10,24,51,17,27]
lista_ropa = ["sweaters", "Zapatos", "jeans", "Camisetas","sweaters"]
lista_ropa.extend(lista_numeros)
x = lista_ropa.index("Zapatos")
y = lista_numeros.index(10)
print(lista_ropa)
print(f"{x} tiene la talla de calzado numero {y}")"""


"""lista_numeros = [5,10,24,51,17,27]
lista_ropa = ["sweaters", "Zapatos", "jeans", "Camisetas","sweaters"]

for x in lista_numeros:
    lista_ropa.append(x)
    if x == 24:
        continue

    print(lista_ropa)"""

# format strings
# nos permite generar strings combinando texto con otras variables de forma sencilla y legible

"""lista_numeros = [5,10,24,51,17,27]
lista_ropa = ["sweaters", "Zapatos", "jeans", "Camisetas","sweaters"]
print("javier se compro un par de " + str(lista_ropa[1]) + " de calzado " + str(lista_numeros[-1]))
print("javier se compro un par de {} de calzado {}.".format(lista_ropa[1], lista_numeros[-1]))
print(f"javier se compro un par de {lista_ropa[1]} de calzado {lista_numeros[-1]}.")"""




# ejercicios con bucle



"""
frase = [1, 3, 6, 10]
numeros_enteros = []
for numero in frase:
    
    if numero in (2,4,6,8,10,12,14,16,18,20):
        print(f"{numero} es par")
        numeros_enteros.append(numero)

    else:
        print(f"{numero} es impar")    

print(numeros_enteros)
"""

    
