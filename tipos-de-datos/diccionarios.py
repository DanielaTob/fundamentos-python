# DICCIONARIO: Colección de pares clave valor (Ordenado a partir de Python 3.7)

auto = {
    "Marca": "Renault",
    "Modelo": "Clio",
    "Año": 2025
}

print(auto)

# Solo quiero saber la marca 
print(auto["Marca"])
print(auto.get("Marca"))

# Solo quiero la clave no el valor 
print(auto.keys())

# Solo valores 
print(auto.values())

if "Marca" in auto:
    print("Marca es una de las propiedades de este diccionario")

# Sobre esccribir un valor
auto["Año"] = 2020
print(auto)

# Agregar nueva clave y valor
auto["Color"] = "Verde"
print(auto)

# Update 
auto.update({"Año": 2022, "Puertas": 4})
print(auto)


# Eliminar elementos
# auto.pop("Puertas")
# print(auto)

# Elimina el ultimo elemento
# auto.popitem()
# print(auto)

# Vaciar el diccionario 
# auto.clear()
# print(auto)


# Recorremos las claves 
for k in auto:
    print(k)

print("----------------------------")

# Recorremos los valores
for v in auto.values():
    print(v)

print("----------------------------")

# Recorrer ambos clave y valor
for k,v in auto.items():
    print(k,v)

print("----------------------------")

# Diccionarios Anidados = Objetos directos
familia = {
    "hijo1" : {
        "nombre": "Pedro",
        "edad" : 8

    },
    "hijo2" : {
        "nombre": "Ana",
        "edad" : 7
    },
    "higo3" : {
        "nombre": "Marcelo",
        "edad" : 6
    }
}

print(familia["hijo1"]["nombre"])