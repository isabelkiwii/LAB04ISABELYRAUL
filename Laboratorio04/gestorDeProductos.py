import archivos
from archivos import *





def mainMenu ():
    while True:
        print("\n")
        print("========================================================")
        print("Sistema de Gestion de Inventario de Productos")
        print("========================================================\n")
        print("1.Agregar Producto.")
        print("2.Eliminar Producto.")
        print("3.Actualizar precio de producto.")
        print("4.Listar productos.")
        print("5.Buscar producto.")
        print("6.Guardar Inventario en archivo.")
        print("7.Cargar inventario desde archivo.")
        print("8.Salir.\n")
        print("========================================================\n")
        menuOption = input("Digite una opción: ")

        menuOption = validateOption(menuOption)

        if menuOption == 1:
            archivos.addProduct()
        elif menuOption == 2:
            archivos.deleteProduct()
        elif menuOption == 3:
            archivos.updatePriceProduct()
        elif menuOption == 4:
            archivos.printProducts()
        elif menuOption == 5:
            archivos.searchProduct()
        elif menuOption == 6:
            archivos.saveProducts()
        elif menuOption == 7:
            archivos.loadProducts()
        elif menuOption == 8:
            print("See you later!")
            break

def validateOption(option):
    while True:
        try:
            option = int(option)
            if option >=1 and option <=8 and option % 1 == 0:
                return option
            else:
                print("Invalid argument.")
                option = input("Introduce a valid number: ")
        except ValueError:
            print("Invalid argument.")
            option = input("Introduce a valid number: ")
