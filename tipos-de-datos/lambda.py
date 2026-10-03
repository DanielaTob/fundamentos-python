# Lambda es una función pequeña y anónima que puede tener muchos argumentos pero solo una expresión

# Sintaxis: - palabra lambda - argumentos - : - expresión

# b es la variable 
# la landa va a esperar un argumento, que es a 
# ese argumento (a) se le va a sumar a 10 
# Si le pasamos 5, daría 10 

b = lambda a : a + 10

print(b(5)) # Output 15


print("----------------------------------------")

# Dos argumentos 
# x = lambda a, b : a + b

# print(x(2,3)) # Output 5


# Fabricar Funciones 
def miFuncion(n):
    return lambda a : a * n

duplicador = miFuncion(2)
triplicador = miFuncion(3)
quintuplicador = miFuncion(5)

print(duplicador(5)) # 10
print(triplicador(5)) # 15
print(quintuplicador(5)) # 25



