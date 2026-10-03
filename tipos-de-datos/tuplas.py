# TUPLA: Coleccion ordenada e inmutable de elementos que permiten duplicados 

#                 0           1         2       3
tecnologias = ("Python", "Javascript", "Go", "Python")

print(tecnologias)
print(tecnologias[1])

print(len(tecnologias))

print(type(tecnologias))

fruta = ("Manzana",) # se considera tupla con un solo valor
print(type(fruta))

tupla = ("Python", 5, True)
print(type(tupla))

x, y, z = tupla
print(x)
print(y)
print(z)

tupla1 = (1,2,3)
tupla2 = (3,4,5)
tupla3 = tupla1 + tupla2
print(tupla3)


# Duplicar los datos de una tupla 
tupla = ("Python", 5, True)
print(tupla * 2)

# Recorrer tuplas 
for item in tupla: 
    print(item)

print("----------------------------------------")

# Converir la tupla en lista para modificarla y luego devolverla a tupla 

tuplaAModificar = ("Python", "Javascript", "Go")
listaComodin = list(tuplaAModificar)
listaComodin.append("ReactJS")

tuplaAModificar = tuple(listaComodin)
print(tuplaAModificar)
