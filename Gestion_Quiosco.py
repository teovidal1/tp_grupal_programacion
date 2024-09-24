from inventario import *

NOMBRES = ["Chupetin Sable de luz", "Agua La Fuerza", "Gomitas Holocubo", "Barrita de cereal Wookiee", "Galletitas R2D2"]
STOCK = [50, 35, 25, 48, 20]
PRECIO = [200, 3200, 990, 2500, 15800]
inventario = [NOMBRES, STOCK, PRECIO]
#Lo asignamos de esta forma para que sea más legible, pero sería más simple asignar todas las listas por extensión en la matriz inventario

TERMINAR = False
contador_errores = 0

while TERMINAR == False and contador_errores<3 :
        mostrar_menu()
        opcion = int(input("Ingrese la opción del menú deseada: "))
                
        if validar_opcion_menu(opcion) :
                
                match opcion:
                        case 1:
                                agregar_producto_nuevo(inventario)
                        case 2:
                                realizar_venta(inventario)
                        case 3:
                                mostrar_inventario(inventario)
                                print (" ")
                        case 4:
                                TERMINAR = True
        else:
                print("""Por favor, ingrese una opcion correcta.""")
                contador_errores +=1

print("Saliendo..... Hasta pronto!")