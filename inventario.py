# 1 - MOSTRAR MENU
def mostrar_menu():
        print("""   
____________________________________________________________________________________________
|         ******  BIENVENIDOS a  Quiosco Yoda's Snack ******                                |
|___________________________________________________________________________________________|
|                                                                                           |
|MENU DE OPCIONES:                                                                          |
|                                                                                           |
|        1 - Agregar producto al inventario.                                                |
|        2 - Realizar una venta.                                                            |
|        3 - Mostrar productos disponibles.                                                 |
|        4 - Salir.                                                                         |
|___________________________________________________________________________________________|
""")
        
# 1.1 VALIDAR MENU
def validar_opcion_menu(opcion : int) -> bool:
        """Valida si el numero esta entre 1 y 4 y retorna BOOL"""
        valido = False
        if opcion >= 1 and opcion <= 4:
                valido = True
        return valido


# 2 AGREGAR PRODUCTO AL INVENTARIO
def agregar_producto_nuevo (inventario : list[list]) -> list[list]:
    """Agrega un producto al inventario.

    Args:
        nombre (str)
        stock (int)
        precio (float)
        inventario (list)
    """
    nombre = input("Ingrese el nombre del producto: ")
    stock = int(input("Ingrese el stock del producto: "))

    if nombre in inventario[0]:
        columna_prod = buscar_producto_en_inventario(nombre, inventario)
        inventario[1][columna_prod]+=stock
    else: 
        precio = float(input("Ingrese el precio del producto: "))
        inventario[0].append(nombre)
        inventario[1].append(stock)
        inventario[2].append(precio)

# 3 - REALIZAR UNA VENTA
def realizar_venta(inventario : list[list]) :

    mostrar_inventario(inventario)
    producto_usuario = input("Ingrese el nombre del producto elegido: ")
    
    while buscar_producto_en_inventario(producto_usuario, inventario)== None :
        producto_usuario = input("Ingrese el nombre del producto elegido o escriba SALIR")
        if producto_usuario =="SALIR":
            return None

    cantidad_producto = int(input("Ingrese la cantidad que desea comprar: "))
    columna_producto = buscar_producto_en_inventario(producto_usuario, inventario)
    precio_producto = inventario[2][columna_producto]
    precio_total = cantidad_producto * precio_producto
    
    while cantidad_producto > (inventario[1][columna_producto]):
        cantidad_producto = int(input(f"No hay suficiente {inventario[0][columna_producto]}, ingrese la cantidad que desea comprar: "))

    inventario[1][columna_producto] -=  cantidad_producto
    if inventario[1][columna_producto] == 0:
        inventario[0].pop(columna_producto)
        inventario[1].pop(columna_producto)
        inventario[2].pop(columna_producto)
    print (f"El precio es ${precio_total}")
    

# 3.1 - BUSCAR EN INVENTARIO
def buscar_producto_en_inventario(producto_usuario : str, inventario : list[list]) -> int :
    """Busca la ubicación de un producto en una matriz

    Args:
        producto_usuario (str)
        inventario (list[list])

    Returns:
        int: Nro de columna de la matriz en la que está en producto
    """
    
    for i in range (len(inventario[0])):
        if inventario[0][i] == producto_usuario :
            return i
    return None
    

# 4 - MOSTRAR INVENTARIO
def mostrar_inventario(inventario: list[list]): # Punto 3 - mostrar lista de productos disponibles
    """Muestra en pantalla los productos disponibles del inventario.

    Args:
        inventario (list[list])
    """
    num_filas = len(inventario)
    num_columnas = len(inventario[0])
    print (" ")
    print ("NOMBRE / STOCK / PRECIO")
    print (" ")
    for j in range (num_columnas):
        for i in range (num_filas):
            print (inventario[i][j], end=" / ")
        print ("")

