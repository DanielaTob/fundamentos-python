import random 

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

numero = random.randint(0, 6)

match dias[numero]: 
    case "Lunes": 
        print("Hoy es Lunes")
    case "Martes": 
        print("Hoy es Martes")
    case "Miercoles": 
        print("Hoy es Miercoles")
    case "Jueves": 
        print("Hoy es Jueves")
    case "Viernes": 
        print("Hoy es Viernes")
    case "Sabado": 
        print("Hoy es Sabado")
    case "Domingo": 
        print("Hoy es Domingo")
    case _: 
        print("No coincide con ninguna de las opciones")