def serie_a(n):
    resultado = []
    patron = [1,1,0]
    for i in range(n):
        resultado.append(patron[i % 3])
    return resultado
    
def serie_b(n):
    resultado = []
    if n >= 1:
        resultado.append(3)
    if n >= 2:
        resultado.append(4)
    for i in range(2,n):
        siguiente = resultado[i-1] + resultado[i-2]
        resultado.append(siguiente)
    return resultado

   
n = int(input("Ingresemos el n: "))
vector = serie_a(n)
print("Serie A: ",vector)
print("Seria B: ",serie_b(n))

