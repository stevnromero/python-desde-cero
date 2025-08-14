"""texto = "johan"
edad = 22
nombre_pareja = "Valentina"

print("los mejores alumnos son:" + texto + " " + "y" + " " + nombre_pareja)

texto_1 = """
"""_______________________________________
mi novia y yo terminamos cuando estabamos
en la escuela secundaria de Loreto. actualmente, volvimos juntos
con una pareja feliz."""

"""

print(texto_1)

texto = "johan"
edad = 22
nombre_pareja = "Valentina"

print("los valores son originales:")
print(type(texto))
print(type(edad))
print(type(nombre_pareja))


texto = str("johan")
edad = str(22)
nombre_pareja = str("valentina")

print("los valores son modificados:")
print(type(texto))
print(type(edad))
print(type(nombre_pareja))



nombre_cliente = "Santiago"
ropa = "Camiseta"
lugar = "New York"

texto_unido = "la frase es: " + nombre_cliente + " se estrenó la " + ropa + " en la ciudad de " + lugar
print(texto_unido)


print(nombre_cliente.index("i"))

for x in range(5):
    print(nombre_cliente)
    break"""

"""Contador = 0
ropa = input("nombre de ropa: ")
print(ropa)
for letra in ropa:
    print("cuantos numero de caracteres: " + (letra))"""
    

"""numeros = "2131221214"
total = 0

for x in numeros:
    total += int(x)

else:
    print("valor de suma es: " + str(total))"""


# exercise with in

"""texto = input("ingresa una frase de amor:")
print(texto)

if("amor" in texto):
    print("si esta en la linea de texto")
else:
    print("no esta en la linea de texto")"""

# exercise with not in

"""texto = input("ingresa una frase:")
print(texto)
print(texto.upper())
print("laptop" not in texto)"""

# exercise con strip()

"""texto = " vamos a ver la pelicula, destino final 6 en CineColombia. "
b = texto.strip()
print(b)

texto = "###Hola Mundo###"
texto_limpio = texto.strip("#")
print(texto_limpio)  # Output: Hola Mundo"""


#ejercicio con replace()

"""texto = "vamos a ver la pelicula, destino final 6 en CineColombia."
b = texto.replace("vamos", "let´s go")
print(b)"""


#ejercicios con index() y find()
"""texto = "vamos a ver la pelicula, destino final 6 en CineColombia."
b = texto.index("v", 0, 9)
print(b)

txt = "hello, welcome to the world"
print(txt.find("z"))"""

"""texto_2 = "manzanas son limpias que las manzanas sucias"
x = texto_2.count("manzanas")
print(x)

texto_2 = "manzanas son limpias que las manzanas sucias mas que limpias"
x = texto_2.count("limpias" , 10, 40)
print(x)

print(f"es frase tiene: {len(texto_2)}")"""



# ejercicio de hoy

"""des1 = "Este bolso de cuero de la marca: Miguel Cors tiene un precio de 199.99$. Es una oferta especial."
des2 = "Las botas de la marca: Nique Valen 89$. Nunca han estado tan rebajadas"
des3 = "¡tenemos en bambu en oferta! compralo ahora por 1.2$ el kg ¡no la dejes pasar!"

def findPriceAndPlace(txt):
    txtlist = txt.split()
    pos = -1
    indx = -1
    conversion = 1.21

    for palabra in txtlist:
        pos = palabra.find('$')
        if pos != -1:
            indx = txtlist.index(palabra)
            break
        
        precio = txtlist[indx]
        precio = precio.split('$')[0]
        txtlist[indx] = precio * conversion + '$'
        nuevaDescripcion = " ".join(txtlist)
        return precio, nuevaDescripcion
    
   
precio, descripcion = findPriceAndPlace(des1)
print(precio)
print(descripcion)



precio, descripcion = findPriceAndPlace(des2)
print(precio)
print(descripcion)

precio, descripcion = findPriceAndPlace(des3)
print(precio)
print(descripcion)"""

"""texto = "vamos a ver la pelicula, destino final 6 en CineColombia."
texto_title = texto.title()
print(texto_title)

texto = "vamos a ver la pelicula, destino final 6 en CineColombia."
texto_capitalize = texto.capitalize()
print(texto_capitalize)


texto = "vamos a ver la pelicula, destino final 6 en CineColombia."
texto_startwith = texto.startswith("ver")
print(texto_startwith)

texto = "vamos a ver la pelicula, destino final 6 en CineColombia."
texto_startwith = texto.startswith("ver", 8 ,25)
print(texto_startwith)



texto = "vamos a ver la pelicula, destino final 6 en CineColombia."
texto_rjust = texto.rjust(len(texto)+8)
print(texto_rjust)


texto = "CineColombia."
texto_rjust = texto.rjust(18, "a")
print(texto_rjust)
"""


"""mi_cadena = "Hola mundo"
indice_o = mi_cadena.index('o')
print(f"El índice de la primera 'o' es: {indice_o}")"""

texto_1 = """_______________________________________
mi novia y yo terminamos cuando estabamos
en la escuela secundaria de Loreto. actualmente, volvimos juntos
con una pareja feliz."""


print(texto_1)

texto = "johan"
edad = 22
nombre_pareja = "Valentina"

print("los valores son originales:")
print(type(texto))
print(type(edad))
print(type(nombre_pareja))