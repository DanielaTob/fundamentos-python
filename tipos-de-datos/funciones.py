# FUNCION: Es un bloque de código que solo se ejecuta cuando la llamamos. Permiten organizar y modularizar el código
# (REUTILIZACIÓN)


def saludar(nombre, nacionalidad="Colombia"): # Argumentos
    print("Hola " + nombre, "de", nacionalidad)


# saludar("Daniela", "Mexico") # Parametros
# saludar("Pedro")
# saludar("Ana")

def funcion():
    pass

#Sumar
def sumar(a,b):
    return a + b

resultado = sumar(2,3)
print(resultado)

# Restar
def resta(c,d):
    return c - d

resultadoResta = resta(10,70)
print(resultadoResta)

# Multiplicar 
def multiplicacion(e,f):
    return e * f

resultadoMultiplicar = multiplicacion(2,5)
print(resultadoMultiplicar)

# Dividir 
def dividir(g,h):
    return g / h

resultadoDividir = dividir(2,8)
print(resultadoDividir)