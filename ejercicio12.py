


  

fac = 1

num = int(input("Ingrese el numero que quiere volver factorial: "))
for i in range(num):
    fac *= i+1
    num= num - 1
    print(i+1)
    print("*")
    
print("El factorial es:",fac )

 
