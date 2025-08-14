"""def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))



print(my_resta(15))
print(my_resta(2))"""

#primer ejercicio
"""def sumar_todo(*args):
    total = 0
    for numero in args:
        total += numero
    return total
pass
     
     
resultado_1 = sumar_todo(1,2,3)
print(f"el primer resultado de la suma es {resultado_1}")

resultado_2 = sumar_todo(5,10,15,20)
print(f"el segundo resultado es: {resultado_2}")"""


"""def PrintKwargs(**kwargs):
    print("los atributos del personaje son: ")
    for clave, valor in kwargs.items():
        print(f"{clave},{valor}")


PrintKwargs(nombre = "leonitas", clase= "guerrero", raza = "humano", mascota= "Dragon", clan= "Espartanos")
PrintKwargs(clase = "mago", elfo = "elfo", nombre= "mandalorian")
"""

#combinaciones con args y kwargs


"""def crearPersonaje(nombre,*args,**kwargs):
    descripcion = f"### {nombre.upper()}###\n\n"
    descripcion += "#### DESCRIPCION ###\n\n"
    for clave, valor in kwargs.items():
        descripcion += f"{clave},{valor}\n" 
    descripcion = "##Habilidades##\n\n"
    for skill in args:
        descripcion += f" - {skill}\n"
    return descripcion

personaje = crearPersonaje("leonitas", "guerrero", "humano", mascota= "Dragon", clan= "Espartanos", elfo = "elfo")
print(personaje)



def crearvehiculos(nombre, placa, marca):
    frase = f"{nombre} tiene la placa{placa} de la marca{marca}"
    print(frase)

crearvehiculos("carro", "RT183", "chevelet")
crearvehiculos(marca = "AKT", nombre = "moto", placa = "VY858")
print(crearvehiculos)

"""

"""

def mostrar_argumentos(*args):
    
    for word in args:
        print(f"la palabra verdadera es: {word}")

    pass

mostrar_argumentos('Python', True, 3.14, [1, 2, 3])


def mostrar_info(**kwargs):
    print(f"los nombre de las personas son:")
    for clave, valor in kwargs.items():
        print(f"{clave}===={valor}")
    pass

mostrar_info(nombre='Ana', edad=30, ciudad='Madrid')"""

"""

def crear_usuario(*args, **kwargs):
    print("Nombre completo:", " ".join(args))
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

crear_usuario('Carlos', 'López', edad=28, email='carlos@example.com')"""

"""def crearvehiculos(nombre, placa, marca):
    frase = f"{nombre} tiene la placa {placa} de la marca{marca}"
    print(frase)

crearvehiculos("carro", "RT183", "chevelet")
crearvehiculos(marca = "AKT", nombre = "moto", placa = "VY858")"""

"""def suma(*args):
    lista = []
    resultado = 0
    for numero in args:
        resultado = numero
    return resultado
print(suma(1,2,10,20,30,50))
"""
""
#######################################3

"""def fusion(lista,*args):
    lista.extend(args)
    return lista
   
lista = ["messi", "cristiano", "beckham"]
nueva = fusion(lista,"maradona","pele", "ronaldinho")
print(nueva)"""

"""def combinar (*args):
    lista_nueva = []
    for x in args:
        if isinstance(x, list):
            lista_nueva.extend(x)
    return lista_nueva

lista1 = ["messi", "cristiano"]
lista2 = ["maradona"]
lista3 = ["ronaldinho", "neymar", "ronaldo", "rooney"]
lista_final = combinar(lista1,lista2,lista3)
print(lista_final)"""

"""def verificar_par_impar(numero):
 

  if numero % 2 == 0:
    return "Par"
  else:
    return "Impar"

# Ejemplo de uso con argumentos
numero_ejemplo = 10
resultado = verificar_par_impar(numero_ejemplo)
print(f"El número {numero_ejemplo} es: {resultado}")

numero_ejemplo = 7
resultado = verificar_par_impar(numero_ejemplo)
print(f"El número {numero_ejemplo} es: {resultado}")"""



"""
def multiplicacion(*args):
    result = 4
    for x in args:
        result *= x
    return result

print(multiplicacion(2))"""
"""

def combinaciones(*args, **kwargs):
    for palabras in args:
        print(f"el mejor deportista del mundo es {palabras}")
        continue
    for clave, valor in kwargs.items():
        print(f"{clave} : {valor}")
combinaciones("mariana pajon", "juan pablo montoya")
combinaciones("lionel messi", "john cena")
combinaciones(nombre = "nairo quintana", edad = 50)

  
def combinar_listas(*args):
  """"""
  resultado = []
  for lista in args:
    if isinstance(lista, list):
      resultado.extend(lista)
  return resultado

# Ejemplo de uso
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]
lista_combinada = combinar_listas(lista1, lista2, lista3)
print(lista_combinada)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

lista_mixta = combinar_listas(lista1, "hola", lista3, [10, 11])
print(lista_mixta) # Output: [1, 2, 3, 7, 8, 9, 10, 11]"""

"""""""""""def agregar_elementos(lista_destino, *args):
 
    for elemento in args:
        lista_destino.append(elemento)
    return lista_destino

# Ejemplo de uso
mi_lista = [1, 2, 3]
mi_lista = agregar_elementos(mi_lista, 4, 5, 6)
print(mi_lista) # Output: [1, 2, 3, 4, 5, 6]

mi_lista = agregar_elementos(mi_lista, [7, 8], 9)
print(mi_lista) # Output: [1, 2, 3, 4, 5, 6, [7, 8], 9]"""""""""""


