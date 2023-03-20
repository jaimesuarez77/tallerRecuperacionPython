nombre=input("Ingrese el nombre de un producto: ")    


def imp(precio):
    x = precio*1.19
    return x

def monto(valorT):
    if valorT>80000:
        print("El valor total sumpera los 80.000")
    else:
        print("El valor total es menor de  80.000")
    return valorT    
        
while True:

    precio = imp(float(input("Ingrese el precio del producto: ")))
    valorTotal = monto(precio)
    print("El nombre del producto es: "+ nombre + " y su precio total es : "+ str(round(precio)))
    
    break



 
