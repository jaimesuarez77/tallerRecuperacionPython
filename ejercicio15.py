#Ejercicio 15:
#Se está realizando una obra de teatro para recaudar fondos, se quiere recaudar 
#un total de 1.000.000$. Para la obra hay 3 valores de entradas: la entrada básica de 20.000$, 
#la entrada premium de 40.000 $ y la entrada VIP de 100.000$. 
#Realice un programa en el que se pregunte al usuario por el tipo entrada que quiere comprar, 
#después de ingresar el tipo de entrada el programa saca en pantalla “Disfrute la función”,
#esto se repetirá para el siguiente usuario. El programa se detendrá cuando el dinero acumulado 
#por las entradas sea mayor a 1.000.000$, cuando esto pase, mostrar en pantalla el porcentaje de 
#usuarios que compro cada entrada y el promedio total de entrada contra usuario. 

basica = 20000
premium = 40000
vip = 100000
monto = 1000000
caja = 0
personas = 0
per_uno = 0
per2 = 0
per3 = 0
print("Bienvenido al teatro  ")
print("Què tipo de entrada va a elegir: ")

while caja < monto:
    entrada = int(input(" Bàsica: (1), Premium: (2), VIP: (3) "))
    if entrada == 1:      
        caja = caja + 20000
        personas = personas + 1
        per_uno = per_uno + 1
   

        print("Disfrute la funciòn: ")
    elif entrada == 2:
        print("Disfrute la funciòn: ")
        caja = caja + 40000
        personas = personas + 1
        per2=per2+1
    elif entrada == 3:
        print("Disfrute la funciòn: ")
        caja = caja + 100000
        personas = personas + 1
        per3=per3+1
    else:
        print("El nùmero ingresado no es valido")
        break
porPer1=per_uno/personas
porPer2=per2/personas
porPer3=per3/personas
print("El valor recaudado fue de: ",caja," Asistieron ", personas, "Personas")
print("Porcentaje de personas con entrada basica: ",round(porPer1),"%")
print("Porcentaje de personas con entrada basica: ",round(porPer2),"%")
print("Porcentaje de personas con entrada basica: ",round(porPer3),"%")