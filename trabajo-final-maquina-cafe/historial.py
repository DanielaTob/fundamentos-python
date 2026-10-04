ARCHIVO_PEDIDOS = "pedidos.txt"

def ver_historial():
    try: 
        print("\n Historial de pedidos")
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as archivo: # Lee el archivo
            pedidos = archivo.readlines()                             # Cada linea se archiva
            if pedidos:                                               # Si existen estas variables
                for i, pedido in enumerate(pedidos, start=1):         # Vamos a hacer un bucle que recorre los pedidos y enumerate nos da el indice y el pedido
                    print(str(i) + ". " + pedido.strip())             # Se imprime el numero y el pedido correspondiente al numero
            else:
                print("Aún no hay pedidos")
    except FileNotFoundError:
        print("\n Todavía no existe un historial de pedidos")
