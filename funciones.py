"""
# Definicion de funciones

def greetings():
    print("hello, brother")

def dialogue():
    print("hola amigo. como estas?")

greetings()
dialogue()

# Funciones con argumentos

def emplooyee(name):
    print("hola " + "soy " + name)

emplooyee("santiago")
emplooyee("paula")

def employee2(fname,sname):
    print("buenos dias " + "sr " + fname + " " + sname)

employee2("leydi","cardenas")




#argumento arbitrario

def university(*alumno):
    print("el ultimo puesto fue " + alumno[2] + " y el primer puesto fue " + alumno[0])

university("paula" , "andres", "sebastian", "pablo")



#argumento palabra clave

def university(alumno1, alumno2, alumno3, alumno4):
    print("el ultimo puesto fue " + alumno1 + " y el primer puesto fue " + alumno3)

university(alumno1= "paula" , alumno2= "andres", alumno3= "sebastian", alumno4= "pablo")


#argumento clave arbitraria

def university(**alumno):
    print("el ultimo puesto fue " + alumno["alumno1"] + " y el primer puesto fue " + alumno["alumno2"])
    print("el mejor futbolista del mundo es: " + alumno["alumno1"])
university(alumno1= "paula" , alumno2= "andres", alumno3= "sebastian", alumno4= "pablo")




def soccer(nombre1, apellido1):
    print("el mejor futbolista del mundo es " + nombre1 + " " + apellido1)
          

soccer(nombre1="lionel",apellido1="Messi")


def family(parentesco1 = "mamá"):
    print("hola " + parentesco1)


family("abuela")
family("papá")
family("tía")
family("hijo")
family()



def tech(nombre, apellido, *args):
    print("nombre de cliente: " + nombre)
    print("apellido:" + apellido)
    for yes in devices:
        print("nombre del dispositivo: " + yes)

devices = ["smarthphones" , "gps navigation", "laptop", "videocamera"] 
tech("pablo", "escobar",*devices)

a, b, c, d = devices

print(a + ", " + b + ", " + c + ", " + d)



def cantante(nombre1, nombre2, nombre3, *args):
    print("quien es la banda mas popular: " + nombre1)
    print("cual es tu banda favorita: " + nombre2)
    print("quien tiene mas seguidores: " + nombre1) 

    for cv in songs:
        print("nombre de la cancion: " + cv)

songs = ["whatve done", "american idiot", "one"]
cantante("linkin park", "Green Day", "Metallica",*songs)



def resta_de_tres(a, b, c):
    return a - b - c
valor_resta = resta_de_tres(10,2,3)
print(valor_resta)


def menores(num1,num2):
    return num1 <= num2
valor = menores(13,45)
print(valor)
valor = menores(45,13)
print(valor)

def soccerplayers(nombre,apellido):
    return nombre + " " + apellido
goat = soccerplayers("Lionel","Messi")
print(goat)
goat = soccerplayers("Cristiano","Ronaldo")
print(goat)


def party(edad):
    return edad

edad = party(input("ingresa tu edad: "))
edad = int(edad)

if(edad >=18):
    print("puedes pasar")  

elif(edad ==17):
    print("entras minimo a los 17 años")

else:
    print("no puedes entrar")



def multiplicacion(x):
    return 5 * x
print(multiplicacion(3))

"""

# ejercicios practicos



def multiplicacion(x):
    return 5 * x


def resta(x):
    return 5 + x


