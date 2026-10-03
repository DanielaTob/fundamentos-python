v = True
f = False

print(v)
print(f)

print(5 > 3) # Output: True
print(3 > 5)  # Output: False

print(type(v))

print(bool("Hola Mundo")) # Output: True
print(bool("")) # Output: False


# True 
print(bool("abc"))
print(bool(123))
print(bool(["Manzana", "Pera"]))

#False
print(bool(""))
print(bool(0))
print(bool([]))
print(bool(None))


# isinstance
x = 123

print(isinstance(x, int))