x = 5
y = 3
z = 10

if x > y or x > z:
    print("x es mayor a y yó x es menor a z")
elif x == y: 
    print("x es igual a y")
else: 
    print("Ninguna de las condiciones anteriores se cumplió")


a = "Python"
b = "Javascript"
c = "Python"

if a == c: 
    if a == b: 
        print("a es igual a c pero es distinto a b")
    else: 
        print("estoy saliendo por el else del if interno")
else: 
    print("a no es igual a b")


e = 10 
f = 10 

# Dejar el if vacio 

if e == f: 
    # No se que hacer si estas 2 variables son iguales
    pass # Para ignorar la estructura if hasta tanto definamos que comportamiento se espera