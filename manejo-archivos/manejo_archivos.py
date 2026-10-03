# open(nombre, modo)

# R (read) Lectura
# W (write) Escritura
# X (Crea archivo nuevo)

# try: 
#     f = open("archivo.txt", "r")
#     print(f.readline())
#     f.close()
# except FileNotFoundError:
#     print("No se ha encontrado el archivo")

# Read
try: 
    with open("archivo.txt", "r") as f: 
        print(f.readline())
        print(f.readline())
except FileNotFoundError:
    open("archivo.txt", "x") # Si no existe el archivo lo crea
    print("No se ha encontrado el archivo")

# Write  (Sobre escribe lo que haya estado en el archivo)
# try: 
#     with open("archivo.txt", "w") as f: 
#         f.write("Hola mundo desde write en el with")
#     with open("archivo.txt", "r") as f:
#         print(f.readline())
# except FileNotFoundError:
#     print("No se ha encontrado el archivo")


#Append (Agrega la información al final)
try: 
    with open("archivo.txt", "a") as f: 
        f.write("\n")
        f.write("Hola mundo desde write en el with")
    with open("archivo.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("No se ha encontrado el archivo")