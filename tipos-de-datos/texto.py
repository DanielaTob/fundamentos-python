print("Hola 'mundo'")
print('Hola "mundo"')

ingles = "I'm Daniela"

multiples = """Hola 
Mundo
desde
las
comillas
triples"""

print(ingles)
print(multiples)

# Cuantos caracteres tiene una palabra 

palabra = "Mircielago"
print(len(palabra))

# Palabra Python incluida en el texto (Case sensitive) (es decir si es en mayuscula o minuscula importa)

texto = "Este curso es de fundamentos de Python"
estaIncluida = "Python" in texto
noEstaIncluida = "Javascript" not in texto

print(estaIncluida)
print(noEstaIncluida)

# Cambiar a mayuscula o minuscula

mayuscula = texto.upper()
minuscula = texto.lower()

print(mayuscula)
print(minuscula)


espacios = "          Este es el texto         "
sinEspacios = espacios.strip() # Elimina los espacios al inicio y al final del texto

print(sinEspacios)