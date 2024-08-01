products = []
import pickle
import json

def addProduct():
    code = input("Digite el código del producto: ")
    while True:
        try: #añadir una validacion que no exista el producto
            code = int (code)
            break
        except ValueError:
            print("Argumento inválido.")
            code = input("Digite el código del producto: ")
    
    name = input("Digite el nombre del producto: ")

    brand = input("Ingrese la marca del producto: ")
    
    price = input("Ingrese el precio del producto: ")
    while True:
        try:
            price = int (price)
            break
        except ValueError:
            print("Argumento inválido.")
            price = input("Ingrese el precio del producto: ")
    
    quantity = input("Ingrese la cantidad de existencias del producto: ")
    while True:
        try:
            quantity = int (quantity)
            break
        except ValueError:
            print("Argumento inválido.")
            quantity = input("Ingrese la cantidad de existencias del producto: ")
    
    providerName = input("Ingrese el nombre del proveedor: ")
    providerCode = input("Ingrese el código del proveedor: ")
    while True:
        try:
            providerCode = int (providerCode)
            break
        except ValueError:
            print("Argumento inválido.")
            providerCode = input("Ingrese el código del proveedor: ")
    providerCountry = input("Ingrese el país del proveedor: ")
    
    provider = dict (code = "", name = "", country = "")
    provider ["code"] = providerCode
    provider ["name"] = providerName
    provider ["country"] = providerCountry

    class Product:
        def __init__(self,code,name,brand,price,quantity,provider):
            self.code = code
            self.name = name
            self.brand = brand
            self.price = price
            self.quantity = quantity
            self.provider = provider
        def __str__(self):
            return f"Código: {self.code}, Nombre: {self.name}, Marca: {self.brand}, Precio: {self.price}, Cantidad: {self.quantity}, Proveedor: {self.provider}"
        def formatToFile(self):
            return {'code':self.code, 'name': self.name, 'brand': self.brand, 'price': self.price, 'provider': self.provider}
    product = Product(code = code, name = name, brand = brand, price = price, quantity = quantity, provider = provider)
    products.append(product)

    printProducts()


def deleteProduct():
    indexNumber = 'F'
    code = input("Introduzca el código del producto que desea eliminar: ")
    while True:
        try:
            code = int (code)
            break
        except ValueError:
            print("Argumento inválido.")
            code= input("Introduzca el código del producto que desea eliminar: ")
    for i in range(0,len(products)):
        if code == products[i].code:
            indexNumber = i
    if indexNumber != 'F':
        del products[indexNumber]
    else: 
        print("No existe un producto con ese código registrado.")
    print("El producto se eliminó correctamente.")

    printProducts()


def printProducts():
    print("\nEsta es la lista de productos existentes en el inventario: \n")
    for i in range (0,len(products)):
        print(products[i].__str__())



def updatePriceProduct():
    indexNumber = 'F'
    code = input("Introduzca el código del producto al que desea actualizar el precio: ")
    while True:
        try:
            code = int (code)
            break
        except ValueError:
            print("Argumento inválido.")
            code= input("Introduzca el código del producto que desea eliminar: ")
    for i in range(0,len(products)):
        if code == products[i].code:
            indexNumber = i
    if indexNumber != 'F':
        price = input("Introduzca el nuevo precio del producto: ")
        while True:
            try:
                price = int (price)
                break
            except ValueError:
                print("Argumento inválido.")
                price = input("Introduzca el nuevo precio del producto: ")
        products[indexNumber].price = price
    else: 
        print("No existe un producto con ese código registrado.")
    print("El precio del producto se actualizó correctamente.")

    printProducts()


def searchProduct():
    indexNumber = 'F'
    code = input("Introduzca el código del producto al que desea visualizar: ")
    while True:
        try:
            code = int (code)
            break
        except ValueError:
            print("Argumento inválido.")
            code= input("Introduzca el código del producto que desea eliminar: ")
    for i in range(0,len(products)):
        if code == products[i].code:
            indexNumber = i
    if indexNumber != 'F':
       print("\nEstos son los detalles del producto: \n")
       print(products[indexNumber])
    else: 
        print("No existe un producto con ese código registrado.")


def saveProducts():
    with open("inventario.txt", 'w') as f:
        for i in range(0,len(products)):
            f.write(f"{products[i].formatToFile()}")
    print("Inventario guardado en el archivo 'inventario.txt'")


def loadProducts():
    with open("inventario.txt", 'r') as f:
        products.append(line.strip() for line in f)
    print("Inventario cargado desde el archivo 'inventario.txt'")
    



 

  