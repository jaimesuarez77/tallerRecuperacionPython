x=float(input("Ingrese un nùmero: "))

condicion = input("Desea agregarle al nùmero ingresado el 30%: si o no ")
if condicion == "si" or condicion == "SI" or condicion == "Si":
    print("El valor ingresado mas el 30% es: ", round(x*1.30))
else:
    print("La operacion no se realizo: ")
 
