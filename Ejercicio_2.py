def suma_serie(n):
    suma = 0.0
    for i in range(1,n+1):
        suma += 1/i
    return suma
    
def mostrar():
    n = int(input("Ingrese el numero: "))
    resultado = suma_serie(n)
    print("La suma es: ", round(resultado,5))
          
mostrar()