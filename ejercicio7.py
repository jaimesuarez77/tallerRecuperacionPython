nombre=input("Ingrese el nombre de un producto: ")    
precio=float(input("Ingrese el precio del producto: "))
impuesto = .19
total = precio +(precio*impuesto)



if total > 80000    :
    print("El valor total supera los 80.000, el valor total mas impuestos: ", round(total) , "del articulo : ", nombre)
else:
     print("El valor total no supera los 80.000, el valor total  mas impuestos: ", round(total) , "del articulo : ", nombre)
 
