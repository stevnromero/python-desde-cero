"""johan = {"Nombre" : "johan", 
         "Equipo_favorito" : "Fc Barcelona",
         "edad" : 22,
         "intereses" : ["futbol", "programacion", "musica", "telenovelas"]
         }
print(johan)


Juanita = {"Nombre" : "juanita", 
         "Equipo_favorito" : "Fc Barcelona",
         "edad" : 26,
         "intereses" : ["patines", "baile", "musica", "lectura", "gimnasio"]

         }

print(Juanita)

relationship = {0:johan, 1:Juanita}
print(relationship)

print(type(johan))
print(type(Juanita))

frase = f"{"johan"} es hincha de {"Fc barcelona"}"
frase = f"cuanto es la longitud de johan: {len(johan)}"
print(frase)

frase1 = f"{"juanita"} es hincha de {"Fc barcelona"}"
frase1 = f"cuanto es la longitud de juanita: {len(Juanita)}"
print(frase1)


print(johan["edad"])
print(Juanita["intereses"])"""


# Valores duplicados que tienen que contener una clave y un valor ya que los valores se sobrescriben
"""Juanita = {"Nombre" : "juanita", 
         "Equipo_favorito" : "Fc Barcelona",
         "edad" : 26,
         "intereses" : ["patines", "baile", "musica", "lectura", "gimnasio"],
         "Comida favorita" : "Pasta",
         "Comida favorita" : "pizza",
         }

print(Juanita)
print(len(Juanita))


aprendiz = dict(
    nombre = "johan",
    edad = 22,
    deportes = "futbol",         
    ciudad = "Bogotá D.C."            
                
                )

print(aprendiz)
print(len(aprendiz))
"""


# Agregar, modificar y eliminar los elementos de una lista


"""Juanita = {"Nombre" : "juanita", 
         "Equipo_favorito" : "Fc Barcelona",
         "edad" : 26,
         "intereses" : ["patines", "baile", "musica", "lectura", "gimnasio"],
         "Comida favorita" : "pizza",
         }"""

"""print("agregar elementos:")
Juanita["instrumento"] = "guitarra"
print(Juanita)

Juanita.update({"color" : "rojo", "bebida" : "limonada"})
print(Juanita)
"""
"""print("eliminar un elemento:")
del Juanita ["Comida favorita"]
print(Juanita)

Juanita.pop("edad")
print(Juanita)

Juanita.popitem()
print(Juanita)
"""

"""print("acceder elementos:")
edad = Juanita["edad"]
print(f"la edad de Juanita es {edad}")

x = Juanita["instrumento"]
x = Juanita.get("instrumento")
print(x)
print(x)
print(Juanita.keys())
print(Juanita.items())
print(Juanita.values())

if "comida favorita" in Juanita:
    print("si esta en la lista")

else: 
    print("no aparece en el diccionario")


print("cambiar elementos:")
Juanita["instrumento"] = "Bateria"
print(Juanita)
Juanita.update({"comida favorita" : "hamburguesa", "edad" : "43"})
print(Juanita)"""


"""Juanita = {"Nombre" : "juanita", 
         "Equipo_favorito" : "Fc Barcelona",
         "edad" : 26,
         "intereses" : ["patines", "baile", "musica", "lectura", "gimnasio"],
         "Comida favorita" : "pizza",
         }"""


"""for clave , valor in Juanita.items():
    print(f"{clave} === {valor}")

for y in Juanita.keys():
    print( y)

for x in Juanita.get("Comida favorita"):
    print(x)

Juanita.copy()
print(Juanita)

a = dict(Juanita)
print(a)"""


# Diccionarios Anidados


mis_luchadores_favoritos_WWE = {
    "luchador 1" : {
        "nombre" : "John Cena",
        "edad" : 47,
        "n.titulos" : 17,
        "fecha_nacimiento" : "23/4/2025",
        "pais" : "Estados Unidos"
        
        },

    "luchador 2" : {
        "nombre" : "Triple H",
        "edad" : 56,
        "n.titulos" : 14,
        "fecha_nacimiento" : "27/7/1969",
        "pais" : "Estados Unidos"
        },

     "luchador 3" : {
        "nombre" : "Seth Rollins",
        "edad" : 39,
        "n.titulos" : 6,
        "fecha_nacimiento" : "28/5/1986",
        "pais" : "Estados Unidos"   
     }


}

for clave, valor in mis_luchadores_favoritos_WWE.items():
    print(f"clave principal: {clave} ")
    
    for clave_1 , valor_1 in valor.items():
        print(f"clave anidada ## {clave_1}: {valor_1}")

for clave, valor in mis_luchadores_favoritos_WWE.items():
    if valor["edad"] > 50:
        print(f"{valor["nombre"]} tiene mas de 50 años.")
    elif valor["edad"] == 47:
        print(f"{valor["nombre"]} es un poco mayor")
    else:
        print(f"{valor["nombre"]} es muy joven.")



#formula del bucle con diccionario anidado
"""
diccionario_anidado = {
    'llave1': {'sub_llave1': 'valor1', 'sub_llave2': 'valor2'},
    'llave2': {'sub_llave3': 'valor3', 'sub_llave4': 'valor4'}
}

# Iterar sobre el diccionario anidado
for llave_externa, valor_externo in diccionario_anidado.items():
    print(f"Clave externa: {llave_externa}")
    for sub_llave, sub_valor in valor_externo.items():
        print(f"\tClave interna: {sub_llave}, Valor: {sub_valor}")

        #salida
        Clave principal: persona1
	Clave anidada: nombre, Valor: Ana
	Clave anidada: edad, Valor: 30
Clave principal: persona2
	Clave anidada: nombre, Valor: Carlos
	Clave anidada: edad, Valor: 25
Clave principal: persona3
	Clave anidada: nombre, Valor: Laura
	Clave anidada: edad, Valor: 35
"""


