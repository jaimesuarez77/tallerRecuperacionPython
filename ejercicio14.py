tiposProductos = ['bebidas','barras','papas','galletas']
preciosProductos = [1900,1000,1600,1300]
print("Tenemos una variada selecciond de productos: ")

for i in range(len(tiposProductos)):    
    print(i,tiposProductos[0+i],preciosProductos[0+i])

presupuesto=int(input("Segùn su seleccion ingrese su presupuesto: "))
produc_comprado= int(input("Ingrese el número del productos de su elección: "))
if produc_comprado == 0:
    precioProducto = 1900
    if presupuesto<precioProducto:
        print("Saldo insufisiente...")
       
    else:
        print("Su compra fue de Bebidas por $1.900... le que un saldo de : ",presupuesto-precioProducto)    
elif produc_comprado == 1:
    precioProducto = 1000
    if presupuesto<precioProducto:
        print("Saldo insufisiente...")
    else:
        print("Su compra fue de Barras por $1.000... le que un saldo de : ",presupuesto-precioProducto)    
elif produc_comprado == 2:
    precioProducto = 1600
    if presupuesto<precioProducto:
        print("Saldo insufisiente...")
    else:
        print("Su compra fue de papas por $1.600... le que un saldo de : ",presupuesto-precioProducto) 
elif produc_comprado == 3:
    precioProducto = 1300
    if presupuesto<precioProducto:
        print("Saldo insufisiente...")
    else:
        print("Su compra fue de galletas por $1.300... le que un saldo de : ",presupuesto-precioProducto)         
else:
    print("El código del producto no es correcto...")
