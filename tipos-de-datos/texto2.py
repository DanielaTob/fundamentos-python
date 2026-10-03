# indice 01234 
texto = "Este es un texto"

print(texto[4])

# slicing (tomar una parte del texto)
print(texto[0:4]) # Output: Este
print(texto[0:15]) # Output: Este es un text (o no incluida) hay que contar uno de más

print(texto[:7]) # Output: Este es
print(texto[5:]) # Output: es un texto

print(texto[5:-2]) # Output: es un tex


# Reemplazar texto

curso = "Este curso es de Javascript"
print(curso.replace("Javascript", "Python"))

textoDividido = texto.split(" ")

print(textoDividido)

# Normalización 

texto2 = "Este texto tiene MAYUSCULAS y minusculas y necesito encontrar ciertas palabras"

print("mayusculas".lower() in texto2.lower())



