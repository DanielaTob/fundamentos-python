x = 1
y = 2.5
z = 1j

print(type(x))
print(type(y))
print(type(z))


positivo = 5.5
negativo = -5.5


imaginario = 5 + 1j

# De entero a flotante
xf = float(x) # obliga a x a comportarse como float

print(type(xf))
print(xf)

# De flotante a entero
ye = int(y) # obliga a y a comportarse como int
print(type(ye))
print(ye)

# De entero a complejo
entero = 5 
flotante = 5.5

enteroComplejo = complex(entero)
flotanteComplejo = complex(flotante)

print(enteroComplejo)
print(type(enteroComplejo))

print(flotanteComplejo)
print(type(flotanteComplejo))


import random 

print(random.randrange(1, 10)) # Devuelve un número aleatorio entre 1 y 9
