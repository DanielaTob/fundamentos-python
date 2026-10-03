# Conjunto (set): Colección no ordenada de elementos únicos 
# NO hay duplicados, se ignoran
# NO se puede acceder por indice 

frutas = {"Manzana", "Naranja", "Mandarina", "Naranja"}
print(frutas)
print(type(frutas))
print(len(frutas))

print("Manzana" in frutas)
print("Pera" not in frutas)

# Agregar elementos y luego eliminarlos 

# Add 
frutas.add("Pera")
print(frutas)

# Update 
frutasTropicales = {"Piña", "Mango"}
frutas.update(frutasTropicales) # Agregar listas, tuplas, conjuntos
print(frutas)

# Eliminarlos
frutas.remove("Mango") # Si no existe aparece error
print(frutas)

frutas.discard("Banana") # Si no existe NO aparece error 
print(frutas)

# Pop = Elimina aleatorio
frutas.pop()
print(frutas)

# Clear = Vaciar el conjunto
frutas.clear()
print(frutas)


# conjuntos = {"Python", 5, True}
# print(conjuntos)
# print(type(conjuntos))

# # No van a estar ordenados

# for item in conjuntos: 
#     print(item) # Output True 5 Python



print("-----------------------------------------")

# Operaciones entre conjuntos 

a = {"a", "b", "c"}
b = {"c", "d", "e"}

# Union 
c = a.union(b)
print(c)

# Interseccion 
i = a.intersection(b)
print(i)

# Diferencia 
d = a.difference(b)
print(d)