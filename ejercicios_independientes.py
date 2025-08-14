"""

nombre_apellido = input("ingresa tu nombre:")
edad = input("ingresa tu edad:")
print(edad)
nombre_apellido1 = input("ingresa tu nombre:")
edad1 = input("ingresa tu edad:")
print(edad1)
nombre_apellido2 = input("ingresa tu nombre:")
edad2= input("ingresa tu edad:")
print(edad2)
frase = f"{nombre_apellido }, {nombre_apellido1 } y {nombre_apellido2 } bienvenidos al SENA del programa de software"
print(frase)



lista_aprendices = [nombre_apellido, nombre_apellido1, nombre_apellido2]
print(lista_aprendices)
frase1 = ("quien es el mas juicioso de la clase: "+ lista_aprendices[1])
print(frase1)

for x in lista_aprendices:
    print(x)

    if x == nombre_apellido1:
       break

print(type(lista_aprendices))

if(edad < edad1):
    print("es menor que el compañero 1")
elif(edad1 >= edad2):
    print("es mayor que el compañero 2 ")
else:
    print("el compañero es menor que el compañero 1 y compañero 2")





nombre = "juan"
apellido = "gomez"
frase = f"{nombre } {apellido } is playing soccer "
print(frase)

lista_accesorios = ["balones", "uniformes deportivos", "sudaderas"]
print(lista_accesorios)
frase_accesorio = f"{nombre } {apellido } quiere comprar varios {lista_accesorios[1]}"
print(frase_accesorio)

for x in lista_accesorios:
    print(x)
    if x == "uniformes deportivos":
       pass"

lista_universidades2 = ["Santo Tomas", "Manuela Beltran", "Politecnico", "Javeriana"]
contador = 0 
for x in lista_universidades2:
    print(x)

for x in range(len(lista_universidades2)):
    print(lista_universidades2[x])"""""""""
""""""



"""nombre_persona = input("ingresa tu nombre: ")
print(nombre_persona)
frase = f"{nombre_persona} eres mi mejor amiga"
edad = input("ingresa tu edad: ")
print(edad)


for x in range(3):
    
    print(f"{nombre_persona}, {frase}")

    if x <= 22:
        print("es verdadero")
    else:
        ("falso")"""


"""animales = ["pato", "leon", "tiburones","ganso","loro"]

for bio in animales[2]:
    if(bio== "a" or bio== "e" or bio== "i" or bio== "o" or bio== "u"):
        print("es un vocal")
    else:
        print("es un consonante")"""


"""animales = ["pato", "leon", "tiburones","ganso","loro"]
contador = 0
while contador <5:
    print("contador", animales)
    contador +=1
else:
    ("DETENTE UN MOMENTO!")"""




"""animales = ["pato", "leon", "tiburones","ganso","loro"]
lista_universidades2 = ["Santo Tomas", "Manuela Beltran", "Politecnico", "Javeriana"]

for x in range(4):
        print(f"{animales[1]} esta enjaulados en la {lista_universidades2[-3]}")"""
        
"""nombre = str(input("ingresa tu nombre:"))
print(nombre)
edad = int(input("ingresa tu edad:"))
print(edad)

nombre_pareja = str(input("ingresar el nombre de tu pareja: "))
print(nombre_pareja)
edad_pareja = int(input("ingresar la edad de tu pareja"))
print(edad_pareja)


frase = f"{nombre} y {nombre_pareja} estan viajando juntos"
print(frase)

lista_viajes = ["Argentina", "Brasil", "USA","Spain"]

for paises in lista_viajes:
    print(paises)

contador= 0
while contador < len(lista_viajes):
    print(lista_viajes)
    contador += 1
    continue

if (edad >= 26):
    print("mi novia es mayor que yo")
else:
    print("soy menor que mi novia")


def viajes(*paises):
    print("el ultimo viaje es:" + paises[1])
viajes("Argentina", "Brasil", "USA","Spain")

def my_function(paises):
    for y in paises:
        print(y)

my_function(lista_viajes)

print("cuantos llevan años en diferencia: ")
def resta(x):
    return edad_pareja - x
print(resta(edad))
 """
 


# pidale el dulce a una amiga

"""nombre = str(input("ingresa tu nombre: "))
print(nombre)



def amistad(x):
    print(f"hola {x}")

amistad(nombre)

print("aqui tengo la lista de los dulces:")
lista_dulces = ["trululu", "chocolatina jet", "bianchi", "bon bon bum"]
lista_dulces.sort()
print(lista_dulces)

for y in lista_dulces:
    print(f"numero de dulces son: {lista_dulces.index(y)} y dulces: {y}")


dulce = input(f"elige un dulce que aparece en la lista:")
print(dulce)



if dulce in lista_dulces:
    print("si esta en la lista")
else:
    print("Intentalo Nuevamente")
 


for y in lista_dulces:
    print(f"{nombre}, compartamos {dulce} ?")
    break

answer = input("SI / NO: ")
print(answer)

if answer == "si":
    print("Acepto")
else:
    print("Lo siento mucho")
"""






# Se sincero con un mejor amiga si eres cliente operador

"""nombre = "Andrea"
apellido = "Roncancio"

def amistad(x):
    print(f"hola {x}, eres mi mejor amiga y llevamos un año de amistad!.")
amistad(nombre)

operador = "TIGO"

for y in operador:
    print(f"{nombre} {apellido}, Soy {operador} 'lo tienes'!")
    break

operador = input("SI / NO: ")

if operador == "si":
    print("Soy leal contigo")
else:
    print("Me arrepiento")"""




"""nombre = "Natalia"


def amistad(x):
    print(f"hola {x}, eres una persona impresionante!.")
amistad(nombre)

dulce = "bon bon bum"

for y in dulce:
    print(f"{nombre} , compartamos {dulce}?")
    break

respuesta = input("SI / NO: ")

if respuesta == "si":
    print("claro que si")
else:
    print("Lo siento mucho")"""

"""print("Suma los primeros tres numeros! ")
num_1 = int(input("ingresa primer numero:"))
num_2 = int(input("ingresa segundo numero:"))
num_3 = int(input("ingresa tercer numero:"))
lista_numeros = [num_1, num_2, num_3]

for x in lista_numeros:
    
    pass

suma = lista_numeros[0] + lista_numeros[1] + lista_numeros[2]

print(f"la suma de los tres numero son: {suma}")

if suma == 20:
        print("esta bien calculado")
else:
      print("corrigelo")
"""
       

"""print("conforma los grupos colaborativos:")

lista_de_compañeros = ["pedro", "marlon","julian","johan"]
lista_mayus = [x.capitalize() for x in lista_de_compañeros]
lista_mayus.sort()
print(lista_mayus)
print(len(lista_mayus))


for nombres in lista_mayus:
    print(f"Muy buenas noches, mi nombre es {nombres}. Soy el aprendiz número: {lista_mayus.index(nombres)}")
    continue

for numero_aprendices in lista_mayus:
    print(f"cuantos miembros del grupo colaborativo son: {len(lista_mayus)}")
    break

def fraseBonita():
    print("muchachos. Somos un gran equipo de trabajo para el proyecto de software llamado ALPIN ICE")
fraseBonita()"""
    
"""
try:
    def suma_multiplicacion(num):
        return 5 + 5 * num
    print(suma_multiplicacion("dsa"))

except TypeError:
    print("debes colocar un numero para completar la operacion")

raise TypeError("debemos salir de ese error")
"""

"""
nombre = str(input("ingresa un nombre: "))
print(nombre)

def amistad(x):
    print(f"hola {x}, como estas?. me haces mucha falta ")
amistad(nombre)

dulce = "bon bon bum"

def compartir_dulce(nombre,dulce):
    print(f"{nombre}, compartamos {dulce}?")
compartir_dulce(nombre,dulce)

respuesta = input("SI / NO: ")

if respuesta == "si":
    print("claro que si")
else:
    print("Lo siento mucho")"""
