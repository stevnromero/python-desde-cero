""""
print("ingresa una palabra: ")
palabra = input()
for x in palabra:
    if (x == "a" or x == "e" or x == "i" or x == "o" or x == "u"):
        print(x)
    else:
        print("es un consonante")
"""""

"""
lista_aprendices = ["paulo", "patricia","lenny", "cristian"]

for x in lista_aprendices:
    print(x)

    if x == "patricia":
        break


devices = ["smartphones", "gps navigation", "laptop"]

for x in devices:
   
    
    if x == "laptop":
        continue
    print(x)
    

for x in range (2,4):
    print(x)
else:
    print("hasta ahi")



nombres = ["pablo", "lenny", "rafael", "romelino"]
apellidos = ["medusa", "saavedra", "santa", "arbelaez"]

for x in nombres:
    for y in apellidos:
        print(x)

"""        


"""
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 2


i = 0
while i < 6:
  i += 1
  if i == 2:
    continue
  print(i)


i = 5
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


frase = "hola eliana"
letra = "a"
count = 0

for caracter in frase:
    if (caracter == letra):
       count += 1
       print(f"la letra encontrada {count} veces")
       continue
    print("no hemos encnotrado nada")




nombre = ["andres", "lisa", "pablo","carlos"]

for alumnos in nombre:
    if alumnos == nombre:
        pass
    print(f"el alumno es {alumnos}")




Adivina_numero = 8

def fortune(Adivina_numero):
    Num = int(input("indicame un numero:"))
    if(Num == Adivina_numero):
        print("numero acertado")
        return True
    
    elif(Num < Adivina_numero):
        print("numero mas grande")
        return False
    
    elif(Num > Adivina_numero):
        print("numero mas pequeño")
        return False
    

while(not(fortune(Adivina_numero))):
       pass

else:
        print("juego terminado")





nombre_estudiante = input("indicame el nombre:")
print(nombre_estudiante)

nombre1 = nombre_estudiante

for x in range(10):
        print(nombre1)


#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).


age = int(input("¿Cuántos años tienes? "))
for i in range(age):
    print("Has cumplido " + str(i+1) + " años")




for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")

    """


"""lista_aprendices = ["Gerardo", "Sofia", "Ricardo", "Francisco","Andrea", "Bernardo"]
lista_aprendices.sort()
print(lista_aprendices)
print(len(lista_aprendices))

for sena in lista_aprendices:
    print(f"lista de aprendices por orden ascendiente es: {sena}")
    continue


contador = 0
while contador < len(lista_aprendices):
    contador +=1

    print(f"La ultima lista del aprendiz es: {lista_aprendices[1]}")
    break

i = int(input("ingresa un numero: "))
print(i)

while i < 5:
    print(i)
   
    if i ==2:
        print("es verdadero")
        break
    else:
        print("falso")
        break
    
    """

lista_aprendices = ["Gerardo", "Sofia", "Ricardo", "Francisco","Andrea", "Bernardo"]
lista_aprendices.sort()
print(lista_aprendices)
print(len(lista_aprendices))

