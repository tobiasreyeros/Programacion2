n=0
resultado=0

def calcular_factorial(n):
    
    n=int(input("Ingrese un número entero positivo: "))
    
    while (n < 0):
        print("El número debe ser positivo.")
        n=int(input("Ingrese un número entero positivo: "))
        
        while (n==float(n)):
            print("El número debe ser un entero.")
        n=int(input("Introduce un número entero: "))
   
    resultado=1
       
    for i in range(1, n + 1):
        resultado=resultado * i

    print("El factorial de ",n," es: ",resultado)

calcular_factorial(n)