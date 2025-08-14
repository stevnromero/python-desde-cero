""""
verdadero = True
falso = False



if(verdadero==True):
    print("hice la tarea")

if(falso==False):
    print("lave los platos")


# ejercicios con operadores de comparacion

nombre1 = "carlos"
nombre2 = "fabio"
nombre3 = "andrés"
edad_carlos = 22
edad_fabio = 15
edad_andrés = 20
hermanos = f"{nombre1}, {nombre2} y {nombre3} son hermanos propios"
print(hermanos)

if(edad_carlos <= edad_fabio):
    print("carlos es mayor que fabio")

elif(edad_fabio >= edad_andrés):
    print("fabio es muy joven")

else:
    print("andres es mayor que fabio")

print(type(hermanos))

# operacion con operadores logicas and, or, not

age = input("how old are you:")
age = int(age)

if(type(age)==int):
    if(age >=18 and age <=40):
        print("puedes pasar")

    elif(age <=17 and age <20):
        print("no puedes entrar")

    elif(age ==40 or age<17):
        print("minimo entras a los 40 años")

    else:
        print("prohibido personas con problemas auditivos")

    print(type(age))

if(not(age<=18)):
    print("puedes pasar")
    

a = "12"
b = "1.23"
c = "43.344"
print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())


prac = "134"
x = (prac.isnumeric())
print(x)

expo = "b^2/3"
y = (expo.isnumeric())
print(y)

num1 = 20
resto1 = num1 % 2
print(resto1)

num2 = 23
resto2 = num2 % 2
print(resto2)


def es_par(num1):
    return num1 % 2 ==0
print(es_par(num1))

def no_par(num2):
    return num2 % 2 == 0
print(no_par(num2))

"""""
""""

num = input("ingresa un numero:")
num = int(num)

if(num % 2 ==0):
    print("es par")

else:
    print("es impar")



"""""
""""


print("ingrese un valor:")
renta = float (input())
print(f"que tipo de renta:")

if(renta< 10000):
    print("5% del imposivo")

elif(renta >10000 and renta <20000):
    print("15% del imposivo")

elif(renta >20000 and renta <35000):
    print("20% del impsotivo")

else:
    print("más del 60% del imposivo")


"""


with open("practica.txt","rt") as find:

    if "prioridad" or "andreita" in find.readable():
        print("el texto si aparece en el fichero")
    else:
        print("no aparece en el fichero")