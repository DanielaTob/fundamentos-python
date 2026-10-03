# LISTAS: Las listas son ordenadas, modificables y permiten valores duplicados

#            0          1           2           3
# frutas = ["Manzana", "Naranja", "Mandarina", "Naranja"]

# print(frutas)
# print(type(frutas))

# frutas[1] = "Banana"

# print(frutas[1])
# print(frutas)


# lista = ["Daniela", 5, True]
# print(lista)
# print(type(lista))


# # Cuantos elementos tiene una lista 
# print(len(lista))
# print(len(frutas))


# # Rango de indices 
# print(frutas[0:2])


# if "Manzana" in frutas: 
#     print("La manzana esta dentro de las frutas")


#             0        1       2
vehiculos = ["Auto", "Moto", "Avion"]

# Métodos para modificar listas 

# Append = Agregar elemento al fina de la lista 
#                   3
vehiculos.append("Barco")
print(vehiculos)

# Insert = Agregar elemento pero en que posicion 
vehiculos.insert(1, "Bicicleta")
print(vehiculos)

# Remove = Eliminar un elemento 
vehiculos.remove("Auto")
print(vehiculos)

# Pop = Remover pasando el indice
vehiculos.pop(1)
print(vehiculos)

# Sort = Ordenar vehiculos
vehiculos.sort()
print(vehiculos)

# Reverse = Ordenar a la inversa 
vehiculos.reverse()
print(vehiculos)


# Unir listas
coleccion1 = [1,2,3]
coleccion2 = [4,5,6]

coleccion3 = coleccion1 + coleccion2
print(coleccion3)

coleccion1.extend(coleccion2)
print(coleccion1)