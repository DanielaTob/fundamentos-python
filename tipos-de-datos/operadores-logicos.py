# Operadores de Comparación

x = 5
y = 3
z = 5

print(x == y) # ¿Si es igual? False
print(x != y) # ¿Si es diferente? True
print(x > y) # ¿Si es mayor? True
print(x < y) # ¿Si es menor? False

print (x >= y) # ¿Es mayor o igual? True
print(x >= z) # ¿Es mayor o igual? True
print(x <= z) # ¿Es menor o igual? True

# Operadores Logicos (usar más de una condicion)

#     True     False  
print(x > y and y > z) # False (porque no se cumplen las dos, solo una)
print(x > y or y > z) # True (porque se cumple una de las dos)

# Negacion not 

v = True 
f = False 

print(not(v)) # False
print(not(f)) # True