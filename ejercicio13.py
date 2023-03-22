#Ejercicio 13:
#Realice un programa que pida al usuario un número, pregunte si quiere ingresar otro número,
# si la respuesta es “no” finalice el programa y muestre en pantalla la cantidad de números
# que se ingresaron y el valor resultante de sumar todos esos números.
contador = 0
acumulador = 0
while True:
    num = int(input("ingrese un número: "))
    contador = contador + 1 
    acumulador = acumulador + num
    otro = input("Desea ingresar otro número? 's' o 'n' ")
    if otro == "n":
        break
    else:
        True


print("Cantidad de números ingresados: ",contador)
print("Valor total de los números ingresados: ",acumulador)