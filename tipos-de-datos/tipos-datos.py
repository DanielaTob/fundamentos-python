comillasSimples = 'Este es un texto'
comillasDobles = "Este es un texto"
comillasTriples = '''comillas triples'''
comillasTriplesDobles = """comillas triples dobles"""

print(comillasSimples)
print(comillasDobles)
print(comillasTriples)
print(comillasTriplesDobles)

# Números

a = 1
b = 3.14
c = 5 +  2j

print(a)
print(b)
print(c)

# Lista (Cada elemento tiene un indice, una posición) (mutable, los elementos pueden cambiar)

lista = [0, 1, 2, 3, 4, 5]

# Tuplas (Son inmutables, los elementos no pueden cabiar, tambien tienen indice)

tupla = ("a", "b", "c")

#Diccionario (Ordenado, mutable, no tiene indice, se accede a los elementos por su clave)

diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}


# Conjuntos (sets) (No tienen indice, no permiten elementos duplicados, son mutables) (Desordenado)

conjunto = {1,1,2,2,3} # Output: {1,2,3}


print(conjunto)

# booleanos (True o False)

booleanoVerdadero = True
booleanoFalso = False

print(booleanoVerdadero)